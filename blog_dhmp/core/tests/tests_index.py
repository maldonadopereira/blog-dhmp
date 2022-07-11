import pytest
from django.urls import reverse
from blog_dhmp.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    resp = client.get(reverse('core:index'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo():
    pass


def test_title(resp):
    assert_contains(resp, '<title>Blog - Home</title>')
