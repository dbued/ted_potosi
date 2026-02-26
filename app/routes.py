import os
from flask import render_template, send_from_directory, current_app

def init_app(app):

    @app.route('/')
    def index():
        # Obtener lista de PDFs desde static/assets/
        pdf_folder = os.path.join(app.static_folder, 'assets', 'documentos')
        pdf_files = []
        if os.path.exists(pdf_folder):
            pdf_files = [f for f in os.listdir(pdf_folder) if f.lower().endswith('.pdf')]
            pdf_files.sort()
        return render_template('index.html', pdfs=pdf_files)

    # ---------- Normativa ----------
    @app.route('/normativa/resolucion')
    def normativa_resolucion():
        return render_template('secciones/normativa_resolucion.html', titulo='Resoluciones')

    @app.route('/normativa/reglamentos')
    def normativa_reglamentos():
        return render_template('secciones/normativa_reglamentos.html', titulo='Reglamentos')

    @app.route('/normativa/leyes')
    def normativa_leyes():
        return render_template('secciones/normativa_leyes.html', titulo='Leyes')

    # ---------- Capacitación ----------
    @app.route('/capacitacion/guias')
    def capacitacion_guias():
        return render_template('secciones/capacitacion_guias.html', titulo='Guías')

    @app.route('/capacitacion/manuales')
    def capacitacion_manuales():
        return render_template('secciones/capacitacion_manuales.html', titulo='Manuales')

    @app.route('/capacitacion/video-tutoriales')
    def capacitacion_video():
        return render_template('secciones/capacitacion_video.html', titulo='Video Tutoriales')

    # ---------- Formularios ----------
    @app.route('/formularios/rrhh')
    def formularios_rrhh():
        return render_template('secciones/formularios_rrhh.html', titulo='RRHH')

    @app.route('/formularios/sistemas')
    def formularios_sistemas():
        return render_template('secciones/formularios_sistemas.html', titulo='Sistemas')

    @app.route('/formularios/otros')
    def formularios_otros():
        return render_template('secciones/formularios_otros.html', titulo='Otros')

    # ---------- Sistemas ----------
    @app.route('/sistemas/trans')
    def sistemas_trans():
        return render_template('secciones/sistemas_trans.html', titulo='Transporte')

    @app.route('/sistemas/exce')
    def sistemas_exce():
        return render_template('secciones/sistemas_exce.html', titulo='Excel')

    # ---------- Social ----------
    @app.route('/social/contactos')
    def social_contactos():
        return render_template('secciones/social_contactos.html', titulo='Contactos')

    # Ruta para servir PDFs (opcional, ya se sirven desde static)
    @app.route('/assets/<path:filename>')
    def serve_asset(filename):
        return send_from_directory(os.path.join(app.static_folder, 'assets'), filename)