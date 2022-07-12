from blog_dhmp.core import views
from django.urls import path

app_name = 'post'

urlpatterns = [
    path('<slug:slug>', views.index, name='detalhe')
]
