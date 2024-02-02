from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView , DetailView, CreateView, UpdateView, DeleteView
from .models import Post ,Comment
from .forms import PostForm
from django.views import View
from django.urls import reverse

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



class AddCommentView(CreateView):
    model = Comment
    fields = ['comment']  # Assuming 'text' is the field for the comment text

    def form_valid(self, form):
        post_id = self.kwargs['post_id']
        form.instance.post_id = post_id
        return super().form_valid(form)

    def get_success_url(self):
        post_id = self.kwargs['post_id']
        return reverse('post_detail', kwargs={'post_id': post_id})
    



class CommentListView(ListView):
    model = Comment



     

    

 