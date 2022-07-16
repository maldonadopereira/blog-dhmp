from django.shortcuts import render
from blog_dhmp.post.models import Post


# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-criado')
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)
