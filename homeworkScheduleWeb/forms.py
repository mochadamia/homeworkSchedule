from django import forms

from .models import Comment

class PostComment(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)