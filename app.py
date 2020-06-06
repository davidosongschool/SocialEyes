import os
import bcrypt
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
    users.insert({'username': request.form['username'],
                  'password': encrypted, 'email': request.form['email']})

    return 'Go to the new Dashboard Here'


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
