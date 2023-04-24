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



@app.route('/filtering', methods =['GET', 'POST'])
def filteredData():
    data=request.json
    date=data.get('Input_date')
    inputArray=data.get('Input_array')
    allRecordsQuery=" select customer_master.Date_Of_Registration,customer_master.Register_Email,customer_master.Customer_Id,customer_master.Approved_Date,customer_master.Next_Renewal,subsription_payment.Subscription_Start,subsription_payment.Subscription_End,subsription_payment.Payment_Type,subsription_payment.Payment_Date from customer_master left join subsription_payment on customer_master.Customer_Id=subsription_payment.Customer_Id"
    #allRecordsQuery=" where DATE_FORMAT(Subscription_Start,'%Y-%m') <=%s and DATE_FORMAT(Subscription_End,'%Y-%m')>=%s"
    additionQuery=" where DATE_FORMAT(Subscription_Start,'%Y-%m')=%s"
    expiryQuery=" where DATE_FORMAT(Subscription_End,'%Y-%m')= %s"
    activeQuery=" where DATE_FORMAT(Subscription_Start,'%Y-%m')<=%s and DATE_FORMAT(Subscription_End,'%Y-%m')>=%s"
    
    if inputArray['allRecords']=='1':
        
        #print(mainQuery)
        cursor = mydb.cursor(dictionary=True)
        cursor.execute( allRecordsQuery)
        rows=cursor.fetchall()
        print(rows)
        return jsonify(rows)
        
    elif inputArray['activeRecords']=='1':
        
        #print(mainQuery+allRecordsQuery)
        cursor=mydb.cursor(dictionary=True)
        cursor.execute( allRecordsQuery+activeQuery,[date,date])
        rows=cursor.fetchall()
        print(rows)
        return jsonify(rows)
    elif inputArray['additionData']=='1':
        #print(mainQuery+additionQuery)
        cursor=mydb.cursor(dictionary=True)
        cursor.execute( allRecordsQuery+additionQuery,[date])
        rows=cursor.fetchall()
        print(rows)
        return jsonify(rows)
    elif inputArray['expiryData']=='1':
        
        #print(mainQuery+expiryQuery)
        cursor=mydb.cursor(dictionary=True)
        cursor.execute( allRecordsQuery+expiryQuery,[date])
        rows=cursor.fetchall()
        print(rows)
        return jsonify(rows)
        
    else:
        return jsonify(rows)
if __name__ == "__main__":
    app.run(debug=True,port=5001)
