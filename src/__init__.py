from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///automatadb.db'
app.config['SECRET_KEY'] = 'ef4c1adcbabd874ea94f6908'
app.config['UPLOAD_FOLDER'] = 'static/storage'

db = SQLAlchemy(app)

from src.routes import routes