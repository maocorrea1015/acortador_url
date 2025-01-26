from flask import Flask, request, jsonify, redirect
import pymysql
from db import conectar_db
import string
import random

app = Flask(__name__)


def generar_seudolink(length=6):
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choices(caracteres, k=length))

@app.route('/shorten', methods=['POST'])
def Sorten_url():
    try:
        data = request.get_json()
        original_url = data.get('url')

        if not original_url:
            return ({"success": False, "error": "No se proporcionó una URL válida"}), 400

        seudolink = generar_seudolink()

        connection = conectar_db()
        query = "INSERT INTO urls (original_url, short_url, created_at, clicks) VALUES (%s, %s, NOW(), 0)"
        with connection.cursor() as cursor:
            cursor.execute(query, (original_url, seudolink))
            connection.commit()


        return jsonify({
            "success": True,
            "short_url": seudolink,
            "original_url": original_url
        }),201
    
    except pymysql.MySQLError as e:
        return jsonify({"success":False, "error":str(e)}), 500

    finally:
        if 'connection' in  locals() and connection.open:
            connection.close


@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
    try:
        connection = conectar_db()
        query = "SELECT original_url FROM urls WHERE short_url = %s"
        with connection.cursor() as cursor:
            cursor.execute(query, (short_url,))
            result = cursor.fetchone()

        if result:
            update_query = "UPDATE urls SET clicks = clicks + 1 WHERE short_url = %s"
            with connection.cursor() as cursor:
                cursor.execute(update_query, (short_url,))
                connection.commit()

            return redirect(result['original_url'])

        else:
            return jsonify({"success": False, "error": "URL no encontrada"}), 404

    except pymysql.MySQLError as e:
        return jsonify({"success": False, "error": str(e)}), 500

    finally:
        if 'connection' in locals() and connection.open:
            connection.close()






if __name__ == '__main__':
    app.run(debug=True, )