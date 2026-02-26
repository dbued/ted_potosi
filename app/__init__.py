from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Registrar blueprints
    from app.routes.web import web_bp
    from app.routes.pdf import pdf_bp

    app.register_blueprint(web_bp)
    app.register_blueprint(pdf_bp, url_prefix='/pdf')

    return app