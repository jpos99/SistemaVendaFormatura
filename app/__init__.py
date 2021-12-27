from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app_variable = Flask(__name__)
app_variable.config.from_object(Config)

db = SQLAlchemy(app_variable)
db.init_app(app_variable)
migrate = Migrate(app_variable, db)

login = LoginManager(app_variable)
login.login_view = 'login'
from app import routes, models
