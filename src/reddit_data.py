import time
import datetime
from threading import Thread

import praw
import asyncio
from textblob import TextBlob


class Reddit_Client():
    def __init__(self, client_id, client_secret, user_agent, sub):
        self.client_id = client_id
        self.client_secret = client_secret
        self.user_agent = user_agent
        self.sub = sub

    def create_reddit_instance(self):
        return praw.Reddit(client_id=self.client_id,
                           client_secret=self.client_secret,
                           user_agent=self.user_agent)

    def get_comments(self):
        subreddit = self.create_reddit_instance().subreddit(self.sub)
        for comment in subreddit.stream.comments(skip_existing=True):
            print(f'{self.sub} Comment: {comment.body} \n {self.sub} \
                   Sentiment: {self.sentiment_value(comment.body)}')

    def sentiment_value(self, comment):
        return TextBlob(comment).sentiment


def main():

    wsb = Reddit_Client('6LUmSC-J4Rat1g',
                        '0vAXTyL24HQx0MXFhNLGK1mDG04',
                        'reddit_market_analysis', 'wallstreetbets')

    investing = Reddit_Client('6LUmSC-J4Rat1g',
                              '0vAXTyL24HQx0MXFhNLGK1mDG04',
                              'reddit_market_analysis', 'investing')

    rh = Reddit_Client('6LUmSC-J4Rat1g',
                       '0vAXTyL24HQx0MXFhNLGK1mDG04',
                       'reddit_market_analysis', 'RobinHood')

    options = Reddit_Client('6LUmSC-J4Rat1g',
                            '0vAXTyL24HQx0MXFhNLGK1mDG04',
                            'reddit_market_analysis', 'options')

    stock_market = Reddit_Client('6LUmSC-J4Rat1g',
                                 '0vAXTyL24HQx0MXFhNLGK1mDG04',
                                 'reddit_market_analysis', 'StockMarket')

    worker_wsb = Thread(target=wsb.get_comments)
    worker_wsb.setDaemon(True)
    worker_wsb.start()

    worker_invest = Thread(target=investing.get_comments)
    worker_invest.setDaemon(True)
    worker_invest.start()

    worker_rh = Thread(target=rh.get_comments)
    worker_rh.setDaemon(True)
    worker_rh.start()

    worker_options = Thread(target=options.get_comments)
    worker_options.setDaemon(True)
    worker_options.start()

    worker_stock_market = Thread(target=stock_market.get_comments)
    worker_stock_market.setDaemon(True)
    worker_stock_market.start()

    worker_wsb.join()
    worker_invest.join()
    worker_rh.join()
    worker_options.join()
    worker_stock_market.join()


if __name__ == "__main__":
    main()
