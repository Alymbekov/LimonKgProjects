from django import forms
from .models import Comment, Article

from tinymce.widgets import TinyMCE


class CustomCreateForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    class Meta:
        model = Article
        fields = ('title', 'description', 'category', 'image',)
        

class CommentForm(forms.ModelForm):
    """Форма для комментариев"""
    comment = forms.CharField(label="", widget=forms.Textarea(attrs={
        'class': 'form-control', 'placeholder': 'Write a text', 'rows':'4', 'cols':'50'
        }))

    class Meta:
        model = Comment
        fields = ('comment',)
