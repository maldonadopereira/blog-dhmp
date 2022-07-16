import pytest
from django.urls import reverse
from blog_dhmp.django_assertions import assert_contains


@pytest.fixture
def resp(client, db):
    resp = client.get(reverse('core:index'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, '<title>Blog - Home</title>')


def test_link_home(resp):
    assert_contains(resp, f'href="{reverse("core:index")}">Home</a>')
