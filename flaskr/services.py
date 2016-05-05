# from flask import Flask, session, redirect, url_for, escape, request, render_template, jsonify
# from hashlib import md5
# from base64 import b64encode
# import MySQLdb
# import os
# import json
#
# app = Flask(__name__)
#
# db = MySQLdb.connect(host="localhost", user="root", passwd="", db="tcoverflow")
# cur = db.cursor()
#
# #Get Data
# @app.route('/getAllQuestion', methods=['GET'])
# def getAllQuestion():
#     cur.execute("SELECT * FROM question")
#     return jsonify(data=cur.fetchall())
#
# @app.route('/getQuestionByIdQuestion/<id>', methods=['GET'])
# def getQuestionByIdQuestion(id):
#     cur.execute("SELECT * FROM question WHERE id_question = %s", [id])
#     return jsonify(data=cur.fetchall())
#
# @app.route('/getQuestionByIdUser/<id>', methods=['GET'])
# def getQuestionByIdUser(id):
#     cur.execute("SELECT * FROM question WHERE id_question = %s", [id])
#     return jsonify(data=cur.fetchall())
#
# @app.route('/getUserById/<id>', methods=['GET'])
# def getUserById(id):
#     cur.execute("SELECT * FROM user WHERE id_user = %s", [id])
#     return jsonify(data=cur.fetchall())
#
# @app.route('/getUserByUsername/<id>', methods=['GET'])
# def getUserByUsername(id):
#     cur.execute("SELECT * FROM user WHERE username = %s", [id])
#     return jsonify(data=cur.fetchall())
#
# @app.route('/getJawabanByIdQuestion/<id>', methods=['GET'])
# def getJawabanByIdQuestion(id):
#     cur.execute("SELECT * FROM jawaban WHERE id_soal = %s", [id])
#     return jsonify(data=cur.fetchall())
#
# @app.route('/getJawabanByIdJawaban/<id>', methods=['GET'])
# def getJawabanByIdJawaban(id):
#     cur.execute("SELECT * FROM jawaban WHERE id_jawaban = %s", [id])
#     return jsonify(data=cur.fetchall())
#
# @app.route('/getTagsByIdQuestion/<id>', methods=['GET'])
# def getTagsByIdQuestion(id):
#     cur.execute("SELECT * FROM tags WHERE id_tags = (SELECT id_tags FROM tagstoquestion WHERE id_question = %s))", [id])
#     return jsonify(data=cur.fetchall())
#
# @app.route('/getPictureByIdPicture/<id>', methods=['GET'])
# def getPictureByIdPicture(id):
#     cur.execute("SELECT * FROM picture WHERE id_picture = %s", [id])
#     return jsonify(data=cur.fetchall())
#
# @app.route('/getPictureByIdQuestion/<id>', methods=['GET'])
# def getPictureByIdQuestion(id):
#     cur.execute("SELECT * FROM picture WHERE id_question = %s", [id])
#     return jsonify(data=cur.fetchall())
#
# #Update Data
# @app.route('/updateStatusUserToFree/<id>', methods=['GET'])
# def updateStatusUserToFree(id):
#     cur.execute("SELECT user SET status=0 WHERE id_user = %s OR username = %s", ([id],[id]))
#     return jsonify(data=cur.fetchall())
#
# @app.route('/updateStatusUserToPremium/<id>', methods=['GET'])
# def updateStatusUserToPremium(id):
#     cur.execute("SELECT user SET status=1 WHERE id_user = %s OR username = %s", ([id],[id]))
#     return jsonify(data=cur.fetchall())
#
# #Delete Data
# @app.route('/deleteUser/<id>', methods=['GET'])
# def deleteUser(id):
#     cur.execute("DELETE FROM user WHERE id_user = %s OR username = %s", ([id],[id]))
#
# @app.route('/deleteQuestion/<id>', methods=['GET'])
# def deleteQuestion(id):
#     cur.execute("DELETE FROM question WHERE id_question = %s", [id])
#
# @app.route('/deleteJawaban/<id>', methods=['GET'])
# def deleteJawaban(id):
#     cur.execute("DELETE FROM jawaban WHERE id_jawaban = %s", [id])
#
# @app.route('/deletePicture/<id>', methods=['GET'])
# def deletePicture(id):
#     cur.execute("DELETE FROM picture WHERE id_picture = %s", [id])
#
# @app.route('/deleteTags/<id>', methods=['GET'])
# def deleteTags(id):
#     cur.execute("DELETE FROM tags WHERE id_tags = %s", [id])
#
# @app.route('/deleteTagsToQuestion/<id>', methods=['GET'])
# def deleteTagsToQuestion(id):
#     cur.execute("DELETE FROM tagstoquestion WHERE id_tagstoquestion = %s", [id])
#
# #app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
# app.secret_key = 'awankinton123'
#
# if __name__ == '__main__':
#     app.run(debug=True)
