
from datetime import datetime
from . import db

class User(db.Model):
    id_user = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(128))
    email = db.Column(db.String(128))
    password = db.Column(db.String(128))
    status = db.Column(db.Integer)
    #TODO FOTO USER

    def __init__(self, username, password, email, status):
        self.username = username
        self.password = password
        self.email = email
        self.status = status


class Question(db.Model):
    id_question = db.Column(db.Integer, primary_key = True)
    id_user = db.Column(db.Integer)
    pertanyaan = db.Column(db.String(128))
    judul = db.Column(db.String(128))
    tgl_question = db.Column(db.DateTime(), default = datetime.utcnow, onupdate = datetime.utcnow)

    def __init__(self, id_user, pertanyaan, tgl_question, judul):
        self.id_user = id_user
        self.pertanyaan = pertanyaan
        self.tgl_question = tgl_question
        self.judul = judul






