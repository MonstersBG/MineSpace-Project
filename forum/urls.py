from django.urls import path
from .views import home, create_forum, ForumDetailView, add_comment, like_comment, favorite_forum, edit_forum, \
    search_forums

urlpatterns = [
    path("", home, name="home"),
    path("create-forum/", create_forum, name="create_forum"),
    path("forum/<int:pk>/", ForumDetailView.as_view(), name="details_forum"),
    path("forum/<int:pk>/add-comment", add_comment, name="add_comment"),
    path("forum/<int:pk>/favorite/", favorite_forum, name="favorite_forum"),
    path("like-comment/<int:pk>/", like_comment, name="like_comment"),
    path("forum/<int:pk>/edit", edit_forum, name="edit_forum"),
    path("search/", search_forums, name="search_forums"),

]
