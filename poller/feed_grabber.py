import feedparser
from Extraction import Extractor
from Model import Model
from newspaper import Article
from Sentiment_Score import Sentiment_Analysis
import datetime
import heapq


class NewsFeedParser:
    def __init__(self):
        self.extractor = Extractor()
        self.model = Model(True)
        self.current_titles = dict()
        self.current_state = 0
        self.sentiment = Sentiment_Analysis()
        self.count_occurances = dict()


    def parse(self, RSSLink):
        self.current_state = self.current_state + 1
        doc = feedparser.parse(RSSLink)
        for key in doc.entries:
            if key.title not in self.current_titles:
                self.current_titles[key.title] = datetime.datetime.now()
                dictionary = dict()
                try:
                    dictionary['title'] = key.title
                    dictionary['summary'] = key.summary
                    dictionary['URL'] = key.link

                    # get article specific information
                    article = Article(key.link)
                    article.download()
                    article.parse()
                    try:
                        dictionary['text'] = article.text
                    except:
                        dictionary['text'] = ''

                    try:
                        dictionary['img'] = article.top_image
                    except:
                        dictionary['img'] = ''
                    try:
                        dictionary['video'] = article.movies[0]
                    except:
                        dictionary['video'] = ''

                    try:
                        score = self.sentiment.get_score(str(key.title) + ' '+ str(key.summary))
                        if score < .10 and score != -1:
                            state = 0
                        elif score <= .2:
                            state = 1
                        elif score <= .3:
                            state = 2
                        elif score <= .4:
                            state = 3
                        elif score <= .5:
                            state = 4
                        elif score <= .6:
                            state = 5
                        elif score <= .7:
                            state = 6
                        elif score <= .8:
                            state = 7
                        elif score <= .9:
                            state = 8
                        else:
                            state = 9
                    except:
                        state = -1

                    dictionary['sentiment_score'] = str(state)

                    try:
                        dictionary['published'] = key.published
                    except:
                        dictionary['published'] = ""
                    dictionary['RSSLink'] = RSSLink
                    sentences = self.extractor.getSentences(key.title)
                    entities = list()
                    chuncks = list()
                    for sentence in sentences:
                        ents = self.extractor.getEntities(sentence)
                        for en in ents:
                            entities.append(str(en).lower())
                        chks = self.extractor.getNounChunks(sentence)
                        for c in chks:
                            chuncks.append(str(c).lower())
                    dictionary['entities'] = entities
                    dictionary['chunks'] = chuncks

                    self.model.savePoll(dictionary)

                except Exception as e:
                    continue

