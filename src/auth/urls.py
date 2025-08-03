from auth.views import AuthObtainTokenView
from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path


app_name = 'auth'

urlpatterns = [
    path('login/', AuthObtainTokenView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
]