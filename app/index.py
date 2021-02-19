from flask import Flask
import MySQLdb

app = Flask(__name__)

@app.route("/")
def index():
    connection = MySQLdb.connect(
        user = 'root',
        passwd = 'root',
        host = 'db',
        port = 3306,
        db = 'bank'
    )
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM user')
    user = cursor.fetchall()
    cursor.close()
    
    return str(user)

app.run(host="0.0.0.0")