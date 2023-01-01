from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'asdsadsae134312321faw!@#@!DFas'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://dev_user:dev_password@localhost/dev_db?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['PAGE_SIZE'] = 8

db = SQLAlchemy(app=app)