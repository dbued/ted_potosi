from flask import Blueprint, render_template

web_bp = Blueprint('web', __name__)

@web_bp.route('/')
def index():
    return render_template('pages/index.html')

@web_bp.route('/pdf-viewer')
def pdf_viewer():
    return render_template('pages/pdf.html')

# Normativa
@web_bp.route('/normativa/resolucion')
def normativa_resolucion():
    return render_template('pages/normativa/resolucion.html')

@web_bp.route('/normativa/reglamentos')
def normativa_reglamentos():
    return render_template('pages/normativa/reglamentos.html')

@web_bp.route('/normativa/leyes')
def normativa_leyes():
    return render_template('pages/normativa/leyes.html')

# Capacitación
@web_bp.route('/capacitacion/guias')
def capacitacion_guias():
    return render_template('pages/capacitacion/guias.html')

@web_bp.route('/capacitacion/manuales')
def capacitacion_manuales():
    return render_template('pages/capacitacion/manuales.html')

@web_bp.route('/capacitacion/videos')
def capacitacion_videos():
    return render_template('pages/capacitacion/videos.html')

# Formularios
@web_bp.route('/formularios/rrhh')
def formularios_rrhh():
    return render_template('pages/formularios/rrhh.html')

@web_bp.route('/formularios/sistemas')
def formularios_sistemas():
    return render_template('pages/formularios/sistemas.html')

@web_bp.route('/formularios/otros')
def formularios_otros():
    return render_template('pages/formularios/otros.html')

# Social
@web_bp.route('/social/contactos')
def social_contactos():
    return render_template('pages/social/contactos.html')