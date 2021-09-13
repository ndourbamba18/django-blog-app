from django.urls import path  
from . import views   

urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.contact_form, name="contact-form"),
    path('about/', views.about, name="about"),
    path('category/<category>/', views.category_blog, name="category-blog"),
    path('details/<int:pk>/', views.blog_detail, name="blog-detail"),
    #
    path('create-post/', views.createPost, name="create-post"),
]
