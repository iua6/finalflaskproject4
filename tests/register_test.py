"""testing the registration"""
import logging
from app.auth.forms import login_form, register_form

def test_user_login(application):
    """sign in"""
    log = logging.getLogger("myApp")
    log.info("user login test")
    with application.test_request_context():
        form = login_form()
        form.email.data = "iua6@njit.edu"
        form.password.data = "testtest"
        assert form.validate


def test_user_register(application):
    """sign up"""
    log = logging.getLogger("myApp")
    log.info("user register test")
    with application.test_request_context():
        form = register_form()
        form.email.data = "iua6@njit.edu"
        form.password.data = "testtest"
        form.confirm.data = "testtest"
        assert form.validate