from django.urls import path, re_path
from .views import (
        PostListView,
        PostDetailView,
        PostCreateView,
        PostUpdateView,
        PostDeleteView,
        UserPostListView,
        contact,
        search
        )
from . import views
from users import views as user_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('newest', views.newest, name='newest'),
    path('oldest', views.oldest, name='oldest'),
    path('new_answer', views.new_answer, name='new_answer'),
    path('get_posts_by_tag/<str:title>', views.get_posts_by_tag, name='get_posts_by_tag'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('profile/',user_views.profile,name='profile'),
    path('post/<int:pk>/', views.displayPost, name='post-detail'),
    path('myPosts/<int:id_user>/', views.list_myPosts, name='my_posts'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('question/', views.question, name='questions'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('register/',user_views.register,name='register'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/comment/', views.add_comment_to_post,name='add_comment_to_post'),
    path('post/<int:pk>/anonymous_comment/', views.add_anonymous_comment_to_post,name='add_anonymous_comment_to_post'),
    path('post/<int:pk>/approve/', views.comment_approve,name='comment_approve'),
    path('post/<int:pk>/remove/', views.comment_remove,name='comment_remove'),
    path('profileUser/<int:pk>/', views.profile_remove,name='profile_remove'),
    path('approveprofile/<int:pk>/', views.profile_approve,name='profile_approve'),
    path('approverole/<int:pk>/', views.role_approve,name='role_approve'),
    path('removerole/<int:pk>/', views.role_remove,name='role_remove'),
    path('search/', views.search, name='search'),
    path('contact/', views.contact, name='Contact')
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
