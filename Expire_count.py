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


@app.route('/Expire',methods=['POST'])

def Get_Range_Of_Renewal1():

    try:        
       
        _Act= request.json['MAHESH']
        print(_Act)
        if _Act and request.method == 'POST':          
            sqlQuery = "select count(id) as Expired from subsription_payment where  DATE_FORMAT(Subscription_End,'%Y-%m') <=%s"
            print(sqlQuery)
            cursor = mydb.cursor(dictionary=True)
            cursor.execute(sqlQuery,[_Act])
            value=cursor.fetchall()
            print(value)
            return jsonify(value)              

        else:
            return showMessage()

    except Exception as e:
         return "Exception Occuered"
def showMessage(error=None):

    message = {

        'status': 404,

        'message': 'Record not found: ' + request.url,

    }

    respone = jsonify(message)

    respone.status_code = 404

    return respone

       

if __name__ == "__main__":

    app.run(debug=True,port=5002)
         