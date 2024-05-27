from flask import Flask

from . import match, search


def create_app(): #start of the app
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "Hello World!"

    app.register_blueprint(match.bp) #use to organize routes into separate modules
    app.register_blueprint(search.bp) #use to organize routes into separate modules

    return app
