from django.urls import path, re_path
from .views import (
        PostListView,
        PostDetailView,
        PostCreateView,
        PostUpdateView,
        PostDeleteView,
        UserPostListView
        )
from . import views
from users import views as user_views


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('question/', views.question, name='questions'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('register/',user_views.register,name='register'),
    path('about/', views.about, name='blog-about'),
    re_path('(?P<slug>[-\w]+)/add_comment', views.add_comment, name='add_comment'),
]
