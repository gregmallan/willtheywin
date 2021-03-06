import pytest

from src.answer import Answer


@pytest.fixture
def positives_answers():
    return {answer.lower() for answer in Answer.POSITIVE}


@pytest.fixture()
def negative_answers():
    return {answer.lower() for answer in Answer.NEGATIVE}


def test_positive_negative_intersection_is_empty(positives_answers, negative_answers):
    assert not positives_answers.intersection(negative_answers)


def test_negative():
    assert Answer.negative() in Answer.NEGATIVE


def test_positive():
    assert Answer.positive() in Answer.POSITIVE


def test_any():
    answer = Answer.any()
    assert (answer in Answer.POSITIVE or answer in Answer.NEGATIVE)
