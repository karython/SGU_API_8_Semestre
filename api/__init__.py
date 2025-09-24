from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv
import os

load_dotenv()

# instanciando o Flask e a Api
app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)
api = Api(app)



#TODO: Apontar os modelos (tabelas)
#      Apontar as Views