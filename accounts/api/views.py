from rest_framework.generics import CreateAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from accounts.api.serializers import UserCreateSerializer

User = get_user_model()

class UserCreateAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserCreateSerializer