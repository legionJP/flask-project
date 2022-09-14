from email.policy import default
from pyexpat import model
import sqlite3
from os import error, path
from datetime import datetime  
import pymysql
 
 

#from ssl import _PasswordType


from flask import Flask
from flask_socketio import SocketIO, join_room, leave_room, emit
#from flask import Session
import mysql.connector


app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy
from flask import Flask,render_template, request
from flask_mysqldb import MySQL, cursors , MySQLdb
from  MySQLdb import Connect 
from flask_migrate import Migrate
mysql = MySQL(app) 
db = MySQL(app)
db.init_app(app)
db= MySQL()
migrate = Migrate(app, db)
import mysql.connector
#import mysql.connector as mysql
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql:///root:JPsdatabase@23@localhost/jp_db'
mydb =mysql.connector.connect(         #creating the varriable 
    host="localhost",
    user="root",
    passwd="JPsdatabase@23"
)

my_cursor = mydb.cursor()
#my_cursor.execute("CREATE DATABASE jp_db")  # commenting after creating the database

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)
 
# Creating the db model

 
 
  #  room=db.column(db.String(100) )
      
  #   chat_date= db.column(db.DateTime,default=datetime.utcnow)   

  # function to return string when we add somethings
#def __repr__(self):
 #   return '<Name %r>' % self.id    
