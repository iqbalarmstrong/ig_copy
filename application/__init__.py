from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_session import Session
from flask_login import LoginManager
from dotenv import load_dotenv
from datetime import timedelta
import os

load_dotenv()

app = Flask(__name__, templete_folder='views')
app.config["SECRET_KEY"]=""
app.config["SQLACHEMY_DATABASES_URI"]=""
app.config["SQLACHEMY_TRACK_MODIFICATIONs"]= False
app.config["SESSION_TYPE"]= "filesystem"
app.config["SESSION_PERMANENT"] = False
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=30)

db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"

from application import routes
from application.models import*