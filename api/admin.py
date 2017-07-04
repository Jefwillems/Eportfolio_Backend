from django.contrib import admin

from .models import Post, Comment


# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'date_created')
    date_hierarchy = 'date_created'
    fields = ('post', 'text', 'author', 'date_created', 'isRemoved')


class CommentInline(admin.TabularInline):
    model = Comment
    fields = ('text', 'author', 'date_created', 'isRemoved')
    extra = 0


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_created')
    date_hierarchy = 'date_created'
    fields = ('title', 'text', 'author', 'date_created', 'published')
    inlines = (CommentInline,)


admin.site.register(Post, PostAdmin)
