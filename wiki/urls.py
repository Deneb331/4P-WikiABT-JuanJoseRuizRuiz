from django.urls import path
from . import views

app_name = 'wiki'
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('create-post/', views.create_post, name='create_post'),
    path('categories/', views.CategoryList.as_view(), name='category_page'),
    path('<slug:category_slug>/', views.post_list_view, name='post_page'),
    path('<slug:category_slug>/<slug:post_slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostDetailLike.as_view(), name='post_detail_like'),
    path('like/<slug:slug>', views.PostListLike.as_view(), name='post_list_like'),
]