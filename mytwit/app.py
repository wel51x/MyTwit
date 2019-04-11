"""Main appl and routing logic for MyTwit."""
from flask import Flask, render_template, request
from .models import DB, User
from .predict import predict_user
from .twitter import update_all_users
from .twitter import add_or_update_user
from os import getenv
from dotenv import load_dotenv

load_dotenv()

def create_app():
    """Create and configure an instance of the Flask application"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['ENV'] = getenv('FLASK_ENV')
    DB.init_app(app)

    @app.route('/')
    def root():
        message = "Select users and enter text to compare"
        return render_template('base.html', title='Home',
               users=User.query.all(), message=message)

    @app.route('/user', methods=['POST'])
    @app.route('/user/<name>', methods=['GET'])
    def user(name=None, message=''):
        name = name or request.values['user_name']
        try:
            if request.method == 'POST':
                add_or_update_user(name)
                message = "User {} successfully added!".format(name)
            else:
                message = "Tweets"
            tweets = User.query.filter(User.name == name).one().tweets
        except Exception as e:
            message = "Error adding {}: {}".format(name, e)
            tweets = []
        return render_template('user.html', title=name, tweets=tweets,
                               message=message)

    @app.route('/compare', methods=['POST'])
    def compare(message=''):
        user1, user2 = sorted([request.values['user1'],
                               request.values['user2']])
        if user1 == user2:
            message = 'Cannot compare a user to self, bozo!'
        else:
            prediction = predict_user(user1, user2, request.values['tweet_text'])
            message = '"{}" is more likely to be said by {} than {}'.format(
                request.values['tweet_text'], user1 if prediction[0] else user2,
                user2 if prediction[0] else user1)
            message += ', with ' + str(prediction[1]) + ' percent confidence'
        return render_template('prediction.html', title='Prediction', message=message)

    @app.route('/update')
    def update():
        update_all_users()
        message = 'All tweets updated!'
        return render_template('base.html', title='Home',
                                users=User.query.all(), message=message)

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template('base.html', title='Reset database!')

    @app.route('/banjo')
    def banjo():
        return 'I like <a href="https://banjohangout.org">banjos!'

    @app.route('/debug')
    def debug():
        users=User.query.all()
        uzerz =[]
        tweetz = []
        for user in users:
            uzerz.append(user.name)
            tweets = User.query.filter(User.name==user.name).first().tweets
            for tweet in tweets:
                tweetz.append(tweet.text)
        
        return str(uzerz) + str(tweetz)

    return app
'''
    @app.route('/user/<name>')
    def user(name):
        tweets = User.query.filter(User.name == name).first().tweets
        return render_template('user.html', title=name, tweets=tweets)
'''
