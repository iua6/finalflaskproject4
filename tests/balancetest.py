"""this is the BALANCE test"""
from flask_login import FlaskLoginClient
from app import db
from app.db.models import User


def test_balance_calculate(application):
    """calculating"""
    application.test_client_class = FlaskLoginClient
    user = User('iua6@njit.edu', 'testtest', is_admin=True)
    db.session.add(user)
    db.session.commit()

    assert user.email == 'keith@webizly.com'
    assert user.balance == 0.00 # Default balance

    user.balance += 5.67
    assert user.balance == 5.67

    user.balance -= 1.00
    assert user.balance == 4.67