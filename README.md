 🚀 Microservicio de Álbumes y Canciones - CineMusic

## 📋 Descripción
Este microservicio es parte del ecosistema de CineMusic y se encarga de gestionar toda la lógica relacionada con álbumes y canciones del sistema. Está desarrollado usando FastAPI y sigue los principios de arquitectura hexagonal.

## 🛠️ Tecnologías Principales
- 🐍 Python
- 🚀 FastAPI
- 🔐 SQLAlchemy
- 📦 Pydantic
- 🐳 Docker
- 🗄️ MySQL
- 📋 Injector (Inyección de Dependencias)
- 🔐 Cryptography

## 📦 Estructura del Proyecto
```
microservice-album-song/
├── app/
│   ├── configuration/     # 🛠️ Configuración del servidor
│   │   ├── enviroments_config.py  # Configuración de variables de entorno
│   │   ├── milddware_cors.py      # Configuración de CORS
│   │   ├── swagger_config.py      # Configuración de Swagger
│   │   ├── routers_config.py      # Configuración de rutas
│   │   └── exceptions_handlers_global.py # Manejo global de excepciones
│   └── src/
│       ├── application/   # 📱 Lógica de aplicación
│       ├── domain/       # 📚 Dominio y modelos
│       │   ├── models/    # Modelos de dominio
│       │   └── persistence/ # Interfaces de persistencia
│       └── infrastructure/ # 🏗️ Infraestructura
│           └── outputs/
│               └── mysql/ # Implementación MySQL
│                   ├── entities/  # Entidades de base de datos
│                   └── repositories/ # Repositorios de datos
├── docker/              # 🐳 Configuración Docker
├── docker-compose.yml   # 📋 Orquestación de servicios
└── requirements.txt     # 📦 Dependencias
```
## 📚 Modelos

### Álbum
El modelo de álbum incluye los siguientes campos y características:

| Campo           | Tipo de Dato | Descripción | Requerido | Restricciones |
| -------------- | ------------ | ----------- | ----------- | ------------- |
| `id`           | `string`     | Identificador único del álbum | ✅ | UUID v4 |
| `title`        | `string`     | Título del álbum | ✅ | Máximo 50 caracteres |
| `description`  | `string`     | Descripción del álbum | ✅ | Máximo 255 caracteres |
| `dateCreated`  | `string`     | Fecha de creación | ✅ | Formato YYYY-MM-DD |
| `imgUrlCover`  | `string`     | URL de la imagen de portada | ✅ | Mínimo 10 caracteres, único |
| `songs`        | `list[Song]` | Lista de canciones | ✅ | Mínimo 1 canción |

### Canción
El modelo de canción incluye los siguientes campos y características:

| Campo          | Tipo de Dato | Descripción | Requerido | Restricciones |
| -------------- | ------------ | ----------- | ----------- | ------------- |
| `id`           | `string`     | Identificador único de la canción | ✅ | UUID v4 |
| `name`         | `string`     | Nombre de la canción | ✅ | Máximo 100 caracteres |
| `singer`       | `string`     | Nombre del cantante | ✅ | Máximo 100 caracteres |
| `duration`     | `int`        | Duración en segundos | ✅ | Mínimo 1 segundo |
| `gender`       | `list[str]`  | Lista de géneros musicales | ✅ | Mínimo 1 género |
| `albumId`      | `string`     | ID del álbum al que pertenece | ✅ | UUID v4 |
| `imgCoverUrl`  | `string`     | URL de la imagen de portada | ✅ | Mínimo 10 caracteres, único |
| `musicUrl`     | `string`     | URL del archivo de música | ✅ | Mínimo 10 caracteres, único |

## 🔄 Relación entre Álbum y Canción
Cada álbum puede contener múltiples canciones, y cada canción pertenece a un solo álbum. La relación se establece a través del campo `albumId` en el modelo de canción, que hace referencia al `id` del álbum correspondiente.

### Características de la Relación
- Un álbum puede tener múltiples canciones (relación uno a muchos)
- Cada canción debe pertenecer a un álbum (campo albumId requerido)
- Las canciones pueden ser actualizadas o eliminadas individualmente sin afectar al álbum
- La eliminación de un álbum eliminará todas sus canciones asociadas

## 🚀 Configuración y Ejecución

### 📝 Variables de Entorno
El microservicio utiliza las siguientes variables de entorno:

#### 🔧 Servidor
- `HOST`: Host del servidor (default: 0.0.0.0)
- `PORT`: Puerto del servidor (default: 2002)
- `DEBUG`: Modo debug (true/false)

#### 🗄️ Base de Datos
**Desarrollo**
- `DATABASE_URL_DEV`: URL de la base de datos en desarrollo

**Producción**
- `DATABASE_URL`: URL completa de la base de datos
- `MYSQL_DATABASE`: Nombre de la base de datos
- `MYSQL_USER`: Usuario de MySQL
- `MYSQL_PASSWORD`: Contraseña de MySQL
- `MYSQL_ROOT_PASSWORD`: Contraseña root de MySQL

#### 📡 CORS
- `ALLOW_ORIGINS`: Orígenes permitidos
- `ALLOW_CREDENTIALS`: Permite credenciales
- `ALLOW_METHODS`: Métodos HTTP permitidos
- `ALLOW_HEADERS`: Headers permitidos

#### 📚 Swagger
- `VERSION`: Versión de la API
- `TITLE`: Título de la documentación

### 🐳 Docker
Para ejecutar el servicio usando Docker:
```bash
# Construir y ejecutar los servicios
docker-compose up --build

# Detener los servicios
docker-compose down
```

### 📋 Requisitos
1. 🐳 Docker y Docker Compose instalados
2. 🐍 Python 3.8+
3. 📦 Dependencias del proyecto (ver requirements.txt)

## 🛠️ Desarrollo Local
Para ejecutar el servicio en modo desarrollo:
```bash
# Crear un entorno virtual
python -m venv env

# Activar el entorno en Linux y Mac
source env/bin/activate

# Activar el entorno en Windows
env\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar el servidor
python main.py
```

```python
# El archivo main.py está configurado para que arranque uvicorn en modo --reload
if __name__ == "__main__":
    os.system(f"uvicorn main:app --host {HOST} --port {PORT} --reload")
```

Recuerda tener presente que se necesita un archivo `.env` en la raíz del proyecto con las variables de entorno para que Docker pueda levantar el contenedor con dichas variables.

## 📚 Documentación API
La documentación de la API está disponible en:
- 🌐 Swagger UI: http://localhost:2002/docs
- 📄 Redoc: http://localhost:2002/redoc

## 🛡️ Seguridad
El microservicio implementa:
- 🔒 Encriptación de datos sensibles
- 🛡️ Manejo de errores global
- 📡 CORS configurado
- 🔐 Validación de datos con Pydantic

## 🚀 Características Principales
- 📱 Gestión completa de álbumes (CRUD)
- 🎵 Gestión de canciones por álbum
- 📦 Inyección de dependencias con Injector
- 📊 Manejo de errores
- 🔄 Contexto asíncrono
- 📡 Consultas por título o descripción
- 📅 Manejo de fechas y timestamps
- 🌐 Validación de URLs para imágenes
- 📚 Documentación Swagger completa