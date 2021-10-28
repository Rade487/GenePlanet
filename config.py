from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    """Set Flask configuration from .env file."""

    FLASK_APP = environ.get('FLASK_APP')
    # Database
    SQLALCHEMY_DATABASE_URI = 'postgresql://newuser:pass@localhost/postgres'  # environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
