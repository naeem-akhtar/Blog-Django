from django.urls import path
from . import views
from .views import (
	PostListView,
  UserPostListView, 
	PostDetailView,
	PostCreateView,
	PostUpdateView,
	PostDeleteView
)

urlpatterns = [
  path('', PostListView.as_view(), name='blog-home'), # home page
  path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
  path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), # post page
  path('post/new/', PostCreateView.as_view(), name='post-create'), # create new post
  path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'), # update post
  path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'), # delete post
  path('about/', views.about, name='blog-about'), # about the websites
]
