from pyexpat import model
from django import forms
from .models import Post

title = forms.CharField(help_text='maksymalnie 200 znaków')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']
