from flask import url_for, request

import pytest


@pytest.mark.usefixtures('client_class')
class TestRootMethodNotAllowed():
    VIEW_NAME = 'root'

    @pytest.mark.parametrize('method_name', ['post', 'put', 'delete', 'patch'])
    def test_status_405(self, method_name):
        client_callable_request_method = getattr(self.client, method_name)
        assert client_callable_request_method(url_for(self.VIEW_NAME)).status_code == 405


@pytest.mark.usefixtures('client_class')
class TestRoot():
    VIEW_NAME = 'root'
    WILL_THEY_WIN_VIEW_NAME = 'will_they_win'

    def test_no_follow_status_code_302(self):
        assert self.client.get(url_for(self.VIEW_NAME)).status_code == 302

    def test_follow_redirects_status_code_200(self):
        assert self.client.get(url_for(self.VIEW_NAME), follow_redirects=True).status_code == 200

    def test_follow_redirects_to_will_they_win(self):
        self.client.get(url_for(self.VIEW_NAME), follow_redirects=True)
        assert request.path == url_for(self.WILL_THEY_WIN_VIEW_NAME)

    def test_follow_redirects_json(self):
        response = self.client.get(url_for(self.VIEW_NAME), follow_redirects=True)
        assert response.get_json()

    @pytest.mark.parametrize('team_name_dict', [
        {'': None},
        {'': ''},
        {'wrong_key': None},
        {'wrong_key': ''},
        {'TEAM': None},
        {'TEAM': ''},
        {'team': None},
        {'team': ''},
        {'tea': 'canucks'},
        {'eam': 'canucks'},
        {'TEAM': 'canucks'},
        {'TEAM': 'vancouver'},
    ])
    def test_redirects_with_invalid_key_or_missing_team(self, team_name_dict):
        response = self.client.get(url_for(self.VIEW_NAME, **team_name_dict), follow_redirects=True)
        assert response.get_json()['status'] == 'error'
        assert response.get_json()['error_message'] == 'missing team'

    @pytest.mark.parametrize('team_name_dict', [
        {'team': 'canucks'},
        {'team': 'raptors'},
        {'team': 'jets'},
        {'team': 'winnipeg'},
    ])
    def test_redirects_with_team(self, team_name_dict):
        response = self.client.get(url_for(self.VIEW_NAME, **team_name_dict), follow_redirects=True)
        assert response.get_json()['status'] == 'ok'
        assert response.get_json()['team'] == team_name_dict['team']
        assert 'answer' in response.get_json()
