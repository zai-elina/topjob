from django import forms
from django.contrib.admin import widgets
from .models import Post,Comment

class PostForm(forms.ModelForm):
    title = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control form-control-lg','placeholder':'Заголовок'}))
    description = forms.CharField(required=True, widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Описание'}))
    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class':'form-control'}))

    class Meta:
        model = Post
        fields = ['title', 'description', 'image']


class CommentForm(forms.ModelForm):
    text_comments = forms.CharField(required=True, widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Комментарий'}))

    class Meta:
        model = Comment
        fields = ['text_comments']