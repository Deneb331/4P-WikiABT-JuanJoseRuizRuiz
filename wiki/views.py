from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Category, Post


def index(request):
    return render(request, "index.html")


class CategoryList(generic.ListView):
    """
    In this page we show a list with all the categories contained in the wiki.
    """
    model = Category
    queryset = Category.objects.all()
    template_name = "category_list.html"
