from datetime import date 
from email import message
from flask import Flask,app,render_template,redirect

import pymysql


from flask import jsonify

from flask import flash, request
import mysql.connector

from flask_mysqldb import MySQL

app = Flask(__name__)

app.secret_key = 'xyzsdfg'



mydb = mysql.connector.connect(

  host="patram-subscription-db.c4qldlczzvrr.us-east-1.rds.amazonaws.com",

  user="admin",

  password="admin123",

  database="patram"
)

mysql = MySQL(app)

@app.route('/viewall', methods =['GET', 'POST'])

def view_data():

  cursor = mydb.cursor(dictionary=True)

  cursor.execute("SELECT * FROM customer_master")

  rows= cursor.fetchall()

    # print (rows)

  return jsonify(rows)

if __name__ == "__main__":

    app.run(debug=True,port=5001)