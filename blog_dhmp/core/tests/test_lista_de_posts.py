import pytest
from django.urls import reverse
from blog_dhmp.django_assertions import assert_contains
from blog_dhmp.post.models import Post
from model_mommy import mommy
from typing import List


@pytest.fixture()
def posts(db):
    return mommy.make(Post, 5)


@pytest.fixture()
def resp(client, posts):
    resp = client.get(reverse('core:index'))
    return resp


def test_titulo_dos_posts(resp, posts: List[Post]):
    for post in posts:
        assert_contains(resp, post.titulo)


def test_subtitulo_dos_posts(resp, posts: List[Post]):
    for post in posts:
        assert_contains(resp, post.subtitulo)


def test_link_dos_posts(resp, posts):
    for post in posts:
        assert_contains(resp, post.get_absolute_url())


def test_criador_dos_posts(resp, posts: List[Post]):
    for post in posts:
        assert_contains(resp, post.usuario)
