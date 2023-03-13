from django.urls import path
from . import views

app_name = 'wiki'
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('categories/', views.CategoryList.as_view(), name='category_page'),
    path('<slug:category_slug>/', views.post_list_view, name='post_page'),
    path('<slug:category_slug>/<slug:post_slug>/', views.PostDetail.as_view(), name='post_detail'),
]