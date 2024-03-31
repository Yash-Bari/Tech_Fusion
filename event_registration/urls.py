from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration_view, name='registration'),
    path('payment/<int:registration_id>/', views.payment_view, name='payment'),
    path('success/', views.success_view, name='success'),
]
