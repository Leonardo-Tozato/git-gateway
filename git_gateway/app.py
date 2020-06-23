import logging

from flask import Flask
from flask_restx import Resource, Api
from git_gateway.resources.user import User
from git_gateway.resources.repo import Repo

app = Flask(__name__)
api = Api(app)


@api.errorhandler(Exception)
def handle_internal_server_error(error):
    logging.error(error)
    return {'message': 'Internal Server Error'}, 500


@api.route('/liveness')
class Liveness(Resource):
    def get(self):
        try:
            return {'status': 'OK'}
        except Exception as e:
            logging.error(e)
            return {'status': 'NOK'}, 500


api.add_resource(User, '/users/<string:username>/repos', endpoint='user_ep')
api.add_resource(Repo, '/repos/<string:username>/<string:repo_name>', endpoint='repo_ep')

if __name__ == '__main__':
    app.run(debug=True)
