from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, CreateAPIView
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated

from accounts.api.serializers import UserInfoSerializer, UserRegisterSerializer, UserChangePasswordSerializer, \
    UserLiteInfoSerializer, PortfolioSerializer

User = get_user_model()


class UserInfoRetrieveUpdateAPIView(RetrieveAPIView, UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserInfoSerializer

    def get_object(self):
        return self.request.user


class UserLiteInfoAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    lookup_field = 'username'
    serializer_class = UserLiteInfoSerializer


class UserPortfolioListRetrieveView(ListModelMixin, RetrieveModelMixin, ):
    serializer_class = PortfolioSerializer



class UserRegistrationCreateAPIView(CreateAPIView):
    serializer_class = UserRegisterSerializer


class UserChangePasswordAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserChangePasswordSerializer

    def get_object(self):
        return self.request.user




