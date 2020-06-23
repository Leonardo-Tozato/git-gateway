from flask_restx import Resource


class Repo(Resource):
    def get(self, username: str, repo_name: str):
        return {'test': repo_name}

