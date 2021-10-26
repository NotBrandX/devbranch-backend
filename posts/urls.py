from django.urls import path

from .views import PostListView
from .views import CommentListView

app_name = 'posts'

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('', CommentListView.as_view(), name='comment-list'),
]
