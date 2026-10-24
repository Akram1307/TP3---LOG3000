"""Tests for the Flask route and the HTML page, using Flask's test client."""

import re

import pytest

from app import app


@pytest.fixture
def client():
    """Return a Flask test client so requests don't need a running server."""
    app.config["TESTING"] = True
    return app.test_client()


def test_get_shows_calculator(client):
    """GET / returns the calculator page."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Flask Calculator" in response.data


def test_post_shows_result(client):
    """POST / with a valid expression puts the result in the display."""
    response = client.post("/", data={"display": "3+4"})
    assert b'value="7.0"' in response.data


def test_post_shows_error(client):
    """POST / with an invalid expression shows an error instead of crashing."""
    response = client.post("/", data={"display": "5+"})
    assert response.status_code == 200
    assert b"Error:" in response.data


def get_buttons(client):
    """Return a dict {value added to the display: text shown on the button}."""
    html = client.get("/").get_data(as_text=True)
    return dict(re.findall(r"appendToDisplay\('(.)'\)\">(.*?)</button>", html))


def test_digit_buttons_labels(client):
    """Each digit button shows the digit it adds to the display."""
    buttons = get_buttons(client)
    for digit in "0123456789":
        assert buttons[digit] == digit, f"button '{digit}' shows '{buttons[digit]}'"


def test_operator_buttons_labels(client):
    """Each operator button shows the operator it adds to the display."""
    buttons = get_buttons(client)
    for op in "+-*/":
        assert buttons[op] == op, f"button '{op}' shows '{buttons[op]}'"
