from django.contrib import admin
from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Meta:
        model = Post
        fields = '__all__'
