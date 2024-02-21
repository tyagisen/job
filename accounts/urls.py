from accounts import views
from django.urls import path
from accounts.views import LoginView, SignUpSuperEmployeeView

urlpatterns=[
    path('login/', LoginView.as_view(), name='user-login'),
    path('signup/', SignUpSuperEmployeeView.as_view(), name="sign-up")
]