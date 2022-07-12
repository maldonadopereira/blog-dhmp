from django.contrib.admin import ModelAdmin, register
from blog_dhmp.post.models import Post


@register(Post)
class PostAdmin(ModelAdmin):
    list_display = ('id', 'titulo', 'slug', 'criado')
    list_display_links = ('titulo',)
    ordering = ('criado',)
    prepopulated_fields = {'slug': ('titulo',)}
