from flask_restful import Api
from .service import Test
from flask import Flask
from settings import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

api = Api(app)
migrate = Migrate(app, db)

api.add_resource(Test, '/test/')