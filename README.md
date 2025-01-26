

---

# URL Shortener API

Esta es una API para acortar URLs y redirigir a las URLs originales a partir de un enlace corto. Permite recibir una URL larga, generar un enlace corto único y almacenar esta información en una base de datos MySQL. También ofrece la funcionalidad de redirigir a la URL original al proporcionar el enlace corto.

## Funcionalidades

1. **Generación de URL corta**
   - Permite enviar una URL larga a la API y recibir una URL corta.
   - La URL corta se genera de manera aleatoria y se guarda en la base de datos junto con la URL original.
   - Un contador de clics se incrementa cada vez que se hace clic en la URL corta.

2. **Redirección con URL corta**
   - Al proporcionar una URL corta, la API redirige a la URL original.
   - Se incrementa el contador de clics cada vez que un usuario visita la URL corta.

## Requisitos

- **Python 3.x**
- **Flask** (Framework para la API web)
- **PyMySQL** (Conexión a base de datos MySQL)
- **MySQL o MariaDB** (Base de datos para almacenar las URLs)

## Instalación

1. Clona este repositorio a tu máquina local:

   ```bash
   git clone <URL DEL REPOSITORIO>
   cd <NOMBRE DEL REPOSITORIO>
   ```

2. Crea un entorno virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate     # Para Windows
   ```

3. Instala las dependencias necesarias:

   ```bash
poetry install
   ```

4. Crea la base de datos y la tabla `urls` en MySQL:

   ```sql
   CREATE DATABASE url_shortener;
   USE url_shortener;

   CREATE TABLE urls (
       id INT AUTO_INCREMENT PRIMARY KEY,
       original_url TEXT,
       short_url VARCHAR(6),
       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
       clicks INT DEFAULT 0
   );
   ```

5. Configura tu archivo `db.py` con la información de conexión a tu base de datos:

   ```python
   import pymysql

   def conectar_db():
       return pymysql.connect(
           host='localhost',
           user='tu_usuario',
           password='tu_contraseña',
           db='url_shortener',
           charset='utf8mb4',
           cursorclass=pymysql.cursors.DictCursor
       )
   ```

## Uso de la API

### 1. Generar una URL corta

**Endpoint**: `POST /shorten`

Este endpoint recibe una URL larga y devuelve un enlace corto.

- **URL de la solicitud**: `http://127.0.0.1:8080/shorten`
- **Método**: `POST`
- **Cuerpo de la solicitud (JSON)**:
  
  ```json
  {
    "url": "https://www.example.com"
  }
  ```

- **Respuesta**:
  
  ```json
  {
    "success": true,
    "short_url": "abc123",
    "original_url": "https://www.example.com"
  }
  ```

### 2. Redirigir usando una URL corta

**Endpoint**: `GET /<short_url>`

Este endpoint recibe una URL corta y redirige al usuario a la URL original.

- **URL de la solicitud**: `http://127.0.0.1:8080/<short_url>`
- **Método**: `GET`
  
  Por ejemplo, si la URL corta generada es `abc123`, la URL sería:

  `http://127.0.0.1:8080/abc123`

- **Respuesta**:
  - Si la URL corta existe: El navegador se redirige automáticamente a la URL original.
  - Si la URL corta no existe:

    ```json
    {
      "success": false,
      "error": "URL no encontrada"
    }
    ```

## Estructura de Archivos

```
.
├── app.py                # Contiene la lógica principal de la API
├── db.py                 # Contiene la función de conexión a la base de datos
├── requirements.txt      # Listado de dependencias para instalar
└── README.md             # Documentación del proyecto
```

## Contribuciones

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama para tus cambios (`git checkout -b mi-rama`).
3. Realiza los cambios y haz commit de ellos (`git commit -am 'Agregué nueva funcionalidad'`).
4. Haz push a tu rama (`git push origin mi-rama`).
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

