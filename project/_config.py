import os

#grab the folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
WTF_CSRF_ENABLED = True
DEBUG = False
SECRET_KEY = 'sdfjgjsdfsfgdsfsdfgdgdfghdsfgsdfgdsfgsdgfsdfgsdfsdfwefewfdsfwefds'
DATABASE_PATH = os.path.join(basedir, DATABASE)

SQLALCHEMY_DATABASE_URI= 'sqlite:///' + DATABASE_PATH