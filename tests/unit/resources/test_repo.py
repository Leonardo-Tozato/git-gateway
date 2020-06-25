from http import HTTPStatus

from git_gateway.resources.repo import Repo

class TestRepo:
    def test_get(self, mocker):
        mocker.patch('git_gateway.resources.repo.flask_cache.get', return_value=None)
        mocker.patch('git_gateway.resources.repo.flask_cache.set', return_value=None)
        stub = mocker.patch('git_gateway.services.repo.Repo.repo_details', return_value={
            "id": 271649307,
            "name": "challenge",
            "html_url": "https://github.com/zikamemo/challenge",
            "description": None,
            "fork": True,
            "pushed_at": "2020-06-25T01:45:56Z",
            "git_url": "git://github.com/zikamemo/challenge",
            "ssh_url": "git@github.com:victorabarros/challenge-olist.git",
            "language": "Go",
            "has_issues": False,
            "has_projects": True,
            "has_downloads": True,
            "has_wiki": True,
            "has_pages": False
        })
        mocker.patch('git_gateway.resources.repo.Repo.send_repo_detail_db', return_value=None)

        repoResource = Repo()
        results = repoResource.get('zikamemo', 'challenge')
        stub.assert_called_once_with('zikamemo', 'challenge')
        assert results == {
            "source": "Github",
            "external_id": 271649307,
            "name": "challenge",
            "html_url": "https://github.com/zikamemo/challenge",
            "description": None,
            "fork": True,
            "pushed_at": "2020-06-25T01:45:56Z",
            "git_url": "git://github.com/zikamemo/challenge",
            "ssh_url": "git@github.com:victorabarros/challenge-olist.git",
            "language": "Go",
            "has_issues": False,
            "has_projects": True,
            "has_downloads": True,
            "has_wiki": True,
            "has_pages": False
        }

    def test_get_not_found(self, mocker):
        mocker.patch('git_gateway.resources.repo.flask_cache.get', return_value=None)
        mocker.patch('git_gateway.services.repo.Repo.repo_details', return_value=None)
        repoResource = Repo()
        results = repoResource.get('zikamemo', 'challenge')
        assert results == ({'message': 'Not Found'}, HTTPStatus.NOT_FOUND)