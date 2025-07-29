Shopping Cart Helper 🛒🤖
Este proyecto es una prueba de concepto (PoC) que implementa un sistema de herramientas (tools) para ser consumido por Modelos de Lenguaje Grandes (LLMs) como Claude o ChatGPT. Permite a un LLM interactuar de forma segura y estructurada con una base de datos de un carrito de compras a través de una API.

Arquitectura del Proyecto
El sistema está diseñado con una arquitectura de microservicios dentro de un monorepo, separando las responsabilidades en dos componentes principales:

Backend API (shoppingCartAPI): Un servicio robusto construido con Django y Django Rest Framework. Se encarga de toda la lógica de negocio, la interacción con la base de datos y la gestión de los modelos de User, ShoppingCart y ShoppingCartItem.

Servidor MCP (shoppingCartMCP): Una interfaz liviana que expone las "herramientas" (tools) bajo el Model Context Protocol (MCP). Actúa como un gateway o fachada que los LLMs pueden consumir. Cuando un LLM quiere usar una herramienta, este servidor recibe la petición, llama al endpoint correspondiente de la Backend API para realizar la operación real, y le devuelve el resultado al LLM.

Tecnologías Utilizadas
Backend (shoppingCartAPI)
Python

Django: Framework principal para el desarrollo web.

Django Rest Framework (DRF): Para la construcción de la API REST.

Djongo: Conector para usar MongoDB con Django.

DRF Simple JWT: Para la autenticación basada en tokens (Login).

django-filter: Para facilitar la creación de filtros en los endpoints.

Servidor de Herramientas (shoppingCartMCP)
Python

Model Context Protocol (MCP) SDK: Para definir y exponer las herramientas a los LLMs.

Uvicorn: Servidor ASGI para ejecutar la aplicación de forma asíncrona.

General
Git: Para el control de versiones en formato de monorepo.

Entorno Virtual (venv): Para gestionar las dependencias de forma aislada.

Configuración e Instalación
Sigue estos pasos para poner en marcha el proyecto en un entorno local.

Clonar el repositorio

Bash

git clone <URL_DEL_REPOSITORIO>
Navegar al directorio del proyecto

Bash

cd shopping-cart-helper
Crear y activar el entorno virtual

Bash

# Crear el entorno
python -m venv .venv

# Activar en Windows (PowerShell)
.\.venv\Scripts\activate

# Activar en Windows (cmd)
.venv\Scripts\activate

# Activar en Mac/Linux
source .venv/bin/activate
Instalar las dependencias
Asegúrate de tener un archivo requirements.txt en la raíz con todas las librerías y ejecútalo.

Bash

pip install -r requirements.txt
Configurar variables de entorno
Creá un archivo .env en la raíz del proyecto para gestionar las variables sensibles, como la conexión a la base de datos.

Cómo Ejecutar
Debes iniciar ambos servicios, cada uno en su propia terminal.

1. Para ejecutar la API Backend (Django)
Bash

# Navegar a la carpeta del backend
cd shoppingCartAPI

# Aplicar las migraciones a la base de datos
python manage.py migrate

# Iniciar el servidor de desarrollo
python manage.py runserver
La API estará disponible en http://127.0.0.1:8000.

2. Para ejecutar el Servidor MCP
Bash

# Navegar a la carpeta del servidor MCP
cd shoppingCartMCP

# Iniciar el servidor con Uvicorn
uvicorn main:app --reload
El servidor de herramientas estará disponible (generalmente también en http://127.0.0.1:8000, asegúrate de cambiar el puerto si quieres correr ambos a la vez).

Roadmap Futuro
[ ] Implementar sistema de autenticación completo para proteger los endpoints.

[ ] Añadir la capacidad de compartir carritos entre usuarios.

[ ] Desarrollar un sistema de logging para monitorear las interacciones del LLM.

[ ] Expandir el número de herramientas disponibles.