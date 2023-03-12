from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse

from .models import Category, Post


def index(request):
    """
    View for the main page of the site.
    """
    category_list = Category.objects.all()
    context = {
        'category_list': category_list
    }
    return render(request, 'index.html', context)


class CategoryList(generic.ListView):
    """
    In this page we show a list with all the categories contained in the wiki.
    """
    model = Category
    template_name = "category_list.html"
    context_object_name = "category_list"

    def get_queryset(self):
        return Category.objects.all()


def post_list_view(request, category_slug):
    """
    View for the list of posts inside a certain category.
    """
    category = get_object_or_404(Category, slug=category_slug)
    post_list = Post.objects.filter(category=category)

    context = {
        "category": category,
        "post_list": post_list,
    }
    return render(request, "post_list.html", context)


class PostDetail(generic.DetailView):
    """
    Detail view of a single post.
    """
    model = Post
    template_name = "post_detail.html"


def contact(request):
    """
    In this page we have a contact form available for the user.
    """
    return render(request, 'contact.html')
