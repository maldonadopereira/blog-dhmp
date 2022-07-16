from blog_dhmp.post import views
from django.urls import path

app_name = 'post'

urlpatterns = [
    path('<slug:slug>', views.detalhe, name='detalhe'),
]
