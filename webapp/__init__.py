from flask import Flask
from config import DevConfig

from models import db

def create_app(object_name):
    app = Flask(__name__)
    app.config.from_object(object_name)

    db.init_app(app)

    @app.route('/')
    def home():
        return '<h1>Hello World!</h1>'

    #app.register_blueprint(default_blueprint)
    return app

#if __name__ == '__main__':
#    app.run()
