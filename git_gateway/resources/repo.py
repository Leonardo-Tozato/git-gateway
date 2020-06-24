from flask_restx import Resource
from http import HTTPStatus
from git_gateway.services.repo import Repo as RepoService


class Repo(Resource):
    def get(self, username: str, repo_name: str):
        repo_details = RepoService.repo_details(username, repo_name)
        if not repo_details:
            return {'message': 'Not Found'}, HTTPStatus.NOT_FOUND

        return {
            'source': 'Github',
            'external_id': repo_details.get('id'),
            'name': repo_details.get('name'),
            'html_url': repo_details.get('html_url'),
            'description': repo_details.get('description'),
            'fork': repo_details.get('fork'),
            'pushed_at': repo_details.get('pushed_at'),
            'git_url': repo_details.get('git_url'),
            'ssh_url': repo_details.get('pushed_at'),
            'language': repo_details.get('language'),
            'has_issues': repo_details.get('has_issues'),
            'has_project': repo_details.get('has_projects'),
            'has_downloads': repo_details.get('has_downloads'),
            'has_wiki': repo_details.get('has_wiki'),
            'has_pages': repo_details.get('has_pages')
        }
