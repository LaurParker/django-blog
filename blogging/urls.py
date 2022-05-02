from django.urls import path
from blogging.views import BlogListView, BlogDetailView, stub_view

urlpatterns = [
    path('', BlogListView.as_view(), name="blog_index"),
    path('posts/<int:pk>/', BlogDetailView.as_view(), name="blog_detail"),
]
