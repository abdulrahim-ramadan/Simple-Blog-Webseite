from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView , DetailView, CreateView, UpdateView, DeleteView
from .models import Post , Comment
from .forms import PostForm, CommentForm
from django.urls import reverse
from django.db.models import Q

class PostList(ListView):
    model = Post
    template_name = 'post_list.html'  
    context_object_name = 'post_list'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
        else:
            return Post.objects.all()

class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["post_comment"] = Comment.objects.filter(post=self.get_object())
        return context
    
def add_post_comment(request,pk):
    post = Post.objects.get(pk=pk)


    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user =  request.user
            myform.post = post
            myform.save()
            
            return redirect(reverse('post_detail', kwargs={'pk': post.pk}))
        


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
    
    






     

    

 