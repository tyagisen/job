from django.urls import path
from .views import UserCreateAPIView


urlpatterns = [
    path('create', UserCreateAPIView.as_view(), name='api-user-create'),
]