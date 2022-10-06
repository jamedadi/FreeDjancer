from django.urls import path, include
from rest_framework import routers

from accounts.api.views import UserAuthenticatedProfileViewSet, UserRegistrationCreateAPIView, \
    UserChangePasswordAPIView, UserReadOnlyViewSet, UserProjectsModelViewSet, UserPortfolioListRetrieveView, \
    UserAuthenticatedFollowingsAPIView, UserAuthenticatedFollowersAPIView

user_info = routers.SimpleRouter()
user_info.register('user', UserReadOnlyViewSet, basename='user-info')

# user_authenticated_profile = routers.SimpleRouter()
# user_authenticated_profile.register('profile', UserAuthenticatedProfileViewSet, basename='profile')


# user_projects = routers.SimpleRouter()
# user_projects.register('', UserProjectsModelViewSet, 'user-projects')


urlpatterns = [
    path('register/', UserRegistrationCreateAPIView.as_view(), name='user-register'),
    path('changepassword/', UserChangePasswordAPIView.as_view(), name='change-password'),
    path('profile/', UserAuthenticatedProfileViewSet.as_view(), name='user-profile'),
    path('profile/followings/', UserAuthenticatedFollowingsAPIView.as_view(), name='user-profile-followings'),
    path('profile/followers/', UserAuthenticatedFollowersAPIView.as_view(), name='user-profile-followers'),


    path('', include(user_info.urls)),
    # path('', include(user_authenticated_profile.urls))
]
