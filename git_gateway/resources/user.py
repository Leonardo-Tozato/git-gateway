from http import HTTPStatus
from git_gateway.services.user import User as UserService
from git_gateway.utils.cache import flask_cache
from git_gateway.utils.db import mongo_client
from os import environ
from flask_restx import Resource

db = mongo_client[environ.get('MONGO_DATABASE')]
user_repos = db['user_repos']

class User(Resource):
    def get(self, username: str):
        cache_key = f"user::repos::{username}"
        response = flask_cache.get(cache_key)

        if response:
            return response

        repos = UserService.all_repos(username)

        if not repos or not len(repos):
            return {'message': 'Not Found'}, HTTPStatus.NOT_FOUND

        self.send_repos_db(repos, username)
        response = list(map(lambda r: {
            'source': 'Github',
            'external_id': r.get('id'),
            'name': r.get('name'),
            'html_url': r.get('html_url')
        }, repos))
        flask_cache.set(cache_key, response, 60)
        return response

    def send_repos_db(self, repos, username):
        user_repos.replace_one({'owner_username': username}, {
            'owner_username': username,
            'repos': repos
        }, upsert=True)
