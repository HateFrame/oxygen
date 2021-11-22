from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_page, name='shop_page'),
    path('shop/', views.index, name='index'),
    path('product/<int:prod_id>/', views.product_page),
    path('request/', views.request_page)
]
