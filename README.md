## 🛒🤖 Shopping Cart Helper · PoC
Shopping Cart Helper es una prueba de concepto (PoC) que implementa un sistema de herramientas (tools) diseñadas para ser utilizadas por Modelos de Lenguaje Grandes (LLMs) como ChatGPT o Claude.
Permite a los LLMs interactuar de manera segura, estructurada y controlada con una base de datos de un carrito de compras, a través de una API.

### 🧠 Arquitectura del Proyecto
El sistema sigue una arquitectura de microservicios dentro de un monorepo, separando las responsabilidades en dos componentes principales:

### 🔧 1. Backend API (shoppingCartAPI)
Servicio robusto desarrollado con Django y Django Rest Framework. Se encarga de:

Lógica de negocio

Conexión con la base de datos

Modelos de usuario, carrito y productos

### 🌐 2. Servidor MCP (shoppingCartMCP)
Interfaz liviana que expone las herramientas compatibles con el Model Context Protocol (MCP).
Actúa como un gateway/fachada para que los LLMs accedan de forma controlada a las funciones del sistema.

## 🛠️ Tecnologías Utilizadas
### 📦 Backend (shoppingCartAPI)
- Python
- Django: Framework web principal
- Django Rest Framework (DRF): Construcción de APIs REST
- Djongo: Conector MongoDB para Django
- DRF Simple JWT: Autenticación basada en tokens
- django-filter: Filtros personalizados en endpoints

### 🌐 Servidor MCP (shoppingCartMCP)
- Python
- Model Context Protocol (MCP) SDK: Exposición de herramientas a LLMs

### ⚙️ General
- Git: Control de versiones en formato monorepo
- venv: Entornos virtuales aislados

 
