from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        model = Post
        fields = ('title','content', 'img', 'draft', 'publish')


    

