import os
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    
    SQLALCHEMY_DATABASE_URI= os.environ.get('DATABASE_URL') or 'postgresql://postgres:test123@localhost/microblog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.googlemail.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') or 1
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'sasukembtest@gmail.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'dattebayo'
    ADMINS = ['sasukembtest@gmail.com']


    POSTS_PER_PAGE = 6

    LANGUAGES = ['en','es']