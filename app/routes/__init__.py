from flask import Flask

def init_app(app: Flask):

    from app.routes.home_route import all_routes
    all_routes(app)