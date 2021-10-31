from flask import Blueprint
from flask_restx import Api

from .hello_world_controller import hello_world_controller
from .audio_controller import audio_controller

api_bp = Blueprint('api', __name__, url_prefix='/api')
api = Api(api_bp,
    title='Sonus API',
    version='1.0',
    validate=False
)
api.add_namespace(hello_world_controller)
api.add_namespace(audio_controller)