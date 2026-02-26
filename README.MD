# TED Potosí - Portal de Anuncios y Documentos

Portal web institucional del **Tribunal Electoral Departamental de Potosí** desarrollado con Flask. Presenta un carrusel de anuncios en PDF, menú de navegación con subsecciones y una interfaz responsiva con los colores institucionales (azul, dorado y rojo).

---

## 📋 Características

- Estructura profesional escalable (patrón fábrica de aplicaciones).
- Menú lateral izquierdo con submenús: Normativa, Capacitación, Formularios, Sistemas y Social.
- Página de inicio con carrusel automático de anuncios en PDF (los archivos se cargan dinámicamente desde `static/assets/documentos/`).
- Visualización de PDF en iframe dentro del carrusel.
- Listado interactivo de todos los PDF disponibles.
- Diseño responsivo basado en **AdminLTE 3** y **Bootstrap 4**.
- Colores personalizados acordes a la identidad institucional.
- Fácil personalización y ampliable para nuevas secciones.

---

## 🛠 Tecnologías utilizadas

- **Backend:** Python 3, Flask 2.3
- **Frontend:** HTML5, CSS3, JavaScript, jQuery
- **Librerías y frameworks:** AdminLTE 3, Bootstrap 4, Font Awesome 5
- **Entorno virtual:** venv
- **Servidor de desarrollo:** Flask built-in

---

## 📁 Estructura del proyecto
```
ted_potosi/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   └── templates/
│       ├── base.html
│       ├── index.html
│       └── pdf.html
├── config.py
├── requirements.txt    
├── run.py
└── static/
    ├── assets/
    │   ├── documentos/ 
    │   ├── css/
    │   ├── js/
    │   └── img/
    └── fonts/
``` 
---## 🚀 Cómo ejecutar el proyecto

1. Clona el repositorio o descarga los archivos del proyecto.
2. Crea un entorno virtual:
   ```bash
   python -m venv venv
   ```
3. Activa el entorno virtual:
   - En Windows:
     ```bash
     venv\Scripts\activate
     ```
   - En Linux/macOS:
     ```bash
     source venv/bin/activate
     ```
4. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```
5. Ejecuta la aplicación:
   ```bash
   python run.py
   ```
6. Accede al sitio web desde tu navegador en `http://localhost:5000`.
---## 📂 Personalización
- Para agregar nuevos anuncios en PDF, simplemente coloca los archivos PDF en la carpeta `static/assets/documentos/`. El carrusel y el listado se actualizarán automáticamente.
- Para modificar los colores o el diseño, edita los archivos CSS en `static/assets/css/` o personaliza las plantillas HTML en `app/templates/`.

