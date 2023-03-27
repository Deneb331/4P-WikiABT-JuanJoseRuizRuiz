from django.test import TestCase
from .forms import CommentForm, PostForm, ContactForm


class CommmentFormTest(TestCase):
    def test_body_content_is_required(self):
        form = CommentForm({'body': ""})
        self.assertFalse(form.is_valid())
        
