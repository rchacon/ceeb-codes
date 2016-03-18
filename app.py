from flask import abort, Flask, g, jsonify, request
from flasgger import Swagger
from flasgger.utils import swag_from

from settings import get_mongo_client


app = Flask(__name__)

Swagger(app)


def get_db():
    mongo = getattr(g, '_database', None)
    if mongo is None:
        mongo = g._database = get_mongo_client()
    db = mongo.get_default_database()
    return db


@app.teardown_appcontext
def teardown_mongo(exception):
    mongo = getattr(g, '_database', None)
    if mongo is not None:
        mongo.close()


@app.errorhandler(500)
def server_error(e):
    resp = jsonify({'error': str(e)})
    resp.status_code = 500

    return resp


@app.errorhandler(400)
def bad_request(e):
    resp = jsonify({'error': str(e)})
    resp.status_code = 400

    return resp


@app.route('/api/highschools', methods=['GET'])
@swag_from('swagger/highschools.yml')
def get_highschools():
    state = request.args.get('state')
    city = request.args.get('city')

    if state is None or city is None:
        abort(400)

    highschools = get_schools('highschools', state, city)

    return jsonify({'results': highschools, 'count': len(highschools)})


@app.route('/api/colleges', methods=['GET'])
@swag_from('swagger/colleges.yml')
def get_colleges():
    state = request.args.get('state')
    city = request.args.get('city')

    if state is None or city is None:
        abort(400)

    colleges = get_schools('colleges', state, city)

    return jsonify({'results': colleges, 'count': len(colleges)})


def get_schools(endpoint, state, city):
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
    db = get_db()
    collection = getattr(db, endpoint)
    cursor = collection.find(predicate, projection)
    schools = list(cursor)

    return schools


if __name__ == '__main__':
    app.run(debug=True)
