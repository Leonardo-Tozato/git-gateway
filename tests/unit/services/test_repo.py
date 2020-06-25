from git_gateway.services.repo import Repo


class TestRepo:
    def test_repo_details(self, requests_mock):
        requests_mock.get(f"https://api.github.com/repos/zikamemo/challenge", json={'name': 'Zika Repository'})
        response = Repo.repo_details('zikamemo', 'challenge')
        assert response == {'name': 'Zika Repository'}

    def test_repo_details_none(self, requests_mock):
        requests_mock.get(f"https://api.github.com/repos/zikamemo/challenge", status_code=404)
        response = Repo.repo_details('zikamemo', 'challenge')
        assert response is None
