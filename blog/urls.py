from django.urls import path
from . views import PostListView, PostDetailView
import pickle as pk

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    ]