from django.urls import path, include

app_name = 'dawn'

from clients.urls import urlpatterns as clients_urls
from products.urls import urlpatterns as products_urls
from auth.urls import urlpatterns as auth_urls

urlpatterns = [
    path('clients/', include(clients_urls)),
    path('products/', include(products_urls)),
    path('auth/', include(auth_urls)),
]