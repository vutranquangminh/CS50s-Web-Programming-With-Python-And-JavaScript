
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('like/<int:postid>', views.like, name='like'),
    path('post/<int:postid>', views.post, name='post'),
    path('profile/<int:profileid>', views.profile, name='profile'),
    path('following', views.following, name='following'),
]
