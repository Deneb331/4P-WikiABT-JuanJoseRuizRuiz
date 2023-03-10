from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse

STATUS = ((0, "Draft"), (1, "Published"))


class Category(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=1000)
    slug = models.SlugField(max_length=200, unique=True)
    feature_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True, null=False)
    slug = models.SlugField(max_length=200, unique=True, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name="post_like", blank=True)

    class Meta:
        ordering = ["title"]

#    def get_absolute_url(self):
#        return f'/{self.category.slug}/{self.slug}/'

    def get_absolute_url(self):
        return reverse("wiki:post_detail", kwargs={"category_slug": self.category.slug, "post_slug": self.slug})

    def __str__(self):
        return self.title
