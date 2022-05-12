""" Testing log files """
import os


def test_request_log_is_created():
    """Checking request log"""
    root = os.path.dirname(os.path.abspath(__file__))
    requestlog = os.path.join(root, '../logs/request.log')
    #Check whether the request exits, if not create a new one
    if not os.path.exists(requestlog):
        os.mknod(requestlog)
    assert os.path.exists(requestlog) is True


def test_errors_log_is_created():
    """Checking errors log"""
    root = os.path.dirname(os.path.abspath(__file__))
    errorlog = os.path.join(root, '../logs/errors.log')
    # Check whether the request exits, if not create a new one
    if not os.path.exists(errorlog):
        os.mknod(errorlog)
    assert os.path.exists(errorlog) is True


def test_debug_log_is_created():
    """Checking errors log"""
    root = os.path.dirname(os.path.abspath(__file__))
    debuglog = os.path.join(root, '../logs/debug.log')
    # Check whether the request exits, if not create a new one
    if not os.path.exists(debuglog):
        os.mknod(debuglog)
    assert os.path.exists(debuglog) is True


def test_flask_log_is_created():
    """Checking errors log"""
    root = os.path.dirname(os.path.abspath(__file__))
    flasklog = os.path.join(root, '../logs/flask.log')
    # Check whether the request exits, if not create a new one
    if not os.path.exists(flasklog):
        os.mknod(flasklog)
    assert os.path.exists(flasklog) is True


def test_random_log_is_created():
    """Checking errors log"""
    root = os.path.dirname(os.path.abspath(__file__))
    randomlog = os.path.join(root, '../logs/random.log')
    # Check whether the request exits, if not create a new one
    if not os.path.exists(randomlog):
        os.mknod(randomlog)
    assert os.path.exists(randomlog) is True


def test_sqlalchemy_log_is_created():
    """Checking errors log"""
    root = os.path.dirname(os.path.abspath(__file__))
    sqlalchemyLog = os.path.join(root, '../logs/sqlalchemy.log')
    # Check whether the request exits, if not create a new one
    if not os.path.exists(sqlalchemyLog):
        os.mknod(sqlalchemyLog)
    assert os.path.exists(sqlalchemyLog) is True


def test_myapp_log_is_created():
    """Checking errors log"""
    root = os.path.dirname(os.path.abspath(__file__))
    myappLog = os.path.join(root, '../logs/myapp.log')
    # Check whether the request exits, if not create a new one
    if not os.path.exists(myappLog):
        os.mknod(myappLog)
    assert os.path.exists(myappLog) is True

def test_update_csv_log_is_created():
    """Checking errors log"""
    root = os.path.dirname(os.path.abspath(__file__))
    myappLog = os.path.join(root, '../logs/updatecsv.log')
    # Check whether the request exits, if not create a new one
    if not os.path.exists(myappLog):
        os.mknod(myappLog)
    assert os.path.exists(myappLog) is True