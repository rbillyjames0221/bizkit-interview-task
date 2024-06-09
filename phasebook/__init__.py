from flask import Flask

from . import match, search, add_user, update_user, delete_user


def create_app(): #start of the app
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "Hello World!"

    app.register_blueprint(match.bp) #use to organize routes into separate modules
    app.register_blueprint(search.bp) 
    app.register_blueprint(add_user.bp) 
    app.register_blueprint(update_user.bp) 
    app.register_blueprint(delete_user.bp)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)