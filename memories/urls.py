from django.urls import path, include
from . import views


urlpatterns = [
    path('delete-memory/<int:memory_id>', views.delete_memory, name='delete-memory'),
    path('post-memory', views.post_memory, name='post-memory'),
    path('', views.home_page, name="home-page"),
    path('home', views.home_page, name="home-page"),
    path('add-memory', views.add_memory_page, name="add-memory-page"),
    path("logout", views.logout_view, name="logout"),
    path('social-auth', include('social_django.urls', namespace="social")),
]
