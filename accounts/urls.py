from django.urls import path

from accounts.views import UserInfoRetrieveUpdateAPIView, UserRegistrationCreateAPIView, UserChangePasswordAPIView

urlpatterns = [
    path('profile/', UserInfoRetrieveUpdateAPIView.as_view(), name='user-info'),
    path('register/', UserRegistrationCreateAPIView.as_view(), name='user-register'),
    path('changepassword/', UserChangePasswordAPIView.as_view(), name='change-password')
]
