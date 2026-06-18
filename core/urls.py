from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('blogs/', views.blogs, name='blogs'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path("robots.txt", views.robots_txt, name='robots_txt'),
    path(
    'who-is-gbarabe-tordi-joseph/',
    views.profile,
    name='profile'
)
]