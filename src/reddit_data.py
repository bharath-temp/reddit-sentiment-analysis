import time
import datetime

import praw

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
            yield (f'{self.sub} Comment: {comment.body} \n {self.sub} \
                   Sentiment: {self.sentiment_value(comment.body)}')

    def sentiment_value(self, comment):
        return TextBlob(comment).sentiment


def main():
    wsb = Reddit_Client('6LUmSC-J4Rat1g', '0vAXTyL24HQx0MXFhNLGK1mDG04',
                        'reddit_market_analysis', 'wallstreetbets')

    investing = Reddit_Client('6LUmSC-J4Rat1g', '0vAXTyL24HQx0MXFhNLGK1mDG04',
                              'reddit_market_analysis', 'investing')

    for elem in wsb.get_comments():
        print(elem)

    for elem in investing.get_comments():
        print(elem)


if __name__ == "__main__":
    main()
