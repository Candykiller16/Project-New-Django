from django import forms
from django.contrib.auth import models
from django import forms
from .models import Post


class PostForm(forms.ModelForm): # Назначали поля в виде виджетов для вкладки Add Post, присваивали класс CSS из Bootstrap
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'body')

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm): # Назначали поля в виде виджетов для вкладки Add Post, присваивали класс CSS из Bootstrap
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}), 
            # 'author': forms.Select(attrs={'class': 'form-control'}), Убираем лишнее поле для Update post
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }