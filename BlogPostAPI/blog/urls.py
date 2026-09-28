from django.urls import path

from .views import (
    RegisterView,
    LoginView,
    BlogPostListCreateView,
    BlogPostDetailView
)


urlpatterns = [

    path(
        'register/',
        RegisterView.as_view(),
        name='register'
    ),

    path(
        'login/',
        LoginView.as_view(),
        name='login'
    ),

    path(
        'posts/',
        BlogPostListCreateView.as_view(),
        name='post-list-create'
    ),

    path(
        'posts/<int:pk>/',
        BlogPostDetailView.as_view(),
        name='post-detail'
    ),
]