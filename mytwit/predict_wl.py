"""Never make predictions...especially about the future - Sam Goldwyn"""
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
# from mytwit.__init__ import *
from mytwit.twitter import *
from .models import DB, Tweet, User

def predict_user(user1_name, user2_name, tweet_text):
    user1 = User.query.filter(User.name == user1_name).one()
    user2 = User.query.filter(User.name == user2_name).one()
    user1_embeddings = np.array([tweet.embedding for tweet in user1.tweets])
    user2_embeddings = np.array([tweet.embedding for tweet in user2.tweets])
    user1_labels = np.ones(len(user1.tweets))
    user2_labels = np.zeros(len(user2.tweets))
    
    embeddings = np.vstack([user1_embeddings, user2_embeddings])
    labels = np.concatenate([user1_labels, user2_labels])

    log_reg = LogisticRegression(solver='lbfgs', max_iter=1000)
    log_reg.fit(embeddings, labels)
    
    tweet_embedding = BASILICA.embed_sentence(tweet_text, model='twitter')
    i = int(log_reg.predict(np.array(tweet_embedding).reshape(1, -1))[0])
    
    return i,int(log_reg.predict_proba(np.array(tweet_embedding).reshape(1, -1))[0][i]*100)
