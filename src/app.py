import logging

from flask import Flask, jsonify, request
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)


@app.errorhandler(404)
def page_not_found(error):
    return jsonify({'message': 'Not found', 'status': 404}), 404


# http://webargs.readthedocs.io/en/latest/framework_support.html#error-handling
@app.errorhandler(422)
def handle_bad_request(error):
    # webargs attaches additional metadata to the `data` attribute
    message = error.description
    data = getattr(error, 'data')
    if data:
        # Get validations from the ValidationError object
        data = data['messages']
    else:
        data = f'{error.name}-{error.description}'

    extra = {
        'request_headers': request.headers.items(),
        'request': request.get_data()
    }
    logging.error("handle_bad_request: {}-{}".format(message, data), extra=extra)
    return jsonify({
        'message': message,
        'errors': data,
    }), 422


@app.errorhandler(Exception)
def handle_internal_server_error(error):
    logging.exception(error)
    return jsonify({'message': str(error)}), 500


@app.route('/liveness')
def liveness():
    try:
        return "OK"
    except Exception as e:
        logging.error(e)
        return "NOK", 500


@app.route('/')
def welcome():
    return 'Welcome to Git Gateway API', 200


if __name__ == '__main__':
    app.run(debug=True)
