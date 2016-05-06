

import MySQLdb
db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="tcoverflow")
cur = db.cursor()