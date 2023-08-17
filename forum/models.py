from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

AppUser = get_user_model()


class Forum(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    date_time_of_creation = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    image = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.DO_NOTHING)
    to_forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    date_time_of_creation = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)

    def is_nested(self):
        return self.parent_comment is not None


class Upvote(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    to_comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="upvotes")


class Favorites(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    to_forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
