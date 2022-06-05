from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect, name='redirect'),
    path('main/', views.main, name='main'),
    path('main/<int:pk>/', views.yogurt_detail, name='yogurt_detail'),
    path('log_in/', views.log_in_user, name='log_in'),
    path('log_out/', views.log_out_user, name='logout_user'),
    path('registration/', views.register_user, name='registration'),
    path('order_create/<int:pk>', views.create_order, name='order_create'),
]