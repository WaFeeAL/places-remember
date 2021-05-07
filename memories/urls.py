from django.urls import path
from . import views


urlpatterns = [
    # path('friend/', FriendList.as_view()),
    path('get-memory-list', views.get_memory_list, name='get-memory-list'),
    path('delete-memory/<int:memory_id>', views.delete_memory, name='delete-memory'),
    path('get-memory/<int:memory_id>', views.get_memory, name='get-memory'),
    path('post-memory', views.post_memory, name='post-memory'),
    # path('add/<int:product_id>', views.cart_add, name='cart-add'),
    # path('remove/<int:product_id>', views.cart_remove, name='cart-remove'),
]