from flask import Flask

from .views import posts as posts_view

def create_app():

    app = Flask(__name__, static_folder=None)
    posts_view.init_app(app)

    return app