from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

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
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name="post_like", blank=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title