from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('/about', views.index, name="about"),
    path('products/', views.products, name="products"),
    path('services/', views.services, name="services"),
    
    
]