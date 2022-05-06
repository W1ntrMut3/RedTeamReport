from flask import Flask, Blueprint
from RedTeamReporter.models import db
from RedTeamReporter.auth import jwt

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
jwt.app = app
jwt.init_app(app)

app.register_blueprint(engagement)
app.register_blueprint(issue)
app.register_blueprint(auth)


from RedTeamReporter import routes