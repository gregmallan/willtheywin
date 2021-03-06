from flask import url_for

import pytest

from src.answer import Answer


@pytest.fixture(params=[
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
def invalid_query_str_params_dict(request):
    return request.param


@pytest.fixture(params=[
    {'team': 'canucks'},
    {'team': 'vancouver'},
    {'team': 'raptors'},
    {'team': 'jets'},
    {'team': 'winnipeg'},
])
def valid_query_str_params_dict(request):
    return request.param


@pytest.mark.usefixtures('client_class')
class TestWillTheyWinMethodNotAllowed():
    VIEW_NAME = 'will_they_win'

    @pytest.mark.parametrize('method_name', ['post', 'put', 'delete', 'patch'])
    def test_status_405(self, method_name):
        client_callable_request_method = getattr(self.client, method_name)
        assert client_callable_request_method(url_for(self.VIEW_NAME)).status_code == 405


@pytest.mark.usefixtures('client_class')
class TestWillTheyWinNoTeam():
    VIEW_NAME = 'will_they_win'

    def test_status_code_200(self):
        assert self.client.get(url_for(self.VIEW_NAME)).status_code == 200

    def test_response_is_json(self):
        response = self.client.get(url_for(self.VIEW_NAME))
        assert response.is_json

    def test_response_get_json(self):
        response = self.client.get(url_for(self.VIEW_NAME))
        assert response.get_json()

    def test_status_error_in_json_response(self):
        response = self.client.get(url_for(self.VIEW_NAME))
        assert response.get_json()['status'] == 'error'

    def test_error_message(self):
        response = self.client.get(url_for(self.VIEW_NAME))
        assert response.get_json()['error_message'] == 'missing team'


@pytest.mark.usefixtures('client_class')
class TestWillTheyWinInvalidTeamQueryParam():
    VIEW_NAME = 'will_they_win'

    def test_status_code_200(self, invalid_query_str_params_dict):
        assert self.client.get(url_for(self.VIEW_NAME, **invalid_query_str_params_dict)).status_code == 200

    def test_response_get_json(self, invalid_query_str_params_dict):
        response = self.client.get(url_for(self.VIEW_NAME, **invalid_query_str_params_dict))
        assert response.get_json()

    def test_status_error_in_json_response(self, invalid_query_str_params_dict):
        response = self.client.get(url_for(self.VIEW_NAME, **invalid_query_str_params_dict))
        assert response.get_json()['status'] == 'error'

    def test_error_message(self, invalid_query_str_params_dict):
        response = self.client.get(url_for(self.VIEW_NAME, **invalid_query_str_params_dict))
        assert response.get_json()['error_message'] == 'missing team'


@pytest.mark.usefixtures('client_class')
class TestWillTheyWinWithNameParam():
    VIEW_NAME = 'will_they_win'

    def test_status_code_200(self, valid_query_str_params_dict):
        assert self.client.get(url_for(self.VIEW_NAME, **valid_query_str_params_dict)).status_code == 200

    def test_response_is_json(self, valid_query_str_params_dict):
        response = self.client.get(url_for(self.VIEW_NAME, **valid_query_str_params_dict))
        assert response.is_json

    def test_response_get_json(self, valid_query_str_params_dict):
        response = self.client.get(url_for(self.VIEW_NAME, **valid_query_str_params_dict))
        assert response.get_json()

    def test_status_ok_in_json_response(self, valid_query_str_params_dict):
        response = self.client.get(url_for(self.VIEW_NAME, **valid_query_str_params_dict))
        assert response.get_json()['status'] == 'ok'

    def test_no_error_message_in_json_response(self, valid_query_str_params_dict):
        response = self.client.get(url_for(self.VIEW_NAME, **valid_query_str_params_dict))
        assert 'error_message' not in response.get_json()

    def test_team_in_json_response(self, valid_query_str_params_dict):
        response = self.client.get(url_for(self.VIEW_NAME, **valid_query_str_params_dict))
        assert response.get_json()['team'] == valid_query_str_params_dict['team']

    def test_answer_is_negative(self, valid_query_str_params_dict):
        response = self.client.get(url_for(self.VIEW_NAME, **valid_query_str_params_dict))
        assert response.get_json()['answer'] in Answer.NEGATIVE
