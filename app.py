import os
import bcrypt
import datetime
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask import Flask, render_template, redirect, request, url_for
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'socialize'
app.config["MONGO_URI"] = os.environ.get('Mongo')


mongo = PyMongo(app)


@app.route('/')
@app.route('/landing')
def landing():
    # Check to see if the session is set - if it is then render dashboard -
    # If not then give option to register or login
    return render_template('landing.html')


@app.route('/register_user', methods=['POST', 'GET'])
def register_user():
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
                       'avater': 'Choose a picture'})

    return render_template('dashboard.html', user = users.find_one({'username': request.form['username']}))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
