"""Main appl and routing logic for MyTwit."""
from flask import Flask, render_template
from .models import DB, User
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
        return render_template('base.html', title='Home', users=User.query.all())

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template('base.html', title='Reset database!')

    @app.route('/banjo')
    def banjo():
        return 'I like <a href="https://banjohangout.org">banjos!'

    return app
