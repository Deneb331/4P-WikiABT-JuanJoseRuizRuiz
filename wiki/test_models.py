from django.test import TestCase
from .models import Category, Post, Comment


class TestCategoryModel(TestCase):
    def test_string_method_returns_title(self):
        category = Category.objects.create(title='test title', description='test description')
        self.assertEqual(str(category), 'test title')

    def test_category_slug_is_equal_to_slugified_title(self):
        category = Category.objects.create(title='test title', description='test description')
        self.assertEqual(category.slug, 'test-title')


class TestPostModel(TestCase):
    def test_string_method_returns_title(self):
        category = Category.objects.create(title='test category', description='test description')
        post = Post.objects.create(title='test post', category=category, image_alt='test alt', content='test content')
        self.assertEqual(str(post), 'test post')

    def test_post_slug_is_equal_to_slugified_title(self):
        category = Category.objects.create(title='test category', description='test description')
        post = Post.objects.create(title='test post', category=category, image_alt='test alt', content='test content')
        self.assertEqual(post.slug, 'test-post')


class TestCommentModel(TestCase):
    def test_string_method_returns_title_and_body(self):
        category = Category.objects.create(title='test category', description='test description')
        post = Post.objects.create(title='test post', category=category, image_alt='test alt', content='test content')
        comment = Comment.objects.create(name='test user', post=post, email='testmail@1234.com', body='test body', created_on='february', approved=True)
        self.assertEqual(str(comment), 'Comment test body by test user')
