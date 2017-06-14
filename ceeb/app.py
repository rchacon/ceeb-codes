from flask import abort, Flask, jsonify, request
from flasgger import Swagger
from flasgger.utils import swag_from
from six import iteritems

from .db import Mongo, get_schools
from .settings import STATES


app = Flask(__name__)

mongo = Mongo(app)

Swagger(app)


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


@app.route('/api/states', methods=['GET'])
def get_states():
    states = [{'name': k, 'abbr': v['abbr']} for k, v in iteritems(STATES)]

    return jsonify({'results': states, 'count': len(states)})


@app.route('/api/highschools', methods=['GET'])
@swag_from('swagger/highschools.yml')
def get_highschools():
    state = request.args.get('state')
    city = request.args.get('city')

    if state is None or city is None:
        abort(400)

    highschools = get_schools(mongo, 'highschools', state, city)

    return jsonify({'results': highschools, 'count': len(highschools)})


@app.route('/api/colleges', methods=['GET'])
@swag_from('swagger/colleges.yml')
def get_colleges():
    state = request.args.get('state')
    city = request.args.get('city')

    if state is None or city is None:
        abort(400)

    colleges = get_schools(mongo, 'colleges', state, city)

    return jsonify({'results': colleges, 'count': len(colleges)})


if __name__ == '__main__':
    app.run(debug=True)
