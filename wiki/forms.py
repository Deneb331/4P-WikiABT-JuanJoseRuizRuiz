from django import forms
from .models import Comment, Post
from django_summernote.widgets import SummernoteInplaceWidget, SummernoteWidget


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'content': SummernoteWidget(),
            'infobox_content': SummernoteWidget(),
        }
        