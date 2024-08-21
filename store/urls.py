"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('about/', views.about, name='about'),
    path('rings/', views.rings, name='rings'),
    path('earrings/', views.earrings, name='earrings'),
    path('necklace/', views.necklace, name='necklace'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('my-account/', views.my_account, name='my_account'),
    path('orders/', views.orders, name='orders'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('preferences/', views.preferences, name='preferences'),
    #path('update_password/', views.update_password, name='update_password'),
    path('update_user/', views.update_user, name='update_user'),
    #path('update_info/', views.update_info, name='update_info'),
    path('product/<int:pk>', views.product, name='product'),
    path('category/<str:foo>', views.category, name='category'),
    path('category_summary/', views.category_summary, name='category_summary'),
    #path('search/', views.search, name='search'),
    
]


