from django.urls import path
from . import views

urlpatterns = [
    path('bespoke/', views.bespoke, name='members'),
    path('bespoke/contactus/', views.contactus, name = 'contact'),
    path('bespoke/book', views.book, name = 'book')
]