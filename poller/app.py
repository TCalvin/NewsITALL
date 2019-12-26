from feed_grabber import NewsFeedParser
from trending_claculator import Trending_Calculator
import sys
import datetime

if __name__ == "__main__":
    listCNN = list()
    listCNN.append("http://rss.cnn.com/rss/cnn_topstories.rss")
    listCNN.append("http://rss.cnn.com/rss/cnn_world.rss")
    listCNN.append("http://rss.cnn.com/rss/cnn_us.rss")
    listCNN.append("http://rss.cnn.com/rss/cnn_allpolitics.rss")
    listCNN.append("http://rss.cnn.com/rss/cnn_tech.rss")
    listCNN.append("http://rss.cnn.com/rss/cnn_health.rss")
    listCNN.append("http://rss.cnn.com/rss/cnn_showbiz.rss")
    listCNN.append("http://rss.cnn.com/rss/cnn_travel.rss")

    listFoxNews = list()
    listFoxNews.append("https://feeds.foxnews.com/foxnews/latest")
    listFoxNews.append("https://feeds.foxnews.com/foxnews/most-popular")
    listFoxNews.append("https://feeds.foxnews.com/foxnews/entertainment")
    listFoxNews.append("https://feeds.foxnews.com/foxnews/health")
    listFoxNews.append("https://feeds.foxnews.com/foxnews/section/lifestyle")
    listFoxNews.append("https://feeds.foxnews.com/foxnews/opinion")
    listFoxNews.append("https://feeds.foxnews.com/foxnews/politics")
    listFoxNews.append("https://feeds.foxnews.com/foxnews/science")
    listFoxNews.append("https://feeds.foxnews.com/foxnews/sports")
    listFoxNews.append("https://feeds.foxnews.com/foxnews/tech")
    listFoxNews.append("https://feeds.foxnews.com/foxnews/internal/travel/mixed")
    listFoxNews.append("https://feeds.foxnews.com/foxnews/national")
    listFoxNews.append("https://feeds.foxnews.com/foxnews/video")
    listFoxNews.append("https://feeds.foxnews.com/foxnews/world")

    listNYTimes = list()
    listNYTimes.append("https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml")
    listNYTimes.append("https://rss.nytimes.com/services/xml/rss/nyt/World.xml")
    listNYTimes.append("https://rss.nytimes.com/services/xml/rss/nyt/US.xml")
    listNYTimes.append("https://rss.nytimes.com/services/xml/rss/nyt/NYRegion.xml")
    listNYTimes.append("https://rss.nytimes.com/services/xml/rss/nyt/Business.xml")
    listNYTimes.append("https://rss.nytimes.com/services/xml/rss/nyt/Economy.xml")
    listNYTimes.append("https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml")
    listNYTimes.append("https://rss.nytimes.com/services/xml/rss/nyt/Sports.xml")
    listNYTimes.append("https://rss.nytimes.com/services/xml/rss/nyt/Science.xml")
    listNYTimes.append("https://rss.nytimes.com/services/xml/rss/nyt/Arts.xml")
    listNYTimes.append("https://rss.nytimes.com/services/xml/rss/nyt/Television.xml")
    listNYTimes.append("https://rss.nytimes.com/services/xml/rss/nyt/Movies.xml")
    listNYTimes.append("https://rss.nytimes.com/services/xml/rss/nyt/Music.xml")
    listNYTimes.append("https://rss.nytimes.com/services/xml/rss/nyt/Theater.xml")
    listNYTimes.append("https://rss.nytimes.com/services/xml/rss/nyt/FashionandStyle.xml")
    listNYTimes.append("https://www.nytimes.com/services/xml/rss/nyt/Travel.xml")

    listWPost = list()
    listWPost.append("http://feeds.washingtonpost.com/rss/politics")
    listWPost.append("http://feeds.washingtonpost.com/rss/opinions")
    listWPost.append("http://feeds.washingtonpost.com/rss/local")
    listWPost.append("http://feeds.washingtonpost.com/rss/sports")
    listWPost.append("http://feeds.washingtonpost.com/rss/sports/blogs-columns")
    listWPost.append("http://feeds.washingtonpost.com/rss/national")
    listWPost.append("http://feeds.washingtonpost.com/rss/world")
    listWPost.append("http://feeds.washingtonpost.com/rss/business")
    listWPost.append("http://feeds.washingtonpost.com/rss/lifestyle")
    listWPost.append("http://feeds.washingtonpost.com/rss/entertainment")

    listBBC = list()
    listBBC.append("http://feeds.bbci.co.uk/news/rss.xml")
    listBBC.append("http://feeds.bbci.co.uk/news/world/rss.xml")
    listBBC.append("http://feeds.bbci.co.uk/news/uk/rss.xml")
    listBBC.append("http://feeds.bbci.co.uk/news/business/rss.xml")
    listBBC.append("http://feeds.bbci.co.uk/news/politics/rss.xml")
    listBBC.append("http://feeds.bbci.co.uk/news/health/rss.xml")
    listBBC.append("http://feeds.bbci.co.uk/news/education/rss.xml")
    listBBC.append("http://feeds.bbci.co.uk/news/science_and_environment/rss.xml")
    listBBC.append("http://feeds.bbci.co.uk/news/technology/rss.xml")
    listBBC.append("http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml")
    listBBC.append("http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml")
    listBBC.append("http://feeds.bbci.co.uk/news/world/us_and_canada/rss.xml")
    listBBC.append("http://feeds.bbci.co.uk/news/world/africa/rss.xml")
    listBBC.append("http://feeds.bbci.co.uk/news/world/asia/rss.xml")
    listBBC.append("http://feeds.bbci.co.uk/news/world/europe/rss.xml")
    listBBC.append("http://feeds.bbci.co.uk/news/world/latin_america/rss.xml")
    listBBC.append("http://feeds.bbci.co.uk/news/world/middle_east/rss.xml")

    listWSJ = list()
    listWSJ.append("https://feeds.a.dj.com/rss/RSSOpinion.xml")
    listWSJ.append("https://feeds.a.dj.com/rss/RSSWorldNews.xml")
    listWSJ.append("https://feeds.a.dj.com/rss/WSJcomUSBusiness.xml")
    listWSJ.append("https://feeds.a.dj.com/rss/RSSMarketsMain.xml")
    listWSJ.append("https://feeds.a.dj.com/rss/RSSWSJD.xml")
    listWSJ.append("https://feeds.a.dj.com/rss/RSSLifestyle.xml")

    parseList = NewsFeedParser()
    trendingcalculator = Trending_Calculator()
    trendingcalculator.calculate_trends()
    next_trending_calculation = datetime.datetime.now() + datetime.timedelta(hours=1)

    while True:
        current_time = datetime.datetime.now()
        if current_time > next_trending_calculation:
            next_trending_calculation = datetime.datetime.now() + datetime.timedelta(hours=1)
            trendingcalculator.calculate_trends()
        for link in listCNN:
            parseList.parse(link)

        for link in listFoxNews:
            parseList.parse(link)

        for link in listNYTimes:
            parseList.parse(link)

        # for link in listWPost:
            # parseList.parse(link)

        for link in listBBC:
            parseList.parse(link)

        for link in listWSJ:
            parseList.parse(link)

