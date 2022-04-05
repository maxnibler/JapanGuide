from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'featured',
        ]

class RawPostForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()
    featured = forms.BooleanField()
    