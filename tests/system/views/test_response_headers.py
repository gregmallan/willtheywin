from flask import url_for

import pytest


@pytest.fixture(params=['root', 'will_they_win', ])
def view_name(request):
    return request.param


@pytest.fixture
def expected_response_headers():
    return {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'True'
    }


@pytest.fixture(params=[
    {'': 'canucks'},
    {'': None},
    {'': ''},
    {'tea': 'canucks'},
    {'team': ''},
    {'team': 'vancouver'},
    {'team': 'raptors'},
])
def query_string_params(request):
    return request.param


@pytest.mark.usefixtures('client_class')
class TestResponseHeaders():

    def test_headers(self, view_name, query_string_params, expected_response_headers):
        response = self.client.get(url_for(view_name, **query_string_params), follow_redirects=True)
        for header, value in expected_response_headers.items():
            assert response.headers[header] == value
