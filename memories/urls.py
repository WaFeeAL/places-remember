from django.urls import path
from . import views


urlpatterns = [
    # path('friend/', FriendList.as_view()),
    path('', views.memory_list, name='memory-list'),
    path('delete-memory/<int:memory_id>', views.delete_memory, name='delete-memory'),
    path('<int:memory_id>', views.memory_detail, name='memory-detail'),
    # path('add/<int:product_id>', views.cart_add, name='cart-add'),
    # path('remove/<int:product_id>', views.cart_remove, name='cart-remove'),
]