from django.urls import path
from .views import PostsView, PostView, CommentsView, CommentView

urlpatterns = [
    path('news-list/', PostsView.as_view(), name='news_list'),
    path('<pk>/', PostView.as_view(), name='news_detail'),
    path('news-comments', CommentsView.as_view(), name='news_comment'),
    path('comments/<pk>', CommentView.as_view(), name='comment_details')
]
