import os

from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from ddtrace import patch_all
from os import environ

db = SQLAlchemy()


def init_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    # app.config.from_pyfile('config.py')
    app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://newuser:pass@localhost/postgres'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    with app.app_context():
        import routes
        return app


app = init_app()
if __name__ == "__main__":
    app.run()
