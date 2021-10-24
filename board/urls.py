from django.urls import path
from .views import PostsView, PostView, CommentsView, CommentView, UpvoteView

urlpatterns = [
    path('news-list/', PostsView.as_view(), name='news_list'),
    path('<pk>/', PostView.as_view(), name='news_detail'),
    path('news-comments', CommentsView.as_view(), name='news_comment'),
    path('comments/<pk>', CommentView.as_view(), name='comment_details'),
    path('upvote/<pk>', UpvoteView.as_view(), name='upvote')
]
