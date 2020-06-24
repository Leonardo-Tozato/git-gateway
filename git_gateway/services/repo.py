import requests
import logging
from os import environ


class Repo:
    @classmethod
    def repo_details(cls, username, repo_name):
        url = f"{environ.get('GITHUB_SERVICE_URL')}/repos/{username}/{repo_name}"
        try:
            response = requests.get(url)
            if response.ok:
                return response.json()
        except Exception as e:
            logging.error(f"request to source failed: {str(e)}")

        return None
