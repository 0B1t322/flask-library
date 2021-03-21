import os

base_dir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@127.0.0.1/library?unix_socket=/var/run/mysqld/mysqld.sock'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CSS_BASE_PATH = 'static/css'
