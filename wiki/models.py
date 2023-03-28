from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Category(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=1000)
    slug = models.SlugField(max_length=200, unique=True)
    feature_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ["title"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True, null=False)
    slug = models.SlugField(max_length=200, unique=True, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    featured_image = CloudinaryField('image', default='placeholder')
    image_alt = models.CharField(max_length=100, default="")
    content = models.TextField(default="")
    infobox_content = models.TextField(default="")
    updated_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name="post_like", blank=True)

    class Meta:
        ordering = ["title"]

    def get_absolute_url(self):
        return reverse("wiki:post_detail", kwargs={"category_slug": self.category.slug, "post_slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"