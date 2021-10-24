from django.db import models
from users.models import CustomUser


class Post(models.Model):
    """
        Model for a particular News Post
    """
    title = models.CharField(max_length=50, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    amount_of_upvotes = models.ManyToManyField(
        CustomUser, related_name='voted_posts')
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="authored_posts")


class Comment(models.Model):
    """
        Model for a comment on a News Post
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
