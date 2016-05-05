from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

#include from config.py
app.config.update(
    DEBUG = True,
    SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost/tcoverflow'
)
db = SQLAlchemy(app)

from . import models, views
