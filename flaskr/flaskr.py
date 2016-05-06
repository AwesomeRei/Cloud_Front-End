from flask import Flask, send_from_directory, session, redirect, url_for, escape, request, render_template, jsonify
from hashlib import md5
from base64 import b64encode
import MySQLdb
from werkzeug import secure_filename
import os

app = Flask(__name__)

# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = 'static/foto/'
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

db = MySQLdb.connect(host="localhost", user="root", passwd="", db="tcoverflow")
cur = db.cursor()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    error = None
    print index
    if 'username' in session:
        return redirect(url_for('user'))
    cur.execute("SELECT q.id_question, q.id_user, q.pertanyaan, q.judul, q.tgl_question, t.C_tags, t.CPP_tags, t.CSharp_tags, t.HTML_tags, t.PHP_tags, t.JS_tags, t.Py_tags, t.VB_tags, t.Bash_tags, t.Java_tags, t.Android_tags, t.Unity_tags \
                FROM question q, tags t where q.id_question=t.id_question ORDER BY q.id_question DESC LIMIT 10")
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
        cur.execute("SELECT COUNT(1) FROM user WHERE username = %s;", [username_form]) # CHECKS IF USERNAME EXSIST
        if cur.fetchone()[0]:
            cur.execute("SELECT password FROM user WHERE username = %s;", [username_form]) # FETCH THE HASHED PASSWORD
            for row in cur.fetchall():
                if password_form == row[0]:
                    session['username'] = request.form['username']
                    return redirect(url_for('user'))
                else:
                    error = "Salah password!"
        else:
            error = "Anda belum terdaftar!"
    return render_template('sign_up.html', error=error)

@app.route('/signup/daftar', methods=['GET', 'POST'])
def daftar():
    print signup
    error = None
    if 'username' in session:
        return redirect(url_for('index'))
    if request.method == 'POST':
        username_form  = request.form['username']
        email_form = request.form['email']
        password_form  = request.form['password']
        password2_form = request.form['password2']
        status_form = request.form['status']
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            uploaded_file(filename)
        files = str(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        cur.execute("SELECT COUNT(1) FROM user WHERE username = %s;", [username_form]) # CHECKS IF USERNAME EXSIST
        if cur.fetchone()[0]:
            error = "Username sudah digunakan!"
        elif password_form != password2_form:
            error = "Password yang Anda masukkan tidak sama"
        else:
            cur.execute("SELECT COUNT(1) FROM user WHERE email = %s;", [email_form]) # CHECKS IF email EXSIST
            if cur.fetchone()[0]:
                error = "Email sudah digunakan!"
            else:
                cur.execute("INSERT INTO user(username, email, password, status, foto_user) VALUES(%s ,%s, %s, %s, %s)",
                            ([username_form], [email_form],[password_form], [status_form], [files]))
                db.commit()
                error = "Berhasil Daftar!"
            
    return render_template('sign_up.html', error=error)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    print signup
    error = None
    if 'username' in session:
        return redirect(url_for('index'))
            
    return render_template('sign_up.html', error=error)

@app.route('/anon_post', methods=['GET', 'POST'])
def anon_post():
    print signup
    if 'username' in session:
        return redirect(url_for('index'))
    if request.method == 'POST':
        judul_form  = request.form['judul']
        pertanyaan_form = request.form['pertanyaan']
        id_user = 0
        cur.execute("INSERT INTO question(id_user, judul, pertanyaan) VALUES(%s ,%s, %s)", ([id_user], [judul_form], [pertanyaan_form]))
        db.commit()
        
        cur.execute("SELECT id_question FROM question ORDER BY id_question DESC LIMIT 1")
        id_question = cur.fetchone()[0]
        print 1
        c  = request.form['C_tags']
        cpp  = request.form['C++_tags']
        csharp  = request.form['C#_tags']
        html  = request.form['HTML_tags']
        php  = request.form['PHP_tags']
        js  = request.form['JS_tags']
        py  = request.form['Py_tags']
        vb  = request.form['VB_tags']
        bash  = request.form['Bash_tags']
        java  = request.form['Java_tags']
        android  = request.form['Android_tags']
        unity  = request.form['Unity_tags']
        cur.execute("INSERT INTO tags(C_tags, CPP_tags, CSharp_tags, HTML_tags, PHP_tags, JS_tags, Py_tags, VB_tags, Bash_tags, Java_tags, Android_tags, Unity_tags, id_question) \
                    VALUES(%s ,%s, %s, %s ,%s, %s, %s ,%s, %s, %s ,%s, %s, %s)",
                    ([c], [cpp], [csharp], [html], [php], [js], [py], [vb], [bash], [java], [android], [unity], [id_question]))
        db.commit()
           
    return redirect(url_for('index'))

def uploaded_file(filename):
    send_from_directory(app.config['UPLOAD_FOLDER'],filename)

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

@app.route('/question/<id>', methods=['GET','POST'])
def question(id):
    if request.method == 'GET' :
        cur.execute("select question.*, user.username from question, user where id_question= %s and user.id_user = question.id_user", [id])
        pertanyaan = cur.fetchone()
        cur.execute("select jawaban.*, user.username from jawaban, user where id_soal= %s and user.id_user = jawaban.id_user order by rating_jawaban desc",[id] )
        jawaban = cur.fetchall()
        data = []
        data.append(pertanyaan)
        data.append(jawaban)
        if(data):
            return render_template('question.html', data=data)

#app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.secret_key = 'awankinton123'

if __name__ == '__main__':
    app.run(debug=True)
