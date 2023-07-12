from django.test import TestCase
from .forms import CommentForm, PostForm, ContactForm


class CommmentFormTest(TestCase):
    def test_body_content_is_required(self):
        form = CommentForm({'body': ""})
        self.assertFalse(form.is_valid())
        

class ContactFormTest(TestCase):
    def test_name_is_required(self):
        form = ContactForm({
            'name': '',
            'email': '123@asdf.com',
            'subject': 'test subject',
            'message': 'test message'
        })
        self.assertFalse(form.is_valid())
    
    def test_email_is_required(self):
        form = ContactForm({
            'name': 'test name',
            'email': '',
            'subject': 'test subject',
            'message': 'test message'
        })
        self.assertFalse(form.is_valid())
    
    def test_subject_is_required(self):
        form = ContactForm({
            'name': 'test name',
            'email': '123@asdf.com',
            'subject': '',
            'message': 'test message'
        })
        self.assertFalse(form.is_valid())

    def test_message_is_required(self):
        form = ContactForm({
            'name': 'test name',
            'email': '123@asdf.com',
            'subject': 'test subject',
            'message': ''
        })
        self.assertFalse(form.is_valid())
    

class PostFormTest(TestCase):
    def test_title_is_required(self):
        form = PostForm({
            'title': '',
            'category': 'TestCategory',
            'featured_image': '',
            'image_alt': 'TestAlt',
            'content': 'TestContent',
            'infobox_content': 'TestInfoboxContent',
            'status': 1
        })
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(
            form.errors['title'][0], 'This field is required.')
    
    def test_category_is_required(self):
        form = PostForm({
            'title': 'test title',
            'category': '',
            'featured_image': '',
            'image_alt': 'TestAlt',
            'content': 'TestContent',
            'infobox_content': 'TestInfoboxContent',
            'status': 1
        })
        self.assertFalse(form.is_valid())
        self.assertIn('category', form.errors.keys())
        self.assertEqual(
            form.errors['category'][0], 'This field is required.')

    def test_content_is_required(self):
        form = PostForm({
            'title': 'test title',
            'category': 'test category',
            'featured_image': '',
            'image_alt': 'test_alt',
            'content': '',
            'infobox_content': 'TestInfoboxContent',
            'status': 1
        })
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(
            form.errors['content'][0], 'This field is required.')

    def test_infobox_content_is_required(self):
        form = PostForm({
            'title': 'test title',
            'category': 'test category',
            'featured_image': '',
            'image_alt': 'test_alt',
            'content': 'TestContent',
            'infobox_content': '',
            'status': 1
        })
        self.assertFalse(form.is_valid())
        self.assertIn('infobox_content', form.errors.keys())
        self.assertEqual(
            form.errors['infobox_content'][0], 'This field is required.')

    def test_status_is_required(self):
        form = PostForm({
            'title': 'test title',
            'category': 'test category',
            'featured_image': '',
            'image_alt': 'test_alt',
            'content': 'TestContent',
            'infobox_content': '',
            'status': ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('status', form.errors.keys())
        self.assertEqual(
            form.errors['status'][0], 'This field is required.')
