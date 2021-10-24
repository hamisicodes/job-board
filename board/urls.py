from django.urls import path
from .views import PostsView, PostView

urlpatterns = [
    path('news-list/', PostsView.as_view(), name='news_list'),
    path('<pk>/', PostView.as_view(), name='news_detail'),
]
