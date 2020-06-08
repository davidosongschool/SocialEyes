import os
import bcrypt
import datetime
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask import Flask, render_template, redirect, request, url_for, session
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'socialize'
app.config["MONGO_URI"] = os.environ.get('Mongo')


mongo = PyMongo(app)

users = mongo.db.users
username = ''


@app.route('/')
@app.route('/landing')
def landing():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return render_template('landing.html')


@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        user = users.find_one({'username': session['username']})
        return render_template('dashboard.html', user=user)
    return render_template('landing.html')


@app.route('/login')
def login():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html')



@app.route('/login_user', methods=['POST'])
def login_user():
    users = mongo.db.users
    login_user = users.find_one({'username' : request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('dashboard'))

    return 'Invalid username/password combination'



@app.route('/register_user', methods=['POST', 'GET'])
def register_user():
    if 'username' in session:
        return redirect(url_for('dashboard'))

    #Still need to check if the username or email already existsÏ
    users = mongo.db.users
    encrypted = bcrypt.hashpw(
    request.form['password'].encode('utf-8'), bcrypt.gensalt())
    date = datetime.datetime.now()
    users.insert_one({'username': request.form['username'],
                        'password': encrypted,
                        'email': request.form['email'],
                        'date_registered': date,
                        'description': 'Tell Us About Yourself',
                        'following': (1, 2, 3),
                        'followers': (3, 2, 1),
                        'discover': True,
                        'avatar': 'Choose a picture'})

    session['username'] = request.form['username']
    return redirect(url_for('dashboard'))


if __name__ == '__main__':
    app.secret_key = 'Clodyoneill1' #Needs to be an environment var
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
