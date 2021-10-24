from .celery import app
from board.models import Post


@app.task
def reset_upvotes():
    post_list = Post.objects.all().iterator()
    for post in post_list:
        post.upvotes.clear()
