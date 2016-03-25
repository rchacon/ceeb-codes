import os

from flask import g
from pymongo import MongoClient


class Mongo(object):
    def __init__(self, app):
        app.teardown_appcontext(self.teardown)

    def teardown(self, exception):
        mongo = getattr(g, '_database', None)
        if mongo is not None:
            mongo.close()

    def get_db(self):
        uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017/schools')
        mongo = g._database = MongoClient(uri)
        db = mongo.get_default_database()
        return db

    @property
    def db(self):
        mongo = getattr(g, '_database', None)
        if mongo is None:
            return self.get_db()
        db = mongo.get_default_database()
        return db


def get_schools(session, endpoint, state, city):
    """Get highschools or colleges from mongo."""
    predicate = {
        'address.state': state,
        'address.city': city
    }
    projection = {
        '_id': 0,
        'date_created': 0,
        'date_modified': 0,
        'date_deleted': 0
    }
    db = session.db
    collection = getattr(db, endpoint)
    cursor = collection.find(predicate, projection)
    schools = list(cursor)

    return schools
