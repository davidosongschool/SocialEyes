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
        following = []
        if user['following']:
            following = user['following']
        posts_to_display = []
        no_posts = 0
        # Your own latest post
        your_own_post = posts.find_one({'posted_by': session['username']}, sort=[
            ('_id', -1)])
        if your_own_post is None:
            no_posts = 1

        for username in following:
            # Find the latest post be each user the follow
            latest_post = posts.find_one({'posted_by': username}, sort=[
                ('_id', -1)])
            # Don't add any blank posts
            if latest_post is not None:
                posts_to_display.extend([latest_post])

        return render_template('dashboard.html', user=user, posts_to_display=posts_to_display, your_own_post=your_own_post, no_posts=no_posts)
    return render_template('landing.html')


@ app.route('/login')
def login():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html')


@ app.route('/login_user', methods=['POST', 'GET'])
def login_user():

    if request.method == 'GET':
        return redirect(url_for('dashboard'))

    users = mongo.db.users
    username_entered = request.form['username'].lower()
    login_user = users.find_one({'username': username_entered})

    if login_user:
        if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password']) == login_user['password']:
            session['username'] = username_entered
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
    """ This function registers a user
    """
    if 'username' in session:
        return redirect(url_for('dashboard'))

    if request.method == 'GET':
        return redirect(url_for('dashboard'))

    users = mongo.db.users

    entered_username = request.form['username'].lower()
    entered_username = entered_username.replace(" ", "")
    entered_email = request.form['email'].lower()
    entered_email = entered_email.replace(" ", "")
    existing_user = users.find_one({'username': entered_username})
    existing_email = users.find_one({'email': entered_email})

    # Check if the username or email already exists
    if existing_user is None and existing_email is None:
        encrypted = bcrypt.hashpw(
            request.form['password'].encode('utf-8'), bcrypt.gensalt())
        date = str(datetime.date.today())
        users.insert_one({'username': request.form['username'],
                          'password': encrypted,
                          'email': request.form['email'],
                          'date_registered': date,
                          'description': 'Tell Us About Yourself',
                          'following': [],
                          'followers': [],
                          'discover': True,
                          'avatar': 'https://i.ibb.co/syp2Jpw/default-avatar.png'})

        session['username'] = request.form['username']
        return redirect(url_for('dashboard'))

    error = "Username or Email already exists!"
    return render_template('landing.html', error=error)


@ app.route('/make_post', methods=["POST", 'GET'])
def make_post():

    if request.method == 'GET':
        return redirect(url_for('dashboard'))

    posts = mongo.db.posts
    date = str(datetime.date.today())
    # To get user info (their avatar)
    users = mongo.db.users
    user = users.find_one({'username': session['username']})
    post_avatar = user['avatar']

    # Create a shortened version of the url
    short_url = shorten(request.form['content_link'])

    posts.insert_one({'main_content': request.form['main_content'],
                      'posted_by': session['username'],
                      'date_posted': date,
                      'liked_by': [],
                      'reported_by': [],
                      'content_link': request.form['content_link'],
                      'short_url': short_url,
                      'post_avatar': post_avatar})
    return redirect(url_for('dashboard'))


@ app.route('/delete_post', methods=['POST', 'GET'])
def delete_post():

    if request.method == 'GET':
        return redirect(url_for('dashboard'))
    posts = mongo.db.posts
    posts.delete_one({'_id': ObjectId(request.form['post_id'])})
    return redirect(url_for('dashboard'))


@ app.route('/find')
def find():
    if 'username' not in session:
        return redirect(url_for('landing'))

    users = mongo.db.users
    user = users.find_one({'username': session['username']})
    following = []
    if user['following']:
        following = user['following']
    length = len(following)
    return render_template("follow.html", following=following, length=length)


@ app.route('/search_results', methods=['POST', 'GET'])
def search_results():

    if 'username' not in session:
        return redirect(url_for('landing'))

    if request.method == 'GET':
        return redirect(url_for('dashboard'))

    searched = request.form['searched_user']
    # Don't show yourself in search results
    my_username = session['username']
    users.mongo.db.users
    user = users.find_one({'username': my_username})
    following = []
    if user['following']:
        following = user['following']
    length = len(following)
    results = users.find({'username': {'$regex': searched, '$options': 'i'}})
    # Check that they don't already follow them
    # check if user['following'] contains specific_result.username
    return render_template('follow.html', results=results, my_username=my_username, user=user, following=following, length=length)


@ app.route('/start_following', methods=['POST', 'GET'])
def start_following():

    if 'username' not in session:
        return redirect(url_for('landing'))

    if request.method == 'GET':
        return redirect(url_for('dashboard'))

    users = mongo.db.users
    users.update({'username': session['username']}, {
                 "$push": {'following': request.form['follow_username']}})

    return redirect("/users/" + request.form['follow_username'])


@ app.route('/unfollow', methods=['POST', 'GET'])
def unfollow():

    if 'username' not in session:
        return redirect(url_for('landing'))

    if request.method == 'GET':
        return redirect(url_for('dashboard'))

    users = mongo.db.users
    users.update({'username': session['username']}, {
                 "$pull": {'following': request.form['unfollow_username']}})

    return redirect(url_for('dashboard'))


@ app.route('/settings')
def settings():
    if 'username' not in session:
        return redirect(url_for('landing'))
    return render_template('settings.html')


@ app.route('/about_me', methods=['POST', 'GET'])
def about_me():
    if 'username' not in session:
        return redirect(url_for('landing'))

    if request.method == 'GET':
        return redirect(url_for('dashboard'))

    users = mongo.db.users
    users.update({'username': session['username']}, {"$set": {
                 'description': request.form['description']}})
    return redirect(url_for('dashboard'))


@ app.route('/get_news')
def get_news():
    if 'username' not in session:
        return redirect(url_for('landing'))
    # Make environment variable for API KEY ?
    url = ('http://newsapi.org/v2/top-headlines?'
           'country=ie&'
           'apiKey=a486387335cd46e0a3c0cb8614fdc4ef')

    class1 = "ie"

    response = requests.get(url)

    return render_template('news.html', response=response.json(), class1=class1)


@ app.route('/change_news', methods=['POST', 'GET'])
def change_news():

    if 'username' not in session:
        return redirect(url_for('landing'))

    if request.method == 'GET':
        return redirect(url_for('dashboard'))

    country = request.form['country']

    url = ('http://newsapi.org/v2/top-headlines?'
           'country=' + country + '&'
           'apiKey=a486387335cd46e0a3c0cb8614fdc4ef')

    response = requests.get(url)
    class1 = ""
    class2 = ""
    class3 = ""

    if country == 'ie':
        class1 = "selected"
        class2 = "not-selected"
        class3 = "not-selected"
    elif country == "us":
        class1 = "not-selected"
        class2 = "selected"
        class3 = "not-selected"
    else:
        class1 = "not-selected"
        class2 = "not-selected"
        class3 = "selected"

    return render_template('news.html', response=response.json(), class1=class1, class2=class2, class3=class3)


@ app.route('/change_avatar', methods=['POST', 'GET'])
def change_avatar():
    if 'username' not in session:
        return redirect(url_for('landing'))

    if request.method == 'GET':
        return redirect(url_for('dashboard'))

    img_url = request.form['avatar-change']
    users = mongo.db.users
    users.update({'username': session['username']}, {"$set": {
                 'avatar': img_url}})
    return redirect(url_for('dashboard'))


@ app.route('/users/<username>')
def display_profile(username):
    if 'username' not in session:
        return redirect(url_for('landing'))
    username = username.lower()
    users = mongo.db.users
    user = users.find_one({'username': username})

    # Check that the user exists
    profile_username = username.lower()
    existing_user = users.find_one({'username': profile_username})
    # If User is not found - show error
    if existing_user is None:
        return render_template('oops.html')

    posts = mongo.db.posts
    posts_to_display = []
    # Find all posts by that user and order them by latest to earliest
    get_posts = posts.find({'posted_by': username}, sort=[
        ('_id', -1)])
    # Don't add any blank posts
    if get_posts is not None:
        for n in get_posts:
            posts_to_display.extend([n])

    # Check if user is following the profile or not
    following_users = users.find_one({'username': session['username']})
    following = 0
    for n in following_users['following']:
        if n == existing_user['username']:
            following = 1

    # Check if its your own profile
    if username == session['username']:
        following = 2

    my_username = session['username']

    return render_template('profile.html', username=username, user=user, posts_to_display=posts_to_display, following=following, my_username=my_username)


@ app.route('/delete_account')
def delete_account():
    """ This function will remove the users account and all posts made by that user
    """
    if 'username' not in session:
        return redirect(url_for('landing'))

    users = mongo.db.users
    posts = mongo.db.posts
    users.delete_one({'username': session['username']})
    posts.delete_many({'posted_by': session['username']})

    session.clear()
    return redirect(url_for('landing'))


@ app.route('/report', methods=['POST', 'GET'])
def report():
    if request.method == 'GET':
        return redirect(url_for('dashboard'))

    posts = mongo.db.posts
    posts.update({'_id': ObjectId(request.form['id'])}, {
                 "$push": {'reported_by': session['username']}})
    return redirect(url_for('dashboard'))


@ app.route('/remove_report', methods=['POST', 'GET'])
def remove_report():

    if request.method == 'GET':
        return redirect(url_for('dashboard'))

    posts = mongo.db.posts
    posts.update({'_id': ObjectId(request.form['id'])}, {
                 "$pull": {'reported_by': session['username']}})
    return redirect(url_for('dashboard'))


@ app.route('/add_like', methods=['POST', 'GET'])
def add_like():

    if request.method == 'GET':
        return redirect(url_for('dashboard'))

    posts = mongo.db.posts
    posts.update({'_id': ObjectId(request.form['id'])}, {
                 "$push": {'liked_by': session['username']}})
    return redirect(url_for('dashboard'))


@ app.route('/remove_like', methods=['POST', 'GET'])
def remove_like():

    if request.method == 'GET':
        return redirect(url_for('dashboard'))

    posts = mongo.db.posts
    posts.update({'_id': ObjectId(request.form['id'])}, {
                 "$pull": {'liked_by': session['username']}})
    return redirect(url_for('dashboard'))


def shorten(shorten_url):
    """ This function takes in a url and shortens it to 25 characters + "..." tp
    make it for suitable for sharing 
    """
    new_url = list(shorten_url)
    new_url = ''.join(shorten_url[:25]) + "..."
    return new_url


if __name__ == '__main__':
    app.secret_key = os.environ.get('key')
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')))
