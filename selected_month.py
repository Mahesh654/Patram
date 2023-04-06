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


@app.route('/onemonth',methods=['POST'])

def Get_Range_Of_Renewal1():

    try:        

         Act= request.json['MAHESH']
         if Act and request.method == 'POST':          

            sqlQuery = "select*FROM customer_master WHERE DATE_FORMAT(Date_Of_Registration,'%Y-%m')=%s";
            print(sqlQuery)

            cursor = mydb.cursor(dictionary=True)

            cursor.execute(sqlQuery,[Act])

            value=cursor.fetchall()

            print(value)

            return jsonify(value)              

         else:

             return showMessage()

    except Exception as e:
         return e
def showMessage(error=None):

    message = {

        'status': 404,

        'message': 'Record not found: ' + request.url,

    }

    respone = jsonify(message)

    respone.status_code = 404

    return respone

       

if __name__ == "__main__":

    app.run(debug=True)
         