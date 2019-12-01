from django import forms

from .models import Comment, Assignment, ClassName


class PostComment(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)

class AssignmentForm(forms.ModelForm):
    class_id = forms.ModelChoiceField(queryset=ClassName.objects.all(), widget=forms.Select(
        attrs={
            'class': 'bootstrap-select',
        }
    ))
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))
    content = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
        }
    ))

    class Meta:
        model = Assignment
        fields = ('class_id', 'name', 'content',)

