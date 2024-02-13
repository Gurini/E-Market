from django.urls import path
from . import views 

urlpatterns = [
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),

    #update
    path('update_item/', views.upadateItem, name='update_item'),

    #Process orer
    path('proceess_order/', views.processOrder, name='proceess_order'),
]