from flask_restx import Resource


class User(Resource):
    def get(self, username: str):
        return {'test': username}
