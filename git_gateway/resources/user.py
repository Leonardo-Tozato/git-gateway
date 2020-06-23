from http import HTTPStatus
from flask_restx import Resource
from git_gateway.services.user import User as UserService


class User(Resource):
    def get(self, username: str):
        repos = UserService.all_repos(username)
        if not repos or not len(repos):
            return {'message': 'Not Found'}, HTTPStatus.NOT_FOUND

        return list(map(lambda r: {
            'source': 'Github',
            'external_id': r.get('id'),
            'name': r.get('name'),
            'html_url': r.get('html_url')
        }, repos))
