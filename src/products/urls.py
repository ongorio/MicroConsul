from django.urls import path
from products.views import ProductsApi, ProductApi

app_name = 'products'

urlpatterns = [
    path('', ProductsApi.as_view(), name='products'),
    path('<int:id>/', ProductApi.as_view(), name='product'),
]