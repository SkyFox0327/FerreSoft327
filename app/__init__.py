from flask import Flask
from app.routes.login_routes import login_bp
from app.routes.inicio_routes import inicio_bp
from app.routes.inventario_routes import inventario_bp

def create_app():
    app = Flask(__name__)
    app.secret_key = "clave_secreta"

    app.register_blueprint(login_bp)
    app.register_blueprint(inicio_bp)
    app.register_blueprint(inventario_bp)
    
    return app

