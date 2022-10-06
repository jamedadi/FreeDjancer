from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, CreateAPIView, ListAPIView, DestroyAPIView
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from accounts.api.serializers import UserRetrieveUpdateSerializer, UserRegisterSerializer, \
    UserChangePasswordSerializer, UserReadOnlySerializer, PortfolioSerializer, UserFollowingsSerializer, \
    UserFollowersSerializer
from accounts.models import Relation
from jobs.api.serializers import ProjectSerializer

User = get_user_model()


class UserAuthenticatedProfileViewSet(RetrieveAPIView, UpdateAPIView):
    """
    View to retrieve or update user profile
    """
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserRetrieveUpdateSerializer

    # lookup_url_kwarg = ''
    # lookup_field = ''

    def get_object(self):
        return self.request.user


class UserAuthenticatedFollowingsAPIView(ListAPIView, DestroyAPIView):
    """
    Authenticated User can see own followings and unfollow them.
    """
    queryset = Relation.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserFollowingsSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(from_user=self.request.user)

    def list(self, request, *args, **kwargs):
        qs = self.get_queryset()
        serializer = self.serializer_class(qs, many=True)
        return Response(serializer.data)
# TODO : ADD Destroy to Following
    # def destroy(self, request, *args, **kwargs):
    #     qs = super().get_queryset()


class UserAuthenticatedFollowersAPIView(ListAPIView):
    """
    Authenticated User can see own followers
    """
    queryset = Relation.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserFollowersSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(to_user=self.request.user)

    def list(self, request, *args, **kwargs):
        qs = self.get_queryset()
        serializer = self.serializer_class(qs, many=True)
        return Response(serializer.data)

    # def destroy(self, request,pk, *args, **kwargs):
    #     unfollow_user = User.objects.filter(pk=pk)
    #     serializer = self.serializer_class()
    #     return Response(serializer.data)


class UserReadOnlyViewSet(RetrieveModelMixin, GenericViewSet):
    """
    View to retrieve user profile
    """
    queryset = User.objects.all()
    serializer_class = UserReadOnlySerializer
    lookup_url_kwarg = 'username'

    def get_object(self, *args, **kwargs):
        user = User.objects.filter(username=self.kwargs['username']).first()
        return user

    @action(detail=True, methods=['GET'])
    def portfolios(self, request, *args, **kwargs):
        """  All Portfolios of the user """
        user = self.get_object()
        qs = user.portfolios.all()
        serializer = PortfolioSerializer(data=qs, many=True)
        serializer.is_valid()
        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def projects(self, request, *args, **kwargs):
        """ All Projects that user created """
        user = self.get_object()
        qs = user.projects.all()
        serializer = ProjectSerializer(data=qs, many=True)
        serializer.is_valid()
        return Response(serializer.data)


class UserProjectsModelViewSet(ModelViewSet):
    """
    View to retrieve or update user projects
    """
    # queryset = Project.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_object(self):
        return self.request.user

    def get_queryset(self):
        return self.request.user.projects.all()


class UserPortfolioListRetrieveView(ListModelMixin, RetrieveModelMixin, ):
    serializer_class = PortfolioSerializer


class UserRegistrationCreateAPIView(CreateAPIView):
    serializer_class = UserRegisterSerializer


class UserChangePasswordAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserChangePasswordSerializer

    def get_object(self):
        return self.request.user
