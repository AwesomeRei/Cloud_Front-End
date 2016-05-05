<<<<<<< HEAD
from flask import Flask, session, redirect, url_for, escape, request, render_template, jsonify
from hashlib import md5
from base64 import b64encode
import MySQLdb

app = Flask(__name__)

db = MySQLdb.connect(host="localhost", user="root", passwd="", db="tcoverflow")
cur = db.cursor()

@app.route('/')
def index():
    print index
    if 'username' in session:
        return redirect(url_for('user'))
    cur.execute("SELECT * FROM question ORDER BY id_question DESC LIMIT 10")
    passingData = []
    passingData.append(cur.fetchall())
    passingData.append('data')
    return render_template('index.html', data=passingData)

@app.route('/signup/login', methods=['GET', 'POST'])
def login():
    print login
    error = None
    if 'username' in session:
        return redirect(url_for('index'))
    if request.method == 'POST':
        username_form  = request.form['username']
        password_form  = request.form['password']
        cur.execute("SELECT COUNT(1) FROM users WHERE username = %s;", [username_form]) # CHECKS IF USERNAME EXSIST
        if cur.fetchone()[0]:
            cur.execute("SELECT password FROM users WHERE username = %s;", [username_form]) # FETCH THE HASHED PASSWORD
            for row in cur.fetchall():
                if password_form == row[0]:
                    session['username'] = request.form['username']
                    return redirect(url_for('user'))
                else:
                    error = "Salah password!"
        else:
            error = "Anda belum terdaftar!"
    return render_template('sign_up.html', error=error)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    print signup
    error = None
    if 'username' in session:
        return redirect(url_for('index'))
    if request.method == 'POST':
        username_form  = request.form['username']
        password_form  = request.form['password']
        cur.execute("SELECT COUNT(1) FROM users WHERE username = %s;", [username_form]) # CHECKS IF USERNAME EXSIST
        if cur.fetchone()[0]:
            error = "Username sudah digunakan!"
        else:
            cur.execute("INSERT INTO users(username, password) VALUES(%s ,%s)", ([username_form],[password_form]))
            db.commit()
            error = "Berhasil Daftar!"
            
    return render_template('sign_up.html', error=error)

@app.route('/user', methods=['GET', 'POST'])
def user():
    if 'username' in session:
        username_session = session['username']
        return render_template('user.html', session_user_name=username_session)
    return redirect(url_for('index'))

@app.route('/user/<id>', methods=['GET', 'POST'])
def user_byid(id):
    if 'username' in session:
        cur.execute("SELECT * FROM users where username = %s",[id])
        passingData = []
        passingData.append(cur.fetchall())
        passingData.append('data')
        return render_template('profil.html', data=passingData)
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

#app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.secret_key = 'awankinton123'

if __name__ == '__main__':
    app.run(debug=True)