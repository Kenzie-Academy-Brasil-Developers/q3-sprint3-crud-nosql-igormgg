from flask import Flask

def init_app(app: Flask):

    from app.routes.all_routes import all_routes
    all_routes(app)