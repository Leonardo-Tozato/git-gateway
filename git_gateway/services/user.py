import requests
import logging
from os import environ


class User:
    @classmethod
    def all_repos(cls, username):
        url = f"{environ.get('GITHUB_SERVICE_URL')}/users/{username}/repos"
        try:
            response = requests.get(url)
            if response.ok:
                return response.json()
        except Exception as e:
            logging.error(f"request to source failed: {str(e)}")

        return None
