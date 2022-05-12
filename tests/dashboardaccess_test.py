"""dash"""
from flask_login import FlaskLoginClient
from app.db import db
from app.db.models import User

def test_access_dashboard_accepted(application):
    """success for dash"""
    application.test_client_class = FlaskLoginClient
    user = User('iua6@njit.edu', 'testtest', True)
    db.session.add(user)
    db.session.commit()
    assert user.email == 'iua6@njit.edu'
    assert db.session.query(User).count() == 1
    with application.test_client(user=user) as client:
        response = client.get('/dashboard')
        assert b'iua6@njit.edu' in response.data
        assert response.status_code == 200


def test_access_dashboard_denied(application):
    """denied dash"""
    application.test_client_class = FlaskLoginClient
    assert db.session.query(User).count() == 0
    with application.test_client(user = None) as clients:
        # This request already has a user logged in.
        response = clients.get('/dashboard')
        assert response.status_code == 302