from flask import Flask, Blueprint
from RedTeamReporter.models import db
from flask_jwt_extended import JWTManager

#from flask_login import LoginManager
from RedTeamReporter.config.flask_config import Config, ProdConfig, DevConfig
from RedTeamReporter.issue import issue
from RedTeamReporter.engagement import engagement, phase, asset
from RedTeamReporter.auth import auth


app = Flask(__name__)

if app.config['ENV'] == 'development':
    app.config.from_object(DevConfig)
elif app.config['ENV'] == 'production':
    app.config.from_object(ProdConfig)
else:
    app.config.from_object(Config)

db.app = app
db.init_app(app)

JWTManager(app)

app.register_blueprint(engagement)
app.register_blueprint(issue)
app.register_blueprint(auth)

#app.config['SECRET_KEY'] = 
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

#login_manager = LoginManager(app)
#login_manager.login_view = 'login'
#login_manager.login_message_category = 'info'

from RedTeamReporter import routes