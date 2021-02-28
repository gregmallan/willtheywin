import pytest

from src.api import app as flask_app


def pytest_report_header(config):
    return ["PROJECT: willtheywin", ]


@pytest.fixture
def app():
    return flask_app
