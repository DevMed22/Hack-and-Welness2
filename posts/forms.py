from django import forms
from .models import Post, Comment

class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        feilds = '__all__'
        exclude = ('author','published_date', 'edited_date',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)