from django.urls import path
from .views import (
    home, demo, login_view, my_account, order_history, 
    saved_addresses, saved_payment_details, wishlist, 
    recommendations, individual_order, return_order, 
    order_history_json, add_jewelry_item, jewelry_list, explore_more, CustomLoginView, 
    add_to_cart, cart_detail,update_cart
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', home, name='home'),
    path('demo/', demo, name='demo'),
    path('my_account/', my_account, name='my_account'),
    path('order_history/', order_history, name='order_history'),
    path('saved_addresses/', saved_addresses, name='saved_addresses'),
    path('saved_payment_details/', saved_payment_details, name='saved_payment_details'),
    path('wishlist/', wishlist, name='wishlist'),
    path('recommendations/', recommendations, name='recommendations'),
    path('individual_order/<int:order_id>/', individual_order, name='individual_order'),
    path('return_order/', return_order, name='return_order'),
    path('order_history_json/', order_history_json, name='order_history_json'),
    path('add/', add_jewelry_item, name='add_jewelry_item'),
    path('list/', jewelry_list, name='jewelry_list'),
    path('explore_more/', explore_more, name='explore_more'),
    path('add_to_cart/<int:item_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_detail, name='cart_detail'),
    path('update_cart/<int:item_id>/', update_cart, name='update_cart'),
]
