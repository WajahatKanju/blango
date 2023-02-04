from django.contrib import admin

from blog.models import Tag, Post, Comment

class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}
  list_display = ('slug', 'author', 'published_at')
  

admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Post, PostAdmin)
