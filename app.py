import os
import bcrypt
import datetime
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask import Flask, render_template, redirect, request, url_for, session
from os import path
import requests
if path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'socialize'
app.config["MONGO_URI"] = os.environ.get('Mongo')


mongo = PyMongo(app)

users = mongo.db.users
username = ''

# Not Found Page - Error Handler


@app.errorhandler(404)
def not_found(error):

    return render_template("oops.html")


@ app.route('/')
@ app.route('/landing')
def landing():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return render_template('landing.html')


@ app.route('/dashboard')
def dashboard():
    if 'username' in session:
        user = users.find_one({'username': session['username']})
        posts = mongo.db.posts
        # Display your own latest post
        check_if_post_exists = posts.find_one({'posted_by': session['username']}, sort=[
            ('_id', -1)])
        if check_if_post_exists is not None:
            my_own_post = check_if_post_exists
        else:
            # If they have not posted yet - give them a welcome message
            my_own_post = {
                'posted_by': session['username'], 'main_content': 'Welcome to SocialEyes! This is where your latest post will appear!'}
        following = []
        if user['following']:
            following = user['following']
        posts_to_display = []

        for username in following:
            # Find the latest post be each user the follow
            latest_post = posts.find_one({'posted_by': username}, sort=[
                ('_id', -1)])
            # Don't add any blank posts
            if latest_post is not None:
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

    error = "Incorrect Login! Try Again"
    bs = "d-none"
    bs2 = "d-block"
    return render_template('landing.html', error_2=error, bs=bs, bs2=bs2)


@ app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('landing'))


@ app.route('/register_user', methods=['POST', 'GET'])
def register_user():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    users = mongo.db.users
    entered_username = request.form['username'].lower()
    entered_email = request.form['email'].lower()
    existing_user = users.find_one({'username': entered_username})
    existing_email = users.find_one({'email': entered_email})
    # Check if the username or email already existsÏ

    if existing_user is None and existing_email is None:

        encrypted = bcrypt.hashpw(
            request.form['password'].encode('utf-8'), bcrypt.gensalt())
        date = str(datetime.date.today())
        users.insert_one({'username': request.form['username'],
                          'password': encrypted,
                          'email': request.form['email'],
                          'date_registered': date,
                          'description': 'Tell Us About Yourself',
                          'following': [""],
                          'followers': [""],
                          'discover': True,
                          'avatar': 'https://i.ibb.co/syp2Jpw/default-avatar.png'})

        session['username'] = request.form['username']
        return redirect(url_for('dashboard'))
    error = "Username or Email already exists!"
    return render_template('landing.html', error=error)


@ app.route('/make_post', methods=["POST"])
def make_post():
    posts = mongo.db.posts
    date = str(datetime.date.today())
    # To get user info (their avatar)
    users = mongo.db.users
    user = users.find_one({'username': session['username']})
    post_avatar = user['avatar']

    posts.insert_one({'main_content': request.form['main_content'],
                      'posted_by': session['username'],
                      'date_posted': date,
                      'liked_by': (''),
                      'content_link': '',
                      'post_avatar': post_avatar})
    return redirect(url_for('dashboard'))


@ app.route('/find')
def find():
    return render_template("follow.html")


@ app.route('/search_results', methods=['POST'])
def search_results():
    rendered = 'false'
    searched = request.form['searched_user']
    # Don't show yourself in search results
    my_username = session['username']
    users.mongo.db.users
    user = users.find_one({'username': my_username})

    results = users.find({'username': {'$regex': searched, '$options': 'i'}})
    # Check that they don't already follow them
    # check if user['following'] contains specific_result.username
    return render_template('follow.html', results=results, my_username=my_username, user=user)


@ app.route('/start_following', methods=['POST'])
def start_following():
    users = mongo.db.users
    users.update({'username': session['username']}, {
                 "$push": {'following': request.form['follow_username']}})

    return redirect(url_for('dashboard'))


@ app.route('/settings')
def settings():
    return render_template('settings.html')


@ app.route('/about_me', methods=['POST'])
def about_me():
    users = mongo.db.users
    users.update({'username': session['username']}, {"$set": {
                 'description': request.form['description']}})
    return redirect(url_for('dashboard'))


@ app.route('/get_news')
def get_news():
    # Make environment variable for API KEY ?
    url = ('http://newsapi.org/v2/top-headlines?'
           'country=ie&'
           'apiKey=a486387335cd46e0a3c0cb8614fdc4ef')

    response = requests.get(url)

    return render_template('news.html', response=response.json())


@ app.route('/change_news', methods=['POST'])
def change_news():
    country = request.form['country']

    url = ('http://newsapi.org/v2/top-headlines?'
           'country=' + country + '&'
           'apiKey=a486387335cd46e0a3c0cb8614fdc4ef')

    response = requests.get(url)

    return render_template('news.html', response=response.json())


@ app.route('/change_avatar', methods=['POST'])
def change_avatar():

    img_url = request.form['avatar-change']
    users = mongo.db.users
    users.update({'username': session['username']}, {"$set": {
                 'avatar': img_url}})
    return redirect(url_for('dashboard'))


@ app.route('/users/<username>')
def display_profile(username):
    if 'username' not in session:
        return redirect(url_for('landing'))
    users = mongo.db.users
    user = users.find_one({'username': username})

    profile_username = username.lower()
    existing_user = users.find_one({'username': profile_username})

    if existing_user is None:
        return render_template('oops.html')
    posts = mongo.db.posts
    # Display your own latest post
    find_posts = posts.find({'posted_by': username}, sort=[
        ('_id', -1)])

    user_posts = find_posts

    return render_template('profile.html', user_posts=user_posts, username=username, user=user)


if __name__ == '__main__':
    app.secret_key = 'Clodyoneill1'  # Needs to be an environment var
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
