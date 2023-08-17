from django.contrib import admin
from .models import Comment, Upvote, Forum, Favorites


# Register your models here.

@admin.register(Forum)
class ForumAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'date_time_of_creation')
    list_filter = ('user', 'date_time_of_creation')
    search_fields = ('title', 'description')
    date_hierarchy = 'date_time_of_creation'
    ordering = ('-date_time_of_creation',)


@admin.register(Favorites)
class FavoritesAdmin(admin.ModelAdmin):
    list_display = ('user', 'to_forum')
    list_filter = ('user', 'to_forum')
    search_fields = ('user__username', 'to_forum__title')
    ordering = ('-id',)


@admin.register(Upvote)
class UpvoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'to_comment')
    list_filter = ('user', 'to_comment')
    search_fields = ('user__username', 'to_comment__content')
    ordering = ('-id',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'to_forum', 'date_time_of_creation', 'content')
    list_filter = ('user', 'to_forum', 'date_time_of_creation')
    search_fields = ('user__username', 'to_forum__title', 'content')
    date_hierarchy = 'date_time_of_creation'
    ordering = ('-date_time_of_creation',)
