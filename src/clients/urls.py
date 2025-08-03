from django.urls import path
from clients.views import ClientsApi, ClientApi

app_name = 'clients'

urlpatterns = [
    path('', ClientsApi.as_view(), name='clients'),
    path('<int:id>/', ClientApi.as_view(), name='client'),
]