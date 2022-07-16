from django.db import models
from blog_dhmp.core.models import Base
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Post(Base):
    titulo = models.CharField('Titulo', max_length=64)
    subtitulo = models.CharField('Subtitulo', max_length=128)
    texto = models.TextField('Texto')
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    slug = models.SlugField(unique=True)
    imagem = models.ImageField(upload_to='fotos/%d/%m/%Y', blank=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('post:detalhe', args=(self.slug,))
