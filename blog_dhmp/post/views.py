from django.shortcuts import render
from blog_dhmp.post.models import Post


# Create your views here.
def detalhe(request, slug):
    post = Post.objects.get(slug=slug)
    contexto = {
        'post': post
    }
    return render(request, 'post.html', contexto)
