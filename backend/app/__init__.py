from flask import Flask
from .global_config import Config

def register_extensions(app):
    from .extensions import cors

    cors.init_app(app)

def register_api(app):
    from .controllers import api_bp

    app.register_blueprint(api_bp)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_api(app)
    register_extensions(app)
    return app
