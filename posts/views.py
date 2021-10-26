from rest_framework import generics
from django.views.generic import ListView
from .models import Post, Comment

# Create your views here.
class PostListView(ListView):
    model = Post
    context_object_name = 'posts'

class CommentListView(ListView):
    model = Comment
    context_object_name = 'comments'