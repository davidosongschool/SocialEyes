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
        posts = mongo.db.posts
        # Display your own latest post
        my_own_post = posts.find_one({'posted_by': session['username']}, sort=[
                                     ('_id', -1)])

        following = user['following']
        posts_to_display = []
        for username in following:
            # Find the latest post be each user the follow
            latest_post = posts.find_one({'posted_by': username}, sort=[
                ('_id', -1)])
            posts_to_display.extend([latest_post])

        return render_template('dashboard.html', user=user, my_own_post=my_own_post, posts_to_display=posts_to_display)
    return render_template('landing.html')


@ app.route('/login')
def login():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html')


@ app.route('/login_user', methods=['POST'])
def login_user():
    users = mongo.db.users
    login_user = users.find_one({'username': request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('dashboard'))

    return 'Invalid username/password combination'


@ app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


@ app.route('/register_user', methods=['POST', 'GET'])
def register_user():
    if 'username' in session:
        return redirect(url_for('dashboard'))

    # Still need to check if the username or email already existsÏ
    users = mongo.db.users
    encrypted = bcrypt.hashpw(
        request.form['password'].encode('utf-8'), bcrypt.gensalt())
    date = str(datetime.date.today())
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


@ app.route('/make_post', methods=["POST"])
def make_post():
    posts = mongo.db.posts
    date = str(datetime.date.today())
    posts.insert_one({'main_content': request.form['main_content'],
                      'posted_by': session['username'],
                      'date_posted': date,
                      'liked_by': (''),
                      'content_link': ''})
    return redirect(url_for('dashboard'))


@ app.route('/start_following', methods=['POST'])
def start_following():
    users = mongo.db.users
    account = users.find_one({'username': session['username']})
    users.update({'username': session['username']}, {
                 "$push": {'following': request.form['follow_username']}})

    return redirect(url_for('dashboard'))


if __name__ == '__main__':
    app.secret_key = 'Clodyoneill1'  # Needs to be an environment var
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
