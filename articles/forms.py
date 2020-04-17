from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    """Форма для комментариев"""
    class Meta:
        model = Comment
        fields = ('comment',)
