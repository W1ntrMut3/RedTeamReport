from datetime import timedelta

class Config(object):
	#used when none specified
	DEBUG=True
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
	SECRET_KEY = "testsecretkey123123123"
	JWT_SECRET_KEY='jwtsecretkey123'
	JWT_ACCESS_TOKEN_EXPIRES=timedelta(hours=10)
	JWT_REFRESH_TOKEN_EXPIRES=timedelta(days=30)
	
class ProdConfig(Config):
	pass

class DevConfig(Config):
	#to be used with dev
	DEBUG=False
	SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
	SECRET_KEY = "testsecretkey123123123"
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	JWT_SECRET_KEY='jwtsecretkey123'
	JWT_ACCESS_TOKEN_EXPIRES=timedelta(hours=10)
