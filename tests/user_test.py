"""user test"""
#importing
import logging

from app import db
from app.db.models import User, transaction


def test_adding_user(application):
    """adding user"""
    log = logging.getLogger("myApp")
    with application.app_context():
        assert db.session.query(User).count() == 0
        assert db.session.query(transaction).count() == 0
        #showing how to add a record
        #create a record
        user = User('iua6@njit.edu', 'testtest')
        #add it to get ready to be committed
        db.session.add(user)
        #call the commit
        #db.session.commit()
        #assert that we now have a new user
        #assert db.session.query(User).count() == 1
        #finding one user record by email
        user = User.query.filter_by(email='iua6@njit.edu').first()
        log.info(user)
        #asserting that the user retrieved is correct
        assert user.email == 'iua6@njit.edu'
        #this is how you get a related record ready for insert
        user.transactions= [transaction("test","smap", "trr", "2020"),
                     transaction("test2","te", "dsfns", "1999"),
                     transaction("test","smap", "dadsa", "1984"),
                     transaction("test","smap", "dadsa", "1984")]
        #commit is what saves the transactions
        db.session.commit()
        assert db.session.query(transaction).count() == 4
        transaction1 = transaction.query.filter_by(title='test').first()
        assert transaction1.title == "test"
        #changing the title of the transaction
        transaction1.title = "SupertransactionTitle"
        #saving the new title of the transaction
        db.session.commit()
        transaction2 = transaction.query.filter_by(title='SupertransactionTitle').first()
        assert transaction2.title == "SupertransactionTitle"
        #checking cascade delete
        db.session.delete(user)
        assert db.session.query(User).count() == 0
        assert db.session.query(transaction).count() == 0
