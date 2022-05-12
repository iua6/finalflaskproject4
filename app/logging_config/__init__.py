import logging
from logging.config import dictConfig

import flask
from flask import request, current_app
from werkzeug.wrappers import response

from app.logging_config.log_formatters import RequestFormatter
from app import config

import os
import datetime

log_con = flask.Blueprint('log_con', __name__)


@log_con.before_app_request
def before_request_logging():
    current_app.logger.info("Before Request")
    log = logging.getLogger("myApp")
    log.info(f"The Bank Logger activated at {datetime.datetime.now()}")



@log_con.after_app_request
def before_request_logging(response):
    if request.path == '/favicon.ico':
        return response
    elif request.path.startswith('/static'):
        return response
    elif request.path.startswith('/bootstrap'):
        return response

    current_app.logger.info("After Request")
    log = logging.getLogger("myApp")
    log.info(f"The Bank Logger activated at {datetime.datetime.now()}")

    log = logging.getLogger("request")
    log.info(f"My request logger has been activated at {datetime.datetime.now()}")

    log = logging.getLogger("random")
    log.debug(f"My random logger has been activated at {datetime.datetime.now()}")

    return response

@log_con.before_app_first_request
def setup_logs():

    ## set the name of the apps log folder to logs
    logdir = config.Config.LOG_DIR
    # make a directory if it doesn't exist
    if not os.path.exists(logdir):
        os.mkdir(logdir)
    logging.config.dictConfig(LOGGING_CONFIG)


    log = logging.getLogger("myApp")
    log.info("The Bank Logger")

    current_app.logger.info("myerrors logger has been activated")
    log = logging.getLogger("myerrors")
    log.error("Not working")

    log = logging.getLogger("debug")
    log.debug("Logger for debug")



LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
        'RequestFormatter': {
            '()': 'app.logging_config.log_formatters.RequestFormatter',
            'format': '[%(asctime)s] [%(process)d] %(remote_addr)s requested %(url)s [%(levelname)s] in %(module)s: %(message)s'
        }

    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',  # Default is stderr
        },
        'file.handler': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': os.path.join(config.Config.LOG_DIR,'handler.log'),
            'maxBytes': 10000000,
            'backupCount': 5,
        },
        'file.handler.myapp': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': os.path.join(config.Config.LOG_DIR,'myapp.log'),
            'maxBytes': 10000000,
            'backupCount': 5,
        },
        'file.handler.response': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': os.path.join(config.Config.LOG_DIR,'response.log'),
            'maxBytes': 10000000,
            'backupCount': 5,
        },
        'file.handler.request': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': os.path.join(config.Config.LOG_DIR,'request.log'),
            'maxBytes': 10000000,
            'backupCount': 5,
        },
        'file.handler.errors': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': os.path.join(config.Config.LOG_DIR,'errors.log'),
            'maxBytes': 10000000,
            'backupCount': 5,
        },
        'file.handler.sqlalchemy': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': os.path.join(config.Config.LOG_DIR,'sqlalchemy.log'),
            'maxBytes': 10000000,
            'backupCount': 5,
        },
        'file.handler.werkzeug': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': os.path.join(config.Config.LOG_DIR,'werkzeug.log'),
            'maxBytes': 10000000,
            'backupCount': 5,
        },
        'file.handler.updatecsv': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': os.path.join(config.Config.LOG_DIR, 'updatecsv.log'),
            'maxBytes': 10000000,
            'backupCount': 5,
        },
        'file.handler.random': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': os.path.join(config.Config.LOG_DIR,'random.log'),
            'maxBytes': 10000000,
            'backupCount': 5,
        },
        'file.handler.debug': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': os.path.join(config.Config.LOG_DIR,'debug.log'),
            'maxBytes': 10000000,
            'backupCount': 5,
        },
        'file.handler.flask': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': os.path.join(config.Config.LOG_DIR,'flask.log'),
            'maxBytes': 10000000,
            'backupCount': 5,
        },

    },
    'loggers': {
        '': {  # root logger
            'handlers': ['default','file.handler'],
            'level': 'DEBUG',
            'propagate': True
        },
        '__main__': {  # if __name__ == '__main__'
            'handlers': ['default','file.handler'],
            'level': 'DEBUG',
            'propagate': True
        },
        'werkzeug': {  # if __name__ == '__main__'
            'handlers': ['file.handler.werkzeug'],
            'level': 'DEBUG',
            'propagate': False
        },
        'sqlalchemy.engine': {  # if __name__ == '__main__'
            'handlers': ['file.handler.sqlalchemy'],
            'level': 'INFO',
            'propagate': False
        },
        'myApp': {  # if __name__ == '__main__'
            'handlers': ['file.handler.myapp'],
            'level': 'DEBUG',
            'propagate': False
        },
        'request': {  # if __name__ == '__main__'
            'handlers': ['file.handler.request'],
            'level': 'DEBUG',
            'propagate': False
        },
        'myerrors': {  # if __name__ == '__main__'
            'handlers': ['file.handler.errors'],
            'level': 'DEBUG',
            'propagate': False
        },
        'random': {  # if __name__ == '__main__'
            'handlers': ['file.handler.errors'],
            'level': 'DEBUG',
            'propagate': False
        },
        'debug': {  # if __name__ == '__main__'
            'handlers': ['file.handler.errors'],
            'level': 'DEBUG',
            'propagate': False
        },
        'flask': {  # if __name__ == '__main__'
            'handlers': ['file.handler.flask'],
            'level': 'DEBUG',
            'propagate': False
        },
        'updatecsv': {  # if __name__ == '__main__'
            'handlers': ['file.handler.updatecsv'],
            'level': 'DEBUG',
            'propagate': False
        },

    }
}
