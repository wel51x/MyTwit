"""Main appl and routing logic for MyTwit."""
from flask import Flask
from .models import DB

def create_app():
    """Create and configure an instance of the Flask application"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    DB.init_app(app)

    @app.route('/')
    def root():
        return "Hello, MyTwit!"

    @app.route('/banjo')
    def banjo():
        return 'I like <a href="https://banjohangout.org">banjos!'

    return app
