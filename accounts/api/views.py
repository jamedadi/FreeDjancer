from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, CreateAPIView, ListAPIView, DestroyAPIView
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from accounts.api.serializers import UserRetrieveUpdateSerializer, \
    UserRegisterSerializer, \
    UserChangePasswordSerializer, UserReadOnlySerializer, PortfolioSerializer, \
    UserFollowingsSerializer, \
    UserFollowersSerializer, EmployerRegisterSerializer
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


class UserAuthenticatedFollowingsAPIView(ListAPIView):
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

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class DestroyFollowingAPIView(DestroyAPIView):
    queryset = Relation.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserFollowingsSerializer

    # TODO check the relation is real or not
    def get_object(self, *args, **kwargs):
        instance = Relation.objects.filter(from_user=self.request, to_user=self.lookup_url_kwarg)
        return super().get_object(instance)


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
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'username': user.username,
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserChangePasswordAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserChangePasswordSerializer

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response({
            'message': 'Password successfully changed!'
        }, status=status.HTTP_200_OK)


class EmployerRegistrationCreateAPIView(CreateAPIView):
    serializer_class = EmployerRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            employer = serializer.save()
            refresh = RefreshToken.for_user(employer)
            return Response({
                'username': employer.user.username,
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(TokenObtainPairView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]