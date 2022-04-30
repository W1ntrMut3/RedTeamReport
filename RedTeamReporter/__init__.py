from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
#from flask_login import LoginManager
from RedTeamReporter.config.flask_config import Config, ProdConfig, DevConfig
from RedTeamReporter.issue import issue
from RedTeamReporter.engagement import engagement, phase, asset
from RedTeamReporter.auth import auth
#from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with

app = Flask(__name__)

if app.config['ENV'] == 'development':
    app.config.from_object(DevConfig)
elif app.config['ENV'] == 'production':
    app.config.from_object(ProdConfig)
else:
    app.config.from_object(Config)

app.register_blueprint(engagement)
app.register_blueprint(issue)
app.register_blueprint(auth)

#app.config['SECRET_KEY'] = 
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
#login_manager = LoginManager(app)
#login_manager.login_view = 'login'
#login_manager.login_message_category = 'info'

from RedTeamReporter import routes