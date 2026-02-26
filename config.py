import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave-secreta-para-desarrollo'
    # Si usas base de datos u otras configuraciones, agrégalas aquí