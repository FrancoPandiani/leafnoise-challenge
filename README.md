# Backend Challenge - Leafnoise

API REST desarrollada por **Franco Pandiani** en **Python 3.10** con **Flask** para la gestión de empleados en *People Flow*.  
Este proyecto ofrece una solución completa para el registro, consulta, actualización y eliminación de empleados.

---

## Cómo levantar el proyecto

### Local

**1. Clonar el repositorio**
```bash
git clone https://github.com/FrancoPandiani/leafnoise-challenge.git
cd backend-challenge-leafnoise-franco-pandiani
```

**2. Crear y activar el entorno virtual**

Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Instalar dependencias**
```bash
pip install -r requirements.txt
```

**4. Ejecutar la aplicación**
```bash
flask run
```

La API estará disponible en [http://127.0.0.1:5000]

---

### Docker

**Build y ejecución**
```bash
docker build -t people-flow-api .
docker run -p 5000:5000 people-flow-api
```

---

## Estructura del proyecto

```
backend-challenge-leafnoise-franco-pandiani/
├── models/              # Modelos de datos (Employee, User)
├── routes/              # Definición de endpoints por recurso
├── .flaskenv            # Variables de entorno Flask
├── .gitignore           # Archivos excluidos del repositorio
├── app.py               # Punto de entrada principal
├── db.py                # Configuración de SQLAlchemy
├── Dockerfile           # Configuración para containerización
├── README.md            # Documentación del proyecto
├── requirements.txt     # Dependencias del proyecto
└── schemas.py           # Validaciones con Marshmallow
```

---

## Decisiones técnicas

### Python 3.10
Elegí esta versión por su estabilidad y compatibilidad con las librerías utilizadas.

### Flask-Smorest
Opté por esta librería por su capacidad para acelerar el desarrollo gracias a la validación automática de datos y la serialización de respuestas.  
Integra **Marshmallow** de forma nativa, evitando código repetitivo y generando automáticamente la documentación **OpenAPI**, lo que asegura respuestas bien estructuradas.  
Aunque no está pensada para entornos productivos de gran escala, es ideal para un challenge completo y profesional.

### SQLAlchemy + SQLite
Elegí esta combinación por su simplicidad y portabilidad.  
SQLite permite ejecutar el proyecto sin dependencias externas, mientras que SQLAlchemy ofrece una capa ORM sólida, facilitando migraciones futuras a motores como PostgreSQL o MySQL.

### JWT Authentication
Implementé autenticación basada en tokens **JWT** para proteger los endpoints y aplicar buenas prácticas de seguridad en APIs REST.  
Los endpoints críticos (como la creación de empleados) requieren autenticación, mientras que otros como listar empleados, paginar o calcular salario promedio se dejaron abiertos para facilitar las pruebas durante el challenge.

### Docker
Utilicé containerización con **Docker** para garantizar que la aplicación se ejecute de forma consistente en cualquier entorno y simplificar el despliegue.
