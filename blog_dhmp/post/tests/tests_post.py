import pytest
from django.urls import reverse
from blog_dhmp.django_assertions import assert_contains
from blog_dhmp.post.models import Post
from model_mommy import mommy


@pytest.fixture()
def post(db):
    return mommy.make(Post)


@pytest.fixture
def resp(client, post):
    resp = client.get(reverse('post:detalhe', kwargs={'slug': post.slug}))
    return resp


def test_title(resp, post: Post):
    assert_contains(resp, f'<title>{post.titulo}</title>')


def test_titulo_do_post(resp, post: Post):
    titulo = post.titulo
    titulo.capitalize()
    assert_contains(resp, f'<h1>{titulo}</h1>')


def test_subtitulo_do_post(resp, post: Post):
    assert_contains(resp, f'<h1>{post.titulo}</h1>')
