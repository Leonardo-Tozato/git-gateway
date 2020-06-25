from http import HTTPStatus

from git_gateway.resources.user import User


class TestUser:
    def test_get(self, mocker):
        mocker.patch('git_gateway.resources.user.flask_cache.get', return_value=None)
        mocker.patch('git_gateway.resources.user.flask_cache.set', return_value=None)
        stub = mocker.patch('git_gateway.services.user.User.all_repos', return_value=[{
            "id": 222693271,
            "name": "challenge",
            "html_url": "https://github.com/zikamemo/challenge"
        }])
        mocker.patch('git_gateway.resources.user.User.send_repos_db', return_value=None)

        userResource = User()
        results = userResource.get('zikamemo')
        stub.assert_called_once_with('zikamemo')
        assert results == [{
            "source": "Github",
            "external_id": 222693271,
            "name": "challenge",
            "html_url": "https://github.com/zikamemo/challenge"
        }]

    def test_get_not_found(self, mocker):
        mocker.patch('git_gateway.resources.user.flask_cache.get', return_value=None)
        stub = mocker.patch('git_gateway.services.user.User.all_repos', return_value=None)
        userResource = User()
        results = userResource.get('zikamemo')
        stub.assert_called_once_with('zikamemo')
        assert results == ({'message': 'Not Found'}, HTTPStatus.NOT_FOUND)
