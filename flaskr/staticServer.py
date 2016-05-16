from flask import Flask, send_from_directory, session, redirect, url_for, escape, request, render_template, jsonify,make_response
from pprint import pprint
from werkzeug import secure_filename
import os

app = Flask(__name__)

app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'PNG', 'JPG', 'JPEG', 'GIF'])
app.config['UPLOAD_FOLDER'] = '/var/www/html/cloudUpload/flaskr/static/foto/'

WEBHOST = 'localhost'
WEBPORT = 5001

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/', methods=['POST'])
def upload_files():
    print "a request is coming!"
    file = request.files['image']
    resp = make_response()

    filename = file.filename
    jaja = file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename ))
    if jaja:
        resp.status_code = 200
    else:
        resp.status_code = 411
    # resp.status_code =200
    return resp

if __name__ == '__main__':
    app.run(host=WEBHOST,debug=True,port=WEBPORT)