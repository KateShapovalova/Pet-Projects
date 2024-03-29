import os.path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config
import logging
from logging.handlers import RotatingFileHandler
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_babel import Babel, lazy_gettext as _l
from flask import request

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
login.login_message = _l("Please log in to access this page.")
bootstrap = Bootstrap(app)
moment = Moment(app)
babel = Babel(app)

from app import routes, models, errors

# if not app.debug:
#     os.makedirs('logs', exist_ok=True)
#     file_handler = RotatingFileHandler('logs/chat.log', maxBytes=10240, backupCount=10)
#     file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
#     file_handler.setLevel(logging.INFO)
#     app.logger.addHandler(file_handler)
#     app.logger.setLevel(logging.INFO)
#     app.logger.info('Chat startup')


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])
