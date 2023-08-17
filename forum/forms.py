from django import forms
from .models import Forum, Comment


class ForumCreationForm(forms.ModelForm):  # TODO rename the form to Creation/Edit/Form or more generally just ForumForm
    class Meta:
        model = Forum
        fields = ['title', 'description', 'image']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content", ]
