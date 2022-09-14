from fileinput import close
from unicodedata import name
#event import
from flask import session, Flask,redirect, url_for, render_template, request

from app.main import db
from . import main
from app import create_app, socketio
from .forms import LoginForm
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQLdb ,MySQL
app= Flask('__name__')
mysql = MySQL(app)
db = MySQL(app)
#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = 'JPsdatabase@23'
#app.config['MYSQL_DB'] = 'my_db'
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql:///root:JPsdatabase@23@localhost/jp_db'

@main.route('/', methods=['GET', 'POST'])
def index():
     
     
    """Login form to enter a room."""
    form = LoginForm()    
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['room'] = form.room.data        
        return redirect(url_for('.chat'))
     
     

    elif request.method == 'GET':
        form.name.data = session.get('name', '')
        form.room.data = session.get('room', '')
    return render_template('index.html', form=form)


@main.route('/chat')
def chat():
     
    """Chat room. The user's name and room must be stored in
    the session."""
         
    name = session.get('name', '')
    room = session.get('room', '')
    if name == '' or room == '':
        return redirect(url_for('.index'))

    return render_template('chat.html', name=name, room=room)
        

    #name = session.get('name', '')
    #room = session.get('room', '')
    #if name == '' or room == '':
    #   return redirect(url_for('.index'))
    #return render_template('chat.html', name=name, room=room)
