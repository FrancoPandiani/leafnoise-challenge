# Backend Challenge Leafnoise
API REST desarrollada por Franco Pandiani en Pyton 3.10 con Flask para la gestión de empleados en PeopleFlow.
Este proyecto proporciona una solución completa para el registro, consulta, actualización y eliminación
de empleados.
---

## 🚀 Cómo levantar el proyecto

### Local

1️⃣ Clonar el repositorio:
git clone https://github.com/FrancoPandiani/leafnoise-challenge.git
cd backend-challenge-leafnoise-franco-pandiani

2️⃣ Crear y activar el entorno virtual:
#### Windows:
python -m venv venv
venv\Scripts\activate

#### Linux / macOS:
python3 -m venv venv
source venv/bin/activate

3️⃣ Instalar dependencias:
pip install -r requirements.txt

4️⃣Ejecutar la app:
flask run

### DOCKER
docker build -t people-flow-api .
docker run -p 5000:5000 people-flow-api

---

## 📂 Estructura rápida del repo
backend-challenge-leafnoise-franco-pandiani

├── models/              # Modelos de datos (Employee, User)
├── routes/              # Definición de endpoints por recurso
├── .flaskenv            # Variables de entorno Flask
├── .gitignore           # Archivos excluidos del repositorio
├── app.py               # Punto de entrada de la app
├── db.py                # Configuración de SQLAlchemy
├── Dockerfile           # Configuración para containerización
├── README.md            # Documentación del proyecto
├── requirements.txt     # Dependencias del proyecto
└── schemas.py           # Esquemas de validación con Marshmallow
---

## 💡 Notas

### Decisiones técnicas:

Python 3.10: Elegí esta versión por su estabilidad.

Flask-Smorest: Elegí esta librería por su capacidad de acelerar el desarrollo gracias a la validación automática de datos de entrada y la serialización de las respuestas. Al integrar Marshmallow de forma nativa, evita la escritura de código repetitivo para validar requests y transformar objetos a JSON. Además, genera documentación OpenAPI de manera automática, lo que no solo reduce tiempos de desarrollo, sino que también garantiza que las respuestas de la API estén siempre correctamente estructuradas. Si bien no está pensada para entornos de producción de gran escala, resulta ideal para completar un challenge de manera ordenada y profesional.

SQLAlchemy + SQLite: Esta combinación la elegí por su simplicidad en la configuración inicial y portabilidad. SQLite permite levantar el proyecto sin dependencias externas, mientras que SQLAlchemy como ORM proporciona una abstracción robusta que facilita migraciones futuros motores como PostgreSQL o MySQL si el proyecto escala. Esta elección me permitió concentrarme en cumplir con todos los requerimientos funcionales del challenge de manera eficiente.

JWT Authentication: Implemente un sistema de autenticación basado en tokens JWT para proteger los endpoints y aplicar buenas prácticas de seguridad en APIs REST. Los endpoints más sensibles, como la creación de empleados, requieren autenticación para garantizar un acceso controlado. En cambio, otros endpoints como listar empleados por puesto / paginar resultados o calcular el salario promedio se dejaron accesibles sin token, con el objetivo de facilitar las pruebas durante el challenge.

Docker: Utilice containerización para facilitar el despliegue y garantizar que la aplicación funcione consistentemente en cualquier entorno.
---

