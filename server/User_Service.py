from Mongo_Model import DB
from Wiki_Tags import get_related_tags
from simlarity_finder import Similarity


class Service:

    def __init__(self):
        self.model = DB()

        # self.similarity_finder = Similarity()

    def get_user(self, id):
        return self.model.getUser(id)

    def get_interest(self, email):
        tags = self.model.get_tags(email)

    def get_all_posts(self):
        return self.model.get_all_posts()

    def get_liked_posts(self, email):
        return self.model.get_liked_posts(email)

    def get_disliked_posts(self, email):
        return self.model.get_disliked_posts(email)

    def add_liked_post(self, email, post_id, rsslink, title, summary, URL):
        return self.model.insert_liked_post(email, post_id, rsslink, title, summary, URL)

    def add_disliked_post(self, email, post_id, rsslink, title, summary, URL):
        return self.model.insert_disliked_post(email, post_id, rsslink, title, summary, URL)

    def remove_liked_post(self, email, post_id):
        return self.model.remove_liked_post(email, post_id)

    def remove_disliked_post(self, email, post_id):
        return self.model.remove_disliked_post(email, post_id)

    def update_user(self, email, new_email, password, phone):
        return self.model.update_user(email, new_email, password, phone)

    def create_user(self, email, name, password, phone):
        return self.model.insert_user(email, name, password, phone)

    def get_tags(self, email):
        return self.model.get_tags(email)

    def gettrendingtags(self):
        return self.model.getTrending()

    def add_tags(self, email, tags):
        # tags_to_add = list(tags)
        # get tags from wiki_related tags
        # make a dictionary of each tag in tags and the related tags

        return self.model.add_tags(email, tags)

    def remove_tags(self, email, tags):
        return self.model.remove_tags(email, tags)

    def search_item(self, to_search):
        related_tags = get_related_tags(to_search)
        posts = self.model.get_all_posts_long(2000)
        to_Return = list()
        for post in posts:
            good_post = False
            for chunk in post['chunks']:
                if str(to_search).lower() == str(chunk).lower():
                    good_post = True
                    break
                for tag in related_tags:
                    if str(chunk) == str(tag):
                        good_post = True
                        break
            if good_post:
                to_Return.append(post)
        return to_Return

    def check_if_user(self, email):
        user = self.model.ifUserExists(email)
        return user

    def get_user_news_feed(self, email):
        tags = self.get_tags(email)
        if tags is None or len(tags) == 0:
            return self.get_all_posts()
        related_tags = list()
        for tag in tags:
            related_tags.append(tag)
            related_tags.append(get_related_tags(tag))
        posts = self.model.get_all_posts_long(1000)
        to_Return = list()
        for post in posts:
            good_post = False
            for chunk in post['chunks']:
                #print(chunk)
                for related_tag in related_tags:
                    if str(chunk).lower() == str(related_tag).lower():
                        good_post = True
                        break
            if good_post:
                to_Return.append(post)
        return to_Return

    def getsentimentscores(self, search_tag):
        posts = self.model.get_all_posts_long(1000)
        related_tags = get_related_tags(search_tag)
        related_tags.append(search_tag)
        related_tags = set(related_tags)
        to_Return = list()
        for post in posts:
            for chunk in post['chunks']:
                for tag in related_tags:
                    if str(tag).lower() == str(chunk).lower():
                        to_Return.append((post, post['sentiment_score']))
                        break
        return to_Return

    def get_trending_posts(self):
        trending_set = self.gettrendingtags()
        posts = self.model.get_all_posts_long(200)
        title_set = set()
        to_return = list()
        for post in posts:
            #print(len(title_set))
            if str(post['URL']) in title_set:
                #print("Duplicate")
                continue
            for chunk in post['chunks']:
                if str(chunk).lower() in trending_set and str(post['URL']) not in title_set:
                    title_set.add(str(post['URL']))
                    to_return.append(post)
                    #to_return = set(to_return)
        return to_return


"""
tags = ("Donald Trump", "What's", "Apple", "city life")"""
#s = Service()
#print(s.get_trending_posts())
#print(s.get_trending_posts())
#print(s.search_item("China"))

#print(s.getsentimentscores("Donald Trump"))
#print(s.search_item("Donald Trump"))
#Need to get getsetimentscore to return new poller data
#same for search item

#need