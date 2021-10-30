from flask import Flask

def register_extensions(app):
    from .extensions import cors

    cors.init_app(app)

def register_api(app):
    from .controllers import api_bp

    app.register_blueprint(api_bp)

def create_app():
    app = Flask(__name__)
    register_api(app)
    register_extensions(app)
    return app
