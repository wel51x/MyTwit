from flask import Flask

def create_app():
    """Create and configure an instance of the Flask application"""
    app = Flask(__name__)

    @app.route('/')
    def root():
        return "Hello, MyTwit!"

    @app.route('/banjo')
    def banjo():
        return 'I like <a href="https://banjohangout.org">banjos!'

    return app
