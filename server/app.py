from flask import Flask, request, jsonify
from flask_cors import CORS
from User_Service import Service
from flask_bcrypt import Bcrypt
from flask_jwt_extended import (create_access_token,
                                JWTManager,
                                jwt_required,
                                get_jwt_identity)
import datetime

app = Flask(__name__)
service = Service()

# Authentication Stuff @Jens
app.config['JWT_SECRET_KEY'] = 'secret'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=0, seconds=540)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

CORS(app)
app.secret_key = "GitItDone"
logged_in_users = list()


# add tags(interest) for user
@app.route('/addTag', methods=['GET', 'POST'])
def addTag():
    email = request.get_json()['email']
    tag = request.get_json()['tags']
    print(tag)
    var = service.add_tags(email, tag)

    if var is not None:
        return var
    else:
        return jsonify({"msg": "Tag already exists!"})


# get all tags
@app.route('/getTags', methods=['GET', 'POST'])
def getTags():
    email = request.get_json()['email']
    tag_list = service.get_tags(email)
    print(tag_list)
    if tag_list is not None:
        return jsonify({'result': tag_list})
    else:
        return "No Tags"


# remove tags
@app.route('/removeTag', methods=['GET', 'POST'])
def removeTag():
    email = request.get_json()['email']
    tags = request.get_json()['tags']

    var = service.remove_tags(email, tags)

    if var is not None:
        return var
    else:
        return "None"


# Route is called when a user is registering
@app.route('/register', methods=['GET'])
def register():
    # Set user information
    email = request.args.get('email')
    name = "NULL"
    password = request.args.get('password')
    phone = ""

    # Check if the user is already registered
    user = service.get_user(email)
    if user is None:

        # Create User
        service.create_user(email, name, password, phone)
        return jsonify({"msg": "You're in! Enjoy."})
    else:
        return jsonify({"msg": "Email(User) already exists"})


# Route is called when a user attempts to login
@app.route('/login', methods=['GET'])
def login():
    # Get login info
    email = request.args.get('email')
    password = request.args.get('password')

    # Check if user exists
    response = service.get_user(email)

    try:
        val = bcrypt.check_password_hash(password, response['Password'])
    except:
        return jsonify({"msg": "Unable to parse password",
                        "status": 1})

    # There was a user and the password was correct
    if response is not None and val:
        logged_in_users.append(email)
        access_token = create_access_token(identity=email)

        return jsonify({"msg": email + " login successful",
                        "token": access_token,
                        "status": 0})

    # There was a user but the password wasn't correct
    elif response is not None:
        return jsonify({"msg": "Wrong Password",
                        "status": 1})

    # User doesn't exist
    else:
        return jsonify({"msg": "User Email doesn't exist",
                        "status": 2})


# This route is called when a user needs to be validated for access to pages
@app.route('/validate', methods=['GET', 'OPTIONS'])
@jwt_required
def validate():
    val = get_jwt_identity()
    return jsonify({"email": val})


# This route gets user information
@app.route('/updateuser')
def update_user():
    # Get arguments
    email = request.args.get('email')
    new_email = request.args.get('newEmail')
    password = request.args.get('password')
    phone = request.args.get('phone')

    # Update user info and get it back
    answer = service.update_user(str(email), str(new_email), str(password), str(phone))

    if answer is None:
        return "None"

    # Format output
    output = {'email': answer['email'], 'password': answer['Password'], 'phone': answer['phone'],
              'address': answer['address']}

    return jsonify({'result': output})


# This route gets user information
@app.route('/getuser')
def get_user():
    email = request.args.get('email')
    answer = service.get_user(str(email))
    if answer is None:
        return "None"
    try:
        output = {'email': answer['email'], 'password': answer['Password'], 'phone': answer['phone']}
    except:
        return "None"

    return jsonify({'result': output})


# Route used to create a user which may not be necessary anymore
# REMOVE?
@app.route('/createuser')
def create_user():
    email = request.args.get('email')
    name = request.args.get('name')
    password = request.args.get('password')
    answer = service.create_user(email, name, password)
    if answer:
        return "True"
    return "False"


# General feed only based on time for unregistered users
@app.route('/getallposts', methods=['GET', 'POST'])
def get_all_posts():
    # Get posts
    all_posts = service.get_all_posts()

    # Get a users liked and disliked posts
    output = []
    liked = False
    disliked = False

    # Mark incoming posts as liked or disliked if they need
    for post in all_posts:

        try:
            url = post['URL']
        except:
            url = ''

        try:
            sentiment = post['sentiment_score']
        except:
            sentiment = '-1'

        # Add post to output
        output.append({'post_id': str(post['_id']), 'URL': url, 'img': post['img'], 'title': post['title'],
                       'summary': post['summary'],
                       'text': post['text'], 'published': post['published'], 'interests': post['chunks'],
                       'video': post['video'], 'liked': liked, 'disliked': disliked, 'sentiment_score': sentiment})

        # Limit to 50 articles
        if len(output) >= 50:
            break

    return jsonify({'result': output})


# General feed only based on time for unregistered users
@app.route('/getuserposts', methods=['GET', 'POST'])
def get_user_posts():

    # Get posts
    email = request.get_json()['email']
    all_posts = service.get_user_news_feed(email)


    # Get a users liked and disliked posts
    liked_posts = service.get_liked_posts(email)
    disliked_posts = service.get_disliked_posts(email)
    output = []
    liked = False
    disliked = False

    # Mark incoming posts as liked or disliked if they need
    for post in all_posts:

        # Mark Liked
        if liked_posts is not None:
            try:
                for like in liked_posts['Post']:
                    if post['title'] == like['Title']:
                        liked = True
                        break
            except:
                liked = False

        # Mark Disliked
        if disliked_posts is not None:
            try:
                for dislike in disliked_posts['Dislikes']:
                    if post['title'] == dislike['Title']:
                        disliked = True
                        break
            except:
                disliked = False

        try:
            url = post['URL']
        except:
            url = ''

        try:
            sentiment = post['sentiment_score']
        except:
            sentiment = '-1'

        # Add post to output
        output.append({'post_id': str(post['_id']), 'URL': url, 'img': post['img'], 'title': post['title'],
                       'summary': post['summary'],
                       'text': post['text'], 'published': post['published'], 'video': post['video'],
                       'interests': post['chunks'],
                       'liked': liked, 'disliked': disliked, 'sentiment_score': sentiment})

        liked = False
        disliked = False

        # Limit to 50 articles
        if len(output) >= 50:
            break

    return jsonify({'result': output})


# Returns the liked articles for a specific user
@app.route('/getlikedposts', methods=['GET', 'POST'])
def get_posts():
    # Get Posts
    email = request.get_json()['email']
    answer = service.get_liked_posts(email)

    if answer is None:
        return "None"

    # Format output
    output = []
    try:
        for q in answer['Post']:
            try:
                URL = q['URL']
            except:
                URL = ''
            output.append({'post_id': q['_id'], 'title': q['Title'], 'rss': q['RSSLINK'], 'summary': q['Summary'], 'URL' : URL})
    except:
        output = []

    return jsonify({'result': output})


# Route for returning disliked posts
@app.route('/getdislikedposts', methods=['GET', 'POST'])
def get_disliked_posts():
    email = request.get_json()['email']
    dislikes = service.get_disliked_posts(email)

    if dislikes is None:
        return "None"

    output = []
    try:
        for dislike in dislikes['Dislikes']:
            try:
                URL = dislike['URL']
            except:
                URL = ''

            output.append({'post_id': dislike['_id'], 'title': dislike['Title'], 'rss': dislike['RSSLINK'],
                           'summary': dislike['Summary'], 'URL': URL})
    except:
        output = []

    return jsonify({'result': output})


@app.route('/gettrending', methods=['POST'])
def gettrendingtags():
    posts = service.get_trending_posts()

    # Mark incoming posts as liked or disliked if they need
    output = []
    for post in posts:

        try:
            url = post['URL']
        except:
            url = ''

        try:
            sentiment = post['sentiment_score']
        except:
            sentiment = '-1'

        try:
            image = post['img']
        except:
            image = ''

        try:
            text = post['text']
        except:
            text = ''

        try:
            video = post['video']
        except:
            video = ''

        # Add post to output
        output.append({'post_id': str(post['_id']), 'URL': url, 'img': image, 'title': post['title'],
                       'summary': post['summary'],
                       'text': text, 'published': post['published'], 'interests': post['chunks'],
                       'video': video, 'sentiment_score': sentiment})

    return jsonify({'result': output})


@app.route('/getusertrending', methods=['POST'])
def getusertrendingtags():
    posts = service.get_trending_posts()

    # Get a users liked and disliked posts
    email = request.get_json()['email']
    liked_posts = service.get_liked_posts(email)
    disliked_posts = service.get_disliked_posts(email)
    liked = False
    disliked = False

    # Mark incoming posts as liked or disliked if they need
    output = []
    for post in posts:

        # Mark Liked
        if liked_posts is not None:
            try:
                for like in liked_posts['Post']:
                    if post['title'] == like['Title']:
                        liked = True
                        break
            except:
                liked = False


        # Mark Disliked
        if disliked_posts is not None:
            try:
                for dislike in disliked_posts['Dislikes']:
                    if post['title'] == dislike['Title']:
                        disliked = True
                        break
            except:
                disliked = False


        try:
            url = post['URL']
        except:
            url = ''

        try:
            sentiment = post['sentiment_score']
        except:
            sentiment = '-1'

        try:
            image = post['img']
        except:
            image = ''

        try:
            text = post['text']
        except:
            text = ''

        try:
            video = post['video']
        except:
            video = ''

        # Add post to output
        output.append({'post_id': str(post['_id']), 'URL': url, 'img': image, 'title': post['title'],
                       'summary': post['summary'],
                       'text': text, 'published': post['published'], 'interests': post['chunks'],
                       'video': video, 'liked': liked, 'disliked': disliked, 'sentiment_score': sentiment})

        liked = False
        disliked = False

    return jsonify({'result': output})


@app.route('/getuserfeed', methods=['POST'])
def getuserfeed():
    email = request.args.get('email')
    return jsonify(service.get_user_news_feed(email))


# DON'T THINK THIS IS NEEDED
@app.route('/searchtext')
def return_search():
    to_search = request.args.get('to_search')
    return to_search


# Add a liked post to a users account
@app.route('/addlikedpost', methods=['POST'])
def addlikedpost():
    # Get necessary info
    email = request.get_json()['email']
    post_id = request.get_json()['post_id']
    rsslink = request.get_json()['rsslink']
    title = request.get_json()['title']
    summary = request.get_json()['summary']
    URL = request.get_json()['URL']
    # Add post
    var = service.add_liked_post(email, post_id, rsslink, title, summary, URL)

    if var is None:
        return "None"
    else:
        return var


# Route for adding disliked posts
@app.route('/adddislikedpost', methods=['POST'])
def adddislikedpost():
    # Get information
    email = request.get_json()['email']
    post_id = request.get_json()['post_id']
    rsslink = request.get_json()['rsslink']
    title = request.get_json()['title']
    summary = request.get_json()['summary']
    URL = request.get_json()['URL']

    # Add Post
    var = service.add_disliked_post(email, post_id, rsslink, title, summary, URL)
    if var is None:
        return "None"
    else:
        return var


# Route for removing liked posts
@app.route('/removelikedpost', methods=['POST'])
def removelikedpost():
    # Get info
    email = request.get_json()['email']
    post_id = request.get_json()['post_id']

    # Remove Post
    var = service.remove_liked_post(email, post_id)
    if var is None:
        return "None"
    else:
        return var


# Route for removing disliked posts
@app.route('/removedislikedpost', methods=['POST'])
def removedislikedpost():
    # Get info
    email = request.get_json()['email']
    post_id = request.get_json()['post_id']

    # Remove Post
    var = service.remove_disliked_post(email, post_id)
    if var is None:
        return "None"
    else:
        return var


# Searches for articles based on a term
@app.route('/searchterm', methods=['POST'])
def searchterm():
    # Get Posts
    term = request.get_json()['term']
    print(term)
    all_posts = service.search_item(term.lower())
    output = []

    # Mark incoming posts as liked or disliked if they need
    for post in all_posts:

        try:
            url = post['URL']
        except:
            url = ''

        try:
            sentiment = post['sentiment_score']
        except:
            sentiment = '-1'

        try:
            image = post['img']
        except:
            image = ''

        try:
            text = post['text']
        except:
            text = ''

        try:
            video = post['video']
        except:
            video = ''

        # Add post to output
        output.append({'post_id': str(post['_id']), 'URL': url, 'img': image, 'title': post['title'],
                       'summary': post['summary'],
                       'text': text, 'published': post['published'], 'interests': post['chunks'],
                       'video': video, 'sentiment_score': sentiment})

        # Limit to 50 articles
        if len(output) >= 50:
            break

    # print(output)
    return jsonify({'result': output})


# Searches for articles based on a term
@app.route('/usersearchterm', methods=['POST'])
def usersearchterm():
    # Get Posts
    term = request.get_json()['term']
    print(term)
    all_posts = service.search_item(term.lower())
    output = []

    # Get a users liked and disliked posts
    email = request.get_json()['email']
    liked_posts = service.get_liked_posts(email)
    disliked_posts = service.get_disliked_posts(email)
    liked = False
    disliked = False

    # Mark incoming posts as liked or disliked if they need
    for post in all_posts:

        # Mark Liked
        if liked_posts is not None:
            try:
                for like in liked_posts['Post']:
                    if post['title'] == like['Title']:
                        liked = True
                        break
            except:
                liked = False

        # Mark Disliked
        if disliked_posts is not None:
            try:
                for dislike in disliked_posts['Dislikes']:
                    if post['title'] == dislike['Title']:
                        disliked = True
                        break
            except:
                disliked = False

        try:
            url = post['URL']
        except:
            url = ''

        try:
            sentiment = post['sentiment_score']
        except:
            sentiment = '-1'

        try:
            image = post['img']
        except:
            image = ''

        try:
            text = post['text']
        except:
            text = ''

        try:
            video = post['video']
        except:
            video = ''

        # Add post to output
        output.append({'post_id': str(post['_id']), 'URL': url, 'img': image, 'title': post['title'],
                       'summary': post['summary'],
                       'text': text, 'published': post['published'], 'interests': post['chunks'],
                       'video': video, 'liked': liked, 'disliked': disliked, 'sentiment_score': sentiment})

        liked = False
        disliked = False

        # Limit to 50 articles
        if len(output) >= 50:
            break

    # print(output)
    return jsonify({'result': output})


@app.route('/sentimentscore', methods=['POST'])
def getsentimentscores():
    term = request.args.get('term')
    posts = service.getsentimentscores(term)
    # Make sure posts are returned
    if posts is None:
        return "None"
    return jsonify({'result': posts})


if __name__ == "__main__":
    app.run(debug=True)
