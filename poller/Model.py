from pymongo import MongoClient
import datetime
import time
import os  # will be used for actual reference


class Model:

    def __init__(self, yes=False):
        self.docker_port = 42069
        self.standard_mongo = 27017
        if yes:
            self.client = MongoClient('localhost', self.docker_port)
        else:
            self.client = MongoClient('localhost', self.standard_mongo)

        self.db = self.client.poller_db

        self.pollercollection = self.db.poller_collection

        self.trendingcollection = self.db.trending_collection

    def savePoll(self, polledDictionary):
        polledDictionary['createdAt'] = datetime.datetime.now()

        self.pollercollection.insert_one(polledDictionary)

    def get_last_n_posts(self, length):
        curser = self.pollercollection.find().limit(1000).sort('createdAt', -1)
        output = []
        for q in curser:
            try:
                output.append(q['chunks'])
            except:
                continue
        return output

    def write_trending(self, trending_content):
        current_trending = dict()
        current_trending["TRENDS"] = trending_content
        current_trending["TIME"] = str(time.asctime())
        # print(str(time.asctime()))
        self.trendingcollection.insert_one(current_trending)
