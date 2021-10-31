from flask_cors import CORS
from flask_mongoengine import MongoEngine

db = MongoEngine()
cors = CORS()
