from flask import Flask,render_template,request,flash,redirect,url_for
from . import app,db
from .models import *

@app.route('/home')
def home():
    question = Question.query.all()
    return render_template("question.html", questions = question)