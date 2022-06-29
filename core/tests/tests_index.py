import pytest
from django.urls import reverse
# from blog_dhmp.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    resp = client.get(reverse('core:index'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200