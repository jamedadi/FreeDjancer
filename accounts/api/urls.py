from django.urls import path, include
from rest_framework import routers

from accounts.api.views import UserInfoRetrieveUpdateAPIView, UserRegistrationCreateAPIView, \
    UserChangePasswordAPIView, UserLiteInfoAPIView, UserInfoReadOnlyViewSet

router = routers.SimpleRouter()

router.register('user', UserInfoReadOnlyViewSet, 'user-info')

urlpatterns = [
    path('profile/', UserInfoRetrieveUpdateAPIView.as_view(), name='user-info'),
    path('register/', UserRegistrationCreateAPIView.as_view(), name='user-register'),
    path('changepassword/', UserChangePasswordAPIView.as_view(), name='change-password'),
    path('user/<str:username>/', UserLiteInfoAPIView.as_view(), name='user-profile'),
    # path('user/portfolio/<int:pk>', UserPortfolioListRetrieveView.as_view(), name='user-portfolio'),
    path('user/<str:username>', include(router.urls))
]
