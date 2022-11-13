from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend

from jobs.api.filters import IsAuthenticatedFilterBackend
from jobs.models import Project
from jobs.api.pagination import StandardSizePagination
from jobs.api.serializers import ProjectSerializer


class ProjectViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    """
    To show all projects
    User can filter projects by "filterset_fields"
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = StandardSizePagination
    lookup_field = 'pk'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'skills__skill', 'budget__min_price', 'budget__max_price',]


class UserSkillProjectViewSet(ListModelMixin, GenericViewSet):
    """
    To show all projects by authenticated User skills
    """
    queryset = Project.objects.prefetch_related('skills__skill').all()
    serializer_class = ProjectSerializer
    pagination_class = StandardSizePagination
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'
    filter_backends = [IsAuthenticatedFilterBackend]


