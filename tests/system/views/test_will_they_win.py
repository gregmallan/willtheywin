from flask import url_for, request

import pytest

from src.answer import Answer


@pytest.mark.usefixtures('client_class')
class TestWillTheyWinMethodNotAllowed():
    VIEW_NAME = 'will_they_win'

    @pytest.mark.parametrize('method_name', ['post', 'put', 'delete', 'patch'])
    def test_status_405(self, method_name):
        client_callable_request_method = getattr(self.client, method_name)
        assert client_callable_request_method(url_for(self.VIEW_NAME)).status_code == 405


@pytest.mark.usefixtures('client_class')
class TestWillTheyWin():
    VIEW_NAME = 'will_they_win'

    def test_status_code_200(self):
        assert self.client.get(url_for(self.VIEW_NAME)).status_code == 200

    def test_response_is_json(self):
        response = self.client.get(url_for(self.VIEW_NAME))
        assert response.is_json

    def test_response_get_json(self):
        response = self.client.get(url_for(self.VIEW_NAME))
        assert response.get_json()

    def test_answer_in_json_response(self):
        response = self.client.get(url_for(self.VIEW_NAME))
        assert 'answer' in response.get_json()

    def test_answer_is_negative(self):
        response = self.client.get(url_for(self.VIEW_NAME))
        assert response.get_json()['answer'] in Answer.NEGATIVE
