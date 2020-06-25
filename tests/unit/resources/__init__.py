from git_gateway.services.user import User


class TestUser:
    def test_all_repos(self, requests_mock):
        requests_mock.get(f"https://api.github.com/users/zikamemo/repos", json=[{'name': 'Zika Repository'}])
        response = User.all_repos('zikamemo')
        assert response == [{'name': 'Zika Repository'}]

    def test_all_repos_None(self, requests_mock):
        requests_mock.get(f"https://api.github.com/users/zikamemo/repos", status_code=404)
        response = User.all_repos('zikamemo')
        assert response is None
