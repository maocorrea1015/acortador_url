

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

- **Python 3.12+**
- **Flask** (Framework para la API web)
- **PyMySQL** (Conexión a base de datos MySQL)
- **MySQL o MariaDB** (Base de datos para almacenar las URLs)
- **Docker** (Para ejecutar la aplicación en contenedores)

## Instalación y Ejecución

### Opción 1: Ejecutar localmente

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
   pip install -e .
   ```

4. Crea la base de datos y la tabla `urls` en MySQL:

   ```sql
   CREATE DATABASE acortador;
   USE acortador;

   CREATE TABLE urls (
       id INT AUTO_INCREMENT PRIMARY KEY,
       original_url TEXT,
       short_url VARCHAR(6),
       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
       clicks INT DEFAULT 0
   );
   ```

5. Configura las variables de entorno en `db.py` o establece las variables de entorno:

   ```bash
   export DB_HOST=localhost
   export DB_USER=root
   export DB_PASSWORD=tu_password
   export DB_NAME=acortador
   ```

6. Ejecuta la aplicación:

   ```bash
   python app.py
   ```

### Opción 2: Ejecutar con Docker

1. Asegúrate de tener Docker y Docker Compose instalados.

2. Clona el repositorio y navega al directorio:

   ```bash
   git clone <URL DEL REPOSITORIO>
   cd <NOMBRE DEL REPOSITORIO>
   ```

3. Construye y ejecuta los contenedores:

   ```bash
   docker-compose up --build
   ```

   Esto iniciará la aplicación Flask en `http://localhost:5000` y MySQL en `localhost:3306`.

4. La base de datos se creará automáticamente con la tabla `urls`.

## Uso de la API

### 1. Generar una URL corta

**Endpoint**: `GET /?url=<URL>`

Este endpoint recibe una URL larga como parámetro de query y devuelve un enlace corto completo.

- **URL de la solicitud**: `http://127.0.0.1:5000/?url=https://www.example.com`
- **Método**: `GET`
  
- **Respuesta**:
  
  ```json
  {
    "success": true,
    "short_url": "http://127.0.0.1:5000/abc123",
    "original_url": "https://www.example.com"
  }
  ```

Si no se proporciona el parámetro `url`, devuelve un mensaje de uso.

### 2. Redirigir usando una URL corta

**Endpoint**: `GET /<short_url>`

Este endpoint recibe una URL corta y redirige al usuario a la URL original.

- **URL de la solicitud**: `http://127.0.0.1:5000/<short_url>`
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
├── pyproject.toml        # Configuración del proyecto y dependencias
├── Dockerfile            # Archivo para construir la imagen Docker de la app
├── docker-compose.yml    # Configuración para ejecutar la app y la base de datos con Docker
├── .dockerignore         # Archivos a ignorar en la construcción de Docker
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

