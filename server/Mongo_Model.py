from pymongo import MongoClient
import datetime

# Global Variables
NAME = "Name"
# user interests
TAGS = "Tags"
EMAIL = "email"
PHONE = "phone"
POST = "Post"
DISLIKES = "Dislikes"
RSSLINK = "RSSLINK"
POST_ID = "post_id"
TITLE = "Title"
SUMMARY = "Summary"
CURRENT_TIME = "Current_Time"
PASSWORD = "Password"
SET_COMMAND = "$set"
PUSH_COMMAND = "$push"
PULL_COMMAND = "$pull"

# number of posts to obtain (currently can exceed ram causing err)
MAX_FIND = 1000


class DB:

    def __init__(self):
        self.client = MongoClient('localhost', 27017)

        self.db = self.client.poller_db

        self.pollercollection = self.db.poller_collection

        self.usercollection = self.db.user_collection

        self.trendingcollection = self.db.trending_collection

    def getTrending(self):
        curser = self.trendingcollection.find().limit(1).sort("_id", -1)
        trends = list()
        for trend in curser[0]['TRENDS']:
            trends.append(str(trend))
        return set(trends)

    # Checks if a user exists
    def ifUserExists(self, email):
        query = {EMAIL: email}
        if self.usercollection.count_documents(query) > 0:
            return True
        return False

    # Adds a user to the database
    def insert_user(self, email, name, password, phone):
        if self.ifUserExists(email):
            return False
        dic = {EMAIL: email, NAME: name, PASSWORD: password, PHONE: phone}
        self.usercollection.insert_one(dic)
        return True

    # Updates an existing users information
    def update_user(self, email, new_email, password, phone):
        if self.ifUserExists(email):

            # Edit User Info
            edit_user = {SET_COMMAND: {EMAIL: new_email, PHONE: phone, PASSWORD: password}}
            query = dict()
            query[EMAIL] = email
            self.usercollection.update(query, edit_user)

            # Retrieve User
            query = {EMAIL: new_email}
            curser = self.usercollection.find_one(query)

            try:
                return curser
            except:
                return None
        else:
            return None

    # Finds and returns a user
    def getUser(self, email):
        query = {EMAIL: email}
        curser = self.usercollection.find_one(query)
        try:
            return curser
        except:
            return None

    # Gets a users tags
    def get_tags(self, email):
        user = self.getUser(email)
        try:
            return user[TAGS]
        except:
            return None

    def add_tags(self, email, tags):

        current_tags = self.get_tags(email)

        if current_tags is None or tags.lower() not in current_tags:
            query = dict()
            query[EMAIL] = email
            addTags = {PUSH_COMMAND: {TAGS: tags}}
            self.usercollection.update(query, addTags)

    # remove tag
    def remove_tags(self, email, tags):
        query = dict()
        query[EMAIL] = email
        remove_tag = {PULL_COMMAND: {TAGS: tags}}

        self.usercollection.update(query, remove_tag)

    # Gets all posts from the database
    def get_all_posts(self):
        return self.pollercollection.find().limit(MAX_FIND).sort('createdAt', -1)

    def get_all_posts_long(self, length):
        posts = self.pollercollection.find().limit(MAX_FIND).sort('createdAt', -1)
        output = []
        url_set = set()
        for post in posts:

            try:
                url = post['URL']
                if url in url_set:
                    continue
                else:
                    url_set.add(url)
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

            try:
                interests = post['entities']

                for chunk in post['chunks']:
                    interests.append(chunk)
            except:
                interests = post['chunks']
            # Add post to output
            output.append({'_id': post['_id'], 'URL': url, 'img': image, 'title': post['title'],
                           'summary': post['summary'],
                           'text': text, 'published': post['published'], 'chunks': interests,
                           'video': video, 'sentiment_score': sentiment})

        return output

    # Adds a liked post to a users account
    def insert_liked_post(self, email, post_id, rsslink, title, summary, URL):
        query = dict()
        query[EMAIL] = email

        # Create Post Object
        post = dict()
        post[RSSLINK] = rsslink
        post[POST_ID] = post_id
        post[TITLE] = title
        post[SUMMARY] = summary
        post['URL'] = URL
        post[CURRENT_TIME] = datetime.datetime.now()

        # Store post
        new_post = {PUSH_COMMAND: {POST: post}}
        try:
            self.usercollection.update(query, new_post)
        except:
            return None

    # Store disliked posts
    def insert_disliked_post(self, email, post_id, rsslink, title, summary, URL):
        query = dict()
        query[EMAIL] = email

        # Create post object
        post = dict()
        post[RSSLINK] = rsslink
        post[POST_ID] = post_id
        post[TITLE] = title
        post[SUMMARY] = summary
        post['URL'] = URL
        post[CURRENT_TIME] = datetime.datetime.now()

        # Store post
        new_post = {PUSH_COMMAND: {DISLIKES: post}}
        try:
            self.usercollection.update(query, new_post)
        except:
            return None

    # Remove liked posts from user account
    def remove_liked_post(self, email, post_id):

        # Get necessary information
        query = dict()
        query[EMAIL] = email
        post = dict()
        post[POST_ID] = post_id

        # Remove post
        old_post = {PULL_COMMAND: {POST: post}}
        try:
            self.usercollection.update(query, old_post)
        except:
            return None

    # Remove disliked post from user account
    def remove_disliked_post(self, email, post_id):

        # Get necessary info
        query = dict()
        query[EMAIL] = email
        post = dict()
        post[POST_ID] = post_id

        # Remove post
        old_post = {PULL_COMMAND: {DISLIKES: post}}
        try:
            self.usercollection.update(query, old_post)
        except:
            return None

    # Get a users liked posts
    def get_liked_posts(self, email):
        try:
            return self.getUser(email)
        except:
            return None

    # Get a users disliked posts
    def get_disliked_posts(self, email):
        try:
            return self.getUser(email)
        except:
            return None
