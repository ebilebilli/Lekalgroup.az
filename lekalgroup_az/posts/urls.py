from django.urls import path
from posts.views import *

app_name = 'posts'

urlpatterns = [
    path(
        '',
        HomeView.as_view(),
        name='home-page'
        ),
    path(
        'blog/',
        BlogView.as_view(),
        name='blog-page'
        ),
    path(
        'about/',
        AboutView.as_view(),
        name='about-page'
        ),
]