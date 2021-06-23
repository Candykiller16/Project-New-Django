from django.urls.base import reverse
from myblog.models import Post
from django.shortcuts import render
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']


class ArticleDetailView(DeleteView):
    model = Post
    template_name = 'article_detail.html'


class AddPostView(CreateView):
    model = Post   
    form_class = PostForm   # Присваивали таблице форму с полями для заполнения из forms.py в Add Post вкладке
    template_name = 'add_post.html'
    # fields = '__all__'
    # # fields = ('title', 'body')


class UpdatePostView(UpdateView):
    model = Post  
    form_class = EditForm 
    template_name = 'update_post.html'
    # fields = ['title', 'title_tag', 'body'] form_class не работает вместе с fields


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')