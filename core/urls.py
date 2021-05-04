from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="home-page"),
    path('home', views.home, name="home-page"),
    # path('show', views.show, name="show-page"),
    # path("login", views.home, name="login"),
    path("logout", views.logout_view, name="logout"),
    path('social-auth', include('social_django.urls', namespace="social")),
]
