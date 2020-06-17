from flask import Flask
from info.modules.index import index_blu
from info.modules.passport import passport


def url_app():
    app = Flask(__name__)
    app.register_blueprint(index_blu)
    app.register_blueprint(passport)
    return app
