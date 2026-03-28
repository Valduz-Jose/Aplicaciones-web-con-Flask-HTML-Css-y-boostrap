# 🌐 Zona Fit Web - Gestión de Gimnasio con Flask

Este proyecto es una evolución del sistema **Zona Fit**, trasladando la lógica de gestión de clientes de una aplicación de escritorio a una **aplicación web dinámica**. Utiliza **Python** con el micro-framework **Flask**, integrando persistencia en **MySQL** y una interfaz moderna con **Bootstrap**.

## 🚀 Características Principales

* **Desarrollo Web con Flask:** Implementación de rutas dinámicas y manejo de peticiones HTTP (GET/POST).
* **Frontend Moderno:** Interfaz responsiva utilizando **Bootstrap 5** y temas oscuros para una mejor experiencia de usuario.
* **Formularios Seguros:** Uso de `Flask-WTF` para la creación de formularios y protección contra ataques **CSRF**.
* **Motor de Plantillas Jinja2:** Renderización dinámica de datos provenientes de la base de datos directamente en el HTML.
* **Arquitectura DAO:** Reutilización de la lógica de acceso a datos para mantener un código limpio y organizado.

## 🛠️ Tecnologías Utilizadas

* **Backend:** Python 3.x, Flask.
* **Frontend:** HTML5, CSS3, Bootstrap 5, Bootstrap Icons.
* **Base de Datos:** MySQL (con Pool de Conexiones).
* **Librerías Extra:** Flask-WTF, WTForms, mysql-connector-python.

## 📋 Estructura del Proyecto

* `app.py`: Servidor Flask y definición de rutas (Inicio, Guardar, Editar, Eliminar).
* `cliente_forma.py`: Definición de la estructura y validaciones del formulario web.
* `templates/index.html`: Plantilla principal con el dashboard y formulario dinámico.
* `cliente_dao.py` & `conexion.py`: Capas de persistencia y conexión a base de datos.

## 🔧 Configuración e Instalación

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/Valduz-Jose/Aplicaciones-web-con-Flask-HTML-Css-y-boostrap.git](https://github.com/Valduz-Jose/Aplicaciones-web-con-Flask-HTML-Css-y-boostrap.git)
    cd Aplicaciones-web-con-Flask-HTML-Css-y-boostrap
    ```

2.  **Configurar Base de Datos:**
    Asegúrate de tener creada la base de datos `zona_fit_db` y la tabla `cliente` (puedes usar el mismo script del proyecto de escritorio).

3.  **Instalar dependencias:**
    ```bash
    pip install flask flask-wtf mysql-connector-python
    ```

4.  **Ejecutar el servidor:**
    ```bash
    python app.py
    ```
    Luego abre en tu navegador: `http://localhost:5000`

---
Desarrollado con ❤️ por **Jose Valduz**.

<img width="930" height="536" alt="Captura de pantalla 2026-03-28 143932" src="https://github.com/user-attachments/assets/80fc2680-d43f-46ac-9210-955495854865" />
