from rest_framework import generics
from django.views.generic import ListView
from .models import Post

# Create your views here.
class PostListView(ListView):
    model = Post
    context_object_name = 'posts'