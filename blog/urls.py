from django.urls import path
from . views import PostListView, PostDetailView, PostCreateView
from . views import postUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-new'),
    path('post/<int:pk>/update', postUpdateView.as_view(), name='post-update' ),
    path('post/<int:pk>/delete',PostDeleteView.as_view(), name='post-delete')
    ]