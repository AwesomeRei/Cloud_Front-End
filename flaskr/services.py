from flask import Flask, send_from_directory, session, redirect, url_for, escape, request, render_template, jsonify
from hashlib import md5
from base64 import b64encode
import requests
import MySQLdb
from werkzeug import secure_filename
import os
from pprint import pprint

app = Flask(__name__)

DBHOST = '10.151.34.15'
DBUSER = 'cloud'
DBPASSWD = ''
DBNAME = 'tcoverflow'
IMAGEUPLOADPATH = 'http://10.151.34.30:5001/'
GETIMAGEPATH = 'http://10.151.34.30:5001/static/foto/'

WEBHOST = '10.151.43.140'
WEBPORT = 5000

# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = 'static/foto/'
app.config['PATH'] = 'foto/'
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'PNG', 'JPG', 'JPEG', 'GIF'])

db = MySQLdb.connect(host=DBHOST, user=DBUSER, passwd=DBPASSWD, db=DBNAME)
cur = db.cursor()


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/static/foto/<filename>', methods=['GET'])
def getImg(foto):
    return GETIMAGEPATH + filename

@app.route('/')
def index():
    error = None
    if 'username' in session:
        cur.execute("SELECT status FROM user WHERE username = %s", [session['username']])
        if cur.fetchone()[0] == 1:
            return redirect(url_for('user_premium'))
        else:
            return redirect(url_for('user_free'))

    cur.execute("SELECT temp.*, (SELECT COUNT(j.id_question) FROM jawaban j WHERE j.id_question = temp.id_question) \
                FROM (SELECT q.id_question, q.id_user, q.pertanyaan, q.judul, q.tgl_question, t.C_tags, t.CPP_tags, \
                t.CSharp_tags, t.HTML_tags, t.PHP_tags, t.JS_tags, t.Py_tags, t.VB_tags, t.Bash_tags, t.Java_tags, \
                t.Android_tags, t.Unity_tags \
                FROM question q, tags t WHERE q.id_question=t.id_question \
                ORDER BY q.tgl_question DESC LIMIT 5) AS temp")
    passingData = []
    passingData.append(cur.fetchall())
    passingData.append('data')
    return render_template('index.html', data=passingData)

@app.route('/signup/login', methods=['GET', 'POST'])
def login():
    error = None
    if 'username' in session:
        return redirect(url_for('index'))
    if request.method == 'POST':
        username_form  = request.form['username']
        password_form  = request.form['password']
        cur.execute("SELECT COUNT(1) FROM user WHERE username = %s;", [username_form]) # CHECKS IF USERNAME EXSIST
        if cur.fetchone()[0]:
            cur.execute("SELECT password, id_user FROM user WHERE username = %s;", [username_form]) # FETCH THE HASHED PASSWORD
            for row in cur.fetchall():
                if password_form == row[0]:
                    session['username'] = request.form['username']
                    return redirect(url_for('index'))
                else:
                    error = "Salah password!"
        else:
            error = "Anda belum terdaftar!"
    return render_template('sign_up.html', error=error)

@app.route('/daftar', methods=['GET', 'POST'])
def daftar():
    error = None
    if 'username' in session:
        return redirect(url_for('index'))
    if request.method == 'POST':
        username_form  = request.form['username']
        email_form = request.form['email']
        password_form  = request.form['password']
        password2_form = request.form['password2']
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            fileSave = {  'image' : open(os.path.join(app.config['UPLOAD_FOLDER'], filename),'rb'), 'filename' : filename }
            r = requests.post(IMAGEUPLOADPATH,files=fileSave)
            #uploaded_file(filename)
        files = str(os.path.join(app.config['PATH'], secure_filename(file.filename)))

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
                cur.execute("INSERT INTO user(username, email, password, foto_user) VALUES(%s ,%s, %s, %s)",
                            ([username_form], [email_form],[password_form], [status_form], [files]))
                db.commit()
                error = "Berhasil Daftar!"

    return render_template('sign_up.html', error=error)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = None
    if 'username' in session:
        return redirect(url_for('index'))

    return render_template('sign_up.html', error=error)

@app.route('/anon_post', methods=['GET', 'POST'])
def anon_post():
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

@app.route('/free_list', methods=['GET', 'POST'])
def free_list():
    if 'username' not in session:
        return redirect(url_for('index'))
    if request.method == 'GET' :
        """
        cur.execute("SELECT q.id_question, q.id_user, q.pertanyaan, q.judul, q.tgl_question, t.C_tags, t.CPP_tags, t.CSharp_tags, t.HTML_tags, t.PHP_tags, t.JS_tags, t.Py_tags, t.VB_tags, t.Bash_tags, t.Java_tags, t.Android_tags, t.Unity_tags \
                    FROM question q, tags t where q.id_question=t.id_question ORDER BY q.tgl_question DESC")
                    """
        cur.execute("SELECT temp.*, (SELECT COUNT(j.id_question) FROM jawaban j WHERE j.id_question = temp.id_question) \
                    FROM (SELECT q.id_question, q.id_user, q.pertanyaan, q.judul, q.tgl_question, t.C_tags, t.CPP_tags, \
                    t.CSharp_tags, t.HTML_tags, t.PHP_tags, t.JS_tags, t.Py_tags, t.VB_tags, t.Bash_tags, t.Java_tags, \
                    t.Android_tags, t.Unity_tags \
                    FROM question q, tags t WHERE q.id_question=t.id_question \
                    ORDER BY q.tgl_question DESC) AS temp")
        passingData = []
        passingData.append(cur.fetchall())
        passingData.append('data')
        return render_template('free_list.html', data=passingData)

@app.route('/premium_list', methods=['GET', 'POST'])
def premium_list():
    if 'username' not in session:
        return redirect(url_for('index'))
    if request.method == 'GET' :
        """
        cur.execute("SELECT q.id_question, q.id_user, q.pertanyaan, q.judul, q.tgl_question, t.C_tags, t.CPP_tags, t.CSharp_tags, t.HTML_tags, t.PHP_tags, t.JS_tags, t.Py_tags, t.VB_tags, t.Bash_tags, t.Java_tags, t.Android_tags, t.Unity_tags \
                    FROM question q, tags t where q.id_question=t.id_question ORDER BY q.tgl_question DESC")
                    """
        cur.execute("SELECT temp.*, (SELECT COUNT(j.id_question) FROM jawaban j WHERE j.id_question = temp.id_question) \
                    FROM (SELECT q.id_question, q.id_user, q.pertanyaan, q.judul, q.tgl_question, t.C_tags, t.CPP_tags, \
                    t.CSharp_tags, t.HTML_tags, t.PHP_tags, t.JS_tags, t.Py_tags, t.VB_tags, t.Bash_tags, t.Java_tags, \
                    t.Android_tags, t.Unity_tags \
                    FROM question q, tags t WHERE q.id_question=t.id_question \
                    ORDER BY q.tgl_question DESC) AS temp")
        passingData = []
        passingData.append(cur.fetchall())
        passingData.append('data')
        return render_template('premium_list.html', data=passingData)

@app.route('/anon_answer/<id>', methods=['GET', 'POST'])
def anon_answer(id):
    if 'username' in session:
        return redirect(url_for('index'))
    if request.method == 'POST':
        isi_jawaban = request.form['isi_jawaban']
        cur.execute("INSERT INTO jawaban(id_question, isi_jawaban, id_user) VALUES(%s, %s, 0)", ([id], [isi_jawaban]))
        db.commit()
        return redirect(url_for('question', id=id))

@app.route('/free_answer/<id>', methods=['GET', 'POST'])
def free_answer(id):
    if 'username' not in session:
        return redirect(url_for('index'))
    if request.method == 'POST':
        isi_jawaban = request.form['isi_jawaban']
        cur.execute("SELECT id_user FROM user WHERE username = %s", [session['username']])
        id_user = str(cur.fetchone()[0])
        cur.execute("INSERT INTO jawaban(id_question, isi_jawaban, id_user) VALUES(%s, %s, %s)", ([id], [isi_jawaban], [id_user]))
        db.commit()
        return redirect(url_for('free_question', id=id))

@app.route('/premium_answer/<id>', methods=['GET', 'POST'])
def premium_answer(id):
    if 'username' not in session:
        return redirect(url_for('index'))
    if request.method == 'POST':
        isi_jawaban = request.form['isi_jawaban']
        cur.execute("SELECT id_user FROM user WHERE username = %s", [session['username']])
        id_user = str(cur.fetchone()[0])
        cur.execute("INSERT INTO jawaban(id_question, isi_jawaban, id_user) VALUES(%s, %s, %s)", ([id], [isi_jawaban], [id_user]))
        db.commit()
        return redirect(url_for('premium_question', id=id))

@app.route('/ask_free', methods=['GET', 'POST'])
def ask_free():
    error = None
    if 'username' not in session:
        return redirect(url_for('index'))
    if request.method == 'POST':
        cur.execute("SELECT id_user FROM user WHERE username = %s", [session['username']])
        id_user = str(cur.fetchone()[0])
        cur.execute("SELECT TIMESTAMPDIFF(DAY, (SELECT tgl_question FROM question WHERE id_user = " + id_user + " ORDER BY tgl_question DESC LIMIT 1), CURRENT_TIMESTAMP())")
        temp = cur.fetchone()[0]
        if ( temp >= 1 or temp is None):
            judul_form  = request.form['judul']
            pertanyaan_form = request.form['pertanyaan']
            cur.execute("INSERT INTO question(id_user, judul, pertanyaan) VALUES(%s ,%s, %s)", ([id_user], [judul_form], [pertanyaan_form]))
            db.commit()

            cur.execute("SELECT id_question FROM question ORDER BY id_question DESC LIMIT 1")
            id_question = str(cur.fetchone()[0])
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
            error = "Pertanyaan Anda berhasil dimasukkan!"
        else:
            error = "Free User hanya dapat bertanya sekali sehari!"

        cur.execute("SELECT id_user, username, email, status, foto_user, \
                    (SELECT COUNT(id_jawaban) FROM jawaban WHERE id_user =  " + id_user + "), \
                    (SELECT COUNT(id_question) FROM question WHERE id_user =  " + id_user + ") \
                    FROM user \
                    WHERE id_user = " + id_user)
        profil = cur.fetchone()
        """
        cur.execute("SELECT q.id_question, q.id_user, q.pertanyaan, q.judul, q.tgl_question, t.C_tags, \
                    t.CPP_tags, t.CSharp_tags, t.HTML_tags, t.PHP_tags, t.JS_tags, t.Py_tags, t.VB_tags, \
                    t.Bash_tags, t.Java_tags, t.Android_tags, t.Unity_tags \
                    FROM question q, tags t where q.id_question=t.id_question AND q.id_user = %s ORDER BY q.tgl_question DESC", [id_user])
                    """
        cur.execute("SELECT temp.*, (SELECT COUNT(j.id_question) FROM jawaban j WHERE j.id_question = temp.id_question) \
                    FROM (SELECT q.id_question, q.id_user, q.pertanyaan, q.judul, q.tgl_question, t.C_tags, \
                    t.CPP_tags, t.CSharp_tags, t.HTML_tags, t.PHP_tags, t.JS_tags, t.Py_tags, t.VB_tags, \
                    t.Bash_tags, t.Java_tags, t.Android_tags, t.Unity_tags \
                    FROM question q, tags t where q.id_question=t.id_question AND q.id_user =  " + id_user + " ORDER BY q.tgl_question DESC) AS temp")
        question = cur.fetchall()
        data = []
        data.append(error)
        data.append(profil)
        data.append(question)
        return render_template('dashboard_free.html', data=data)

    return redirect(url_for('index'))

@app.route('/ask_premium', methods=['GET', 'POST'])
def ask_premium():
    error = None
    if 'username' not in session:
        return redirect(url_for('index'))
    if request.method == 'POST':
        cur.execute("SELECT id_user FROM user WHERE username = %s", [session['username']])
        id_user = str(cur.fetchone()[0])

        file = request.files['file']
        judul_form  = request.form['judul']
        pertanyaan_form = request.form['pertanyaan']
        files = str(os.path.join(app.config['PATH'], secure_filename(file.filename)))

        if secure_filename(file.filename) :
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

                fileSave = {  'image' : open(os.path.join(app.config['UPLOAD_FOLDER'], filename),'rb'), 'filename' : filename }
                r = requests.post(IMAGEUPLOADPATH,files=fileSave)
                #uploaded_file(filename)
            cur.execute("INSERT INTO question(id_user, judul, pertanyaan, gambar) VALUES(%s ,%s, %s, %s)", \
                        ([id_user], [judul_form], [pertanyaan_form],[files]))
        else:
            cur.execute("INSERT INTO question(id_user, judul, pertanyaan) VALUES(%s ,%s, %s)", \
                        ([id_user], [judul_form], [pertanyaan_form]))
        db.commit()

        cur.execute("SELECT id_question FROM question ORDER BY id_question DESC LIMIT 1")
        id_question = str(cur.fetchone()[0])
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
        error = "Pertanyaan Anda berhasil dimasukkan!"

        cur.execute("SELECT id_user, username, email, status, foto_user, \
                    (SELECT COUNT(id_jawaban) FROM jawaban WHERE id_user = "+ id_user+"), \
                    (SELECT COUNT(id_question) FROM question WHERE id_user = "+ id_user+") \
                    FROM user WHERE id_user = " +  id_user)
        profil = cur.fetchone()
        cur.execute("SELECT temp.*, (SELECT COUNT(j.id_question) FROM jawaban j WHERE j.id_question = temp.id_question) \
                    FROM (SELECT q.id_question, q.id_user, q.pertanyaan, q.judul, q.tgl_question, t.C_tags, \
                    t.CPP_tags, t.CSharp_tags, t.HTML_tags, t.PHP_tags, t.JS_tags, t.Py_tags, t.VB_tags, \
                    t.Bash_tags, t.Java_tags, t.Android_tags, t.Unity_tags \
                    FROM question q, tags t where q.id_question=t.id_question AND q.id_user = "+id_user+" ORDER BY q.tgl_question DESC) AS temp")
        question = cur.fetchall()
        data = []
        data.append(error)
        data.append(profil)
        data.append(question)
        data.append(GETIMAGEPATH)
        return render_template('dashboard_premium.html', data=data)

    return redirect(url_for('index'))

def uploaded_file(filename):
    send_from_directory(app.config['UPLOAD_FOLDER'],filename)



@app.route('/user_free', methods=['GET', 'POST'])
def user_free():
    error = None
    if 'username' in session:
        cur.execute("SELECT id_user FROM user WHERE username = %s", [session['username']])
        id_user = str(cur.fetchone()[0])
        cur.execute("SELECT id_user, username, email, status, foto_user, (SELECT COUNT(id_jawaban) FROM jawaban WHERE id_user =" + id_user +") , (SELECT COUNT(id_question) FROM question WHERE id_user = " + id_user +") FROM user WHERE id_user = " + id_user)
        profil = cur.fetchone()
        """
        cur.execute("SELECT q.id_question, q.id_user, q.pertanyaan, q.judul, q.tgl_question, t.C_tags, \
                    t.CPP_tags, t.CSharp_tags, t.HTML_tags, t.PHP_tags, t.JS_tags, t.Py_tags, t.VB_tags, \
                    t.Bash_tags, t.Java_tags, t.Android_tags, t.Unity_tags \
                    FROM question q, tags t where q.id_question=t.id_question AND q.id_user = %s ORDER BY q.tgl_question DESC", [id_user])
                    """
        cur.execute("SELECT temp.*, (SELECT COUNT(j.id_question) FROM jawaban j WHERE j.id_question = temp.id_question) FROM (SELECT q.id_question, q.id_user, q.pertanyaan, q.judul, q.tgl_question, t.C_tags, t.CPP_tags, t.CSharp_tags, t.HTML_tags, t.PHP_tags, t.JS_tags, t.Py_tags, t.VB_tags, t.Bash_tags, t.Java_tags, t.Android_tags, t.Unity_tags FROM question q, tags t where q.id_question=t.id_question AND q.id_user = %s ORDER BY q.tgl_question DESC) AS temp", [id_user])
        question = cur.fetchall()
        data = []
        data.append(error)
        data.append(profil)
        data.append(question)
        return render_template('dashboard_free.html', data=data)
    return redirect(url_for('index'))

@app.route('/user_premium', methods=['GET', 'POST'])
def user_premium():
    error = None
    if 'username' in session:
        cur.execute("SELECT id_user FROM user WHERE username = %s", [session['username']])
        id_user = str(cur.fetchone()[0])
        cur.execute("SELECT id_user, username, email, status, foto_user, \
                    (SELECT COUNT(id_jawaban) FROM jawaban WHERE id_user = "+id_user+"), \
                    (SELECT COUNT(id_question) FROM question WHERE id_user = "+id_user+") \
                    FROM user \
                    WHERE id_user = "+id_user)
        profil = cur.fetchone()
        """
        cur.execute("SELECT q.id_question, q.id_user, q.pertanyaan, q.judul, q.tgl_question, t.C_tags, \
                    t.CPP_tags, t.CSharp_tags, t.HTML_tags, t.PHP_tags, t.JS_tags, t.Py_tags, t.VB_tags, \
                    t.Bash_tags, t.Java_tags, t.Android_tags, t.Unity_tags \
                    FROM question q, tags t where q.id_question=t.id_question AND q.id_user = %s ORDER BY q.tgl_question DESC", [id_user])
                    """
        cur.execute("SELECT temp.*, (SELECT COUNT(j.id_question) FROM jawaban j WHERE j.id_question = temp.id_question) \
                    FROM (SELECT q.id_question, q.id_user, q.pertanyaan, q.judul, q.tgl_question, t.C_tags, \
                    t.CPP_tags, t.CSharp_tags, t.HTML_tags, t.PHP_tags, t.JS_tags, t.Py_tags, t.VB_tags, \
                    t.Bash_tags, t.Java_tags, t.Android_tags, t.Unity_tags \
                    FROM question q, tags t where q.id_question=t.id_question AND q.id_user = "+id_user+" ORDER BY q.tgl_question DESC) AS temp")
        question = cur.fetchall()
        data = []
        data.append(error)
        data.append(profil)
        data.append(question)
        return render_template('dashboard_premium.html', data=data)
    return redirect(url_for('index'))

@app.route('/setting_free', methods=['GET', 'POST'])
def setting_free():
    error = None
    if 'username' in session:
        if request.method == 'GET':
            cur.execute("SELECT id_user, username, email, status, foto_user \
                        FROM user \
                        WHERE username = %s", [session['username']])
            profil = cur.fetchone()
            data = []
            data.append(error)
            data.append(profil)
            return render_template('setting_free.html', data=data)
    return redirect(url_for('index'))

@app.route('/setting_premium', methods=['GET', 'POST'])
def setting_premium():
    error = None
    if 'username' in session:
        if request.method == 'GET':
            cur.execute("SELECT id_user, username, email, status, foto_user \
                        FROM user \
                        WHERE username = %s", [session['username']])
            profil = cur.fetchone()
            data = []
            data.append(error)
            data.append(profil)
            return render_template('setting_premium.html', data=data)
    return redirect(url_for('index'))

@app.route('/update_profile', methods=['GET','POST'])
def update_profile():
    error = None
    if 'username' in session:
        cur.execute("SELECT id_user, username, email, status, foto_user \
                    FROM user \
                    WHERE username = %s", [session['username']])
        profil = cur.fetchone()
        status = profil[3]

        email_form = request.form['email']
        file = request.files['file']
        files = str(os.path.join(app.config['PATH'], secure_filename(file.filename)))
        if secure_filename(file.filename) :
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

                fileSave = {  'image' : open(os.path.join(app.config['UPLOAD_FOLDER'], filename),'rb'), 'filename' : filename }
                r = requests.post(IMAGEUPLOADPATH,files=fileSave)
                #uploaded_file(filename)
            cur.execute("UPDATE user SET foto_user = %s WHERE username = %s", \
                        ([files], [session['username']]))
        if email_form:
            cur.execute("UPDATE user SET email = %s WHERE username = %s", \
                        ([email_form], [session['username']]))
        error = "Profil berhasil di update!"
        db.commit()
        data = []
        data.append(error)
        data.append(profil)
        if status == 1:
            return render_template('setting_premium.html', data=data)
        else:
            return render_template('setting_free.html', data=data)
    return redirect(url_for('index'))

@app.route('/update_password', methods=['GET','POST'])
def update_password():
    error = None
    if 'username' in session:
        cur.execute("SELECT id_user, username, email, status, foto_user, password \
                    FROM user \
                    WHERE username = %s", [session['username']])
        profil = cur.fetchone()
        status = profil[3]
        current = profil[5]

        current_password = request.form['current_password']
        new_password1 = request.form['new_password1']
        new_password2 = request.form['new_password2']

        if new_password1 == new_password2:
            if current == current_password:
                cur.execute("UPDATE user SET password = %s WHERE username = %s", \
                            ([new_password1], [session['username']]))
                db.commit()
                error = "Password berhasil diupdate!"
            else:
                error = "Password lama tidak sesuai!"
        else:
            error = "Password baru yang Anda masukkan tidak sama!"

        data = []
        data.append(error)
        data.append(profil)
        if status == 1:
            return render_template('setting_premium.html', data=data)
        else:
            return render_template('setting_free.html', data=data)
    return redirect(url_for('index'))


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/question/<id>', methods=['GET','POST'])
def question(id):
    if 'username' in session:
        return redirect(url_for('index'))
    if request.method == 'GET' :
        cur.execute("SELECT q.*, t.*, (SELECT COUNT(j.id_question) FROM jawaban j WHERE j.id_question=q.id_question) \
                    FROM question q, tags t \
                    WHERE q.id_question=t.id_question AND q.id_question = %s", [id])
        pertanyaan = cur.fetchone()
        cur.execute("SELECT j.*, u.* \
                    FROM jawaban j, user u \
                    WHERE  j.id_user=u.id_user AND j.id_question = %s order by j.rating_jawaban desc",[id] )
        jawaban = cur.fetchall()
        data = []
        data.append(pertanyaan)
        data.append(jawaban)
        if(data):
            return render_template('question.html', data=data)

@app.route('/free_question/<id>', methods=['GET','POST'])
def free_question(id):
    if 'username' not in session:
        return redirect(url_for('index'))
    if request.method == 'GET' :
        cur.execute("SELECT q.*, t.*, (SELECT COUNT(j.id_question) FROM jawaban j WHERE j.id_question=q.id_question) \
                    FROM question q, tags t \
                    WHERE q.id_question=t.id_question AND q.id_question = %s", [id])
        pertanyaan = cur.fetchone()
        cur.execute("SELECT j.*, u.* \
                    FROM jawaban j, user u \
                    WHERE  j.id_user=u.id_user AND j.id_question = %s order by j.rating_jawaban desc",[id] )
        jawaban = cur.fetchall()
        cur.execute("SELECT id_user, username FROM user WHERE username = %s", [session['username']])
        profil = cur.fetchone()
        data = []
        data.append(pertanyaan)
        data.append(jawaban)
        data.append(profil)
        if(data):
            return render_template('question_free.html', data=data)

@app.route('/premium_question/<id>', methods=['GET','POST'])
def premium_question(id):
    if 'username' not in session:
        return redirect(url_for('index'))
    if request.method == 'GET' :
        cur.execute("SELECT q.*, t.*, (SELECT COUNT(j.id_question) FROM jawaban j WHERE j.id_question=q.id_question) \
                    FROM question q, tags t \
                    WHERE q.id_question=t.id_question AND q.id_question = %s", [id])
        pertanyaan = cur.fetchone()
        cur.execute("SELECT j.*, u.* \
                    FROM jawaban j, user u \
                    WHERE  j.id_user=u.id_user AND j.id_question = %s order by j.rating_jawaban desc",[id] )
        jawaban = cur.fetchall()
        cur.execute("SELECT id_user, username FROM user WHERE username = %s", [session['username']])
        profil = cur.fetchone()
        data = []
        data.append(pertanyaan)
        data.append(jawaban)
        data.append(profil)
        if(data):
            return render_template('question_premium.html', data=data)

#app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.secret_key = 'awankinton123'

if __name__ == '__main__':
    app.run(host=WEBHOST,debug=True, port=WEBPORT)
