from flask_restx import Resource
from http import HTTPStatus
from git_gateway.services.repo import Repo as RepoService
from git_gateway.lib.cache import flask_cache
from git_gateway.lib.db import mongo_client
from os import environ

db = mongo_client[environ.get('MONGO_DATABASE')]
repositories = db['repositories']

class Repo(Resource):
    def get(self, username: str, repo_name: str):
        cache_key = f"repos::{username}::{repo_name}"
        response = flask_cache.get(cache_key)

        if response:
            return response

        repo_details = RepoService.repo_details(username, repo_name)
        if not repo_details:
            return {'message': 'Not Found'}, HTTPStatus.NOT_FOUND

        self.send_repo_detail_db(repo_details)

        response = {
            'source': 'Github',
            'external_id': repo_details.get('id'),
            'name': repo_details.get('name'),
            'html_url': repo_details.get('html_url'),
            'description': repo_details.get('description'),
            'fork': repo_details.get('fork'),
            'pushed_at': repo_details.get('pushed_at'),
            'git_url': repo_details.get('git_url'),
            'ssh_url': repo_details.get('ssh_url'),
            'language': repo_details.get('language'),
            'has_issues': repo_details.get('has_issues'),
            'has_projects': repo_details.get('has_projects'),
            'has_downloads': repo_details.get('has_downloads'),
            'has_wiki': repo_details.get('has_wiki'),
            'has_pages': repo_details.get('has_pages')
        }

        flask_cache.set(cache_key, response, 60)
        return response

    def send_repo_detail_db(self, repo_details):
        repo_full_name = repo_details.get('full_name')
        repositories.replace_one({'full_name': repo_full_name}, {
            'full_name': repo_full_name,
            'repository': repo_details
        }, upsert=True)
