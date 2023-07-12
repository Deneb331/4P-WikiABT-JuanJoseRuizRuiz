from django.test import TestCase, Client
from .models import Post, Category


class TestView(TestCase):
    def test_main_page_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


    def test_contact_page(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')


    def test_login_page(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')


    def test_signup_page(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/signup.html')


    def test_category_list_page(self):
        response = self.client.get(f'/categories/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category_list.html')


    def test_post_list_page(self):
        category = Category.objects.create(
            title = 'test category',
            slug = 'test-category',
            description = 'test description'
        )
        response = self.client.get(f'/{category.slug}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_list.html')


    def test_post_detail_page(self):
        category = Category.objects.create(
            title = 'test category',
            description = 'test description'
        )
        post = Post.objects.create(
            title = 'test post',
            slug = 'test-post',
            category = category,
            image_alt = 'test alt',
            content = 'test content',
            infobox_content = 'test infobox content',
            status = 1
        )
        response = self.client.get(f'/{category.slug}/{post.slug}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')
