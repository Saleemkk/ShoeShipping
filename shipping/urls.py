from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('shop/', views.shop, name='shop'),
    path('contact/', views.contact, name='contact'),
    path('service/', views.service, name='service'),
    path('howtobuy/', views.howtobuy, name='howtobuy'),
    path('products/', views.products, name='products'),
 
]