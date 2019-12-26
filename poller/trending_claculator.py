from Model import Model
from heapq import nlargest


class Trending_Calculator:

    def __init__(self):
        self.model = Model()
        self.pronoun_set = (
        "me", "us", "you", "her", "him", "it", "them", "i", "we", "she", "he", "it", "they", "mine", "ours", "yours",
        "hers", "his", "theirs", "my", "what", "it", "my", "our", "your", "myself", "yourself", "herself", "himself",
        "itself", "ourselves", "yourselves", "themselves", "all", "another", "any", "anybody", "anyone", "anything",
        "both", "each", "either", "everybody", "everyone", "everything", "few", "many", "most", "neither", "nobody",
        "none", "no one", "nothing", "one", "other", "several", "some", "somebody", "someone", "something", "such",
        "that", "these", "this", "those", "what", "whatever", "whichever", "which", "who", "whoever", "whom",
        "whomever", "whose", "as", "that", "what", "whatever", "which", "whichever", "who", "whoever", "whom",
        "whomever", "whose", "'", "'s", "what's", "`", "What's")
        self.pronoun_set = set(self.pronoun_set)

    def calculate_trends(self):
        last_posts = self.model.get_last_n_posts(1000)
        trending_content = dict()
        for post in last_posts:
            for chunck in post:
                if chunck in trending_content and chunck.lower() not in self.pronoun_set and chunck not in self.pronoun_set:
                    trending_content[chunck.lower()] = trending_content[chunck.lower()] + 1
                else:
                    trending_content[chunck.lower()] = 1

        res = nlargest(20, trending_content, key=trending_content.get)
        self.model.write_trending(res)

t = Trending_Calculator()
t.calculate_trends()

