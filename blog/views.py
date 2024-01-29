from django.shortcuts import render
from django.views.generic import ListView , DetailView, CreateView, UpdateView, DeleteView 
from .models import Post
from .forms import PostForm

class PostList(ListView):
    model = Post

class PostDetail(DetailView):
    model = Post 

class PostCreate(CreateView):
    model = Post
    success_url='/blog/'
    form_class = PostForm


class PostEdit(UpdateView):
    model = Post
    success_url='/blog/'
    template_name = 'blog/post_edit.html'
    form_class = PostForm


class PostDelete(DeleteView):
    model = Post
    success_url='/blog/'

 