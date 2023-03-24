from django import forms
from .models import Comment, Post
from django_summernote.admin import SummernoteModelAdmin


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
        summernote_fields = ('content',)
        fields = ('title', 'slug', 'category', 'featured_image', 'image_alt', 'infobox_content', 'status')