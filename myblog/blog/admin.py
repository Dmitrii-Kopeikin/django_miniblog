from django.contrib import admin
from .models import Publication
from .models import Comment


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):

    list_display = ('title', 'author')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'publication')
