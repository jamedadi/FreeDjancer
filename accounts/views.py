from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.generics import get_object_or_404, RetrieveAPIView, UpdateAPIView, CreateAPIView
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from accounts.serializers import UserInfoSerializer, UserRegisterSerializer, UserChangePasswordSerializer, \
    UserLiteInfoSerializer

User = get_user_model()


class UserInfoRetrieveUpdateAPIView(RetrieveAPIView, UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserInfoSerializer

    def get_object(self):
        return self.request.user


class UserLiteInfoAPIView(RetrieveAPIView):
    serializer_class = UserLiteInfoSerializer
    lookup_url_kwarg = 'username'
    lookup_field = 'username'


class UserRegistrationCreateAPIView(CreateAPIView):
    serializer_class = UserRegisterSerializer


class UserChangePasswordAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserChangePasswordSerializer

    def get_object(self):
        return self.request.user




