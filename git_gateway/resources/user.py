from http import HTTPStatus
from flask_restx import Resource
from git_gateway.services.user import User as UserService
from git_gateway.lib.cache import flask_cache


class User(Resource):
    def get(self, username: str):
        cache_key = f"user::repos::{username}"
        response = flask_cache.get(cache_key)

        if response:
            return response

        repos = UserService.all_repos(username)
        if not repos or not len(repos):
            return {'message': 'Not Found'}, HTTPStatus.NOT_FOUND

        response = list(map(lambda r: {
            'source': 'Github',
            'external_id': r.get('id'),
            'name': r.get('name'),
            'html_url': r.get('html_url')
        }, repos))
        flask_cache.set(cache_key, response, 60)
        return response
