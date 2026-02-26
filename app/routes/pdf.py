from flask import Blueprint, send_file, abort, current_app
import os

pdf_bp = Blueprint('pdf', __name__)

@pdf_bp.route('/view/<filename>')
def view_pdf(filename):
    pdf_path = os.path.join(current_app.root_path, 'static', 'documentos', filename)
    if not os.path.exists(pdf_path):
        abort(404)
    return send_file(pdf_path, mimetype='application/pdf')

@pdf_bp.route('/download/<filename>')
def download_file(filename):
    file_path = os.path.join(current_app.root_path, 'static', 'documentos', filename)
    if not os.path.exists(file_path):
        abort(404)
    return send_file(file_path, as_attachment=True, download_name=filename)