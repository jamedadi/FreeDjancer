from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from jobs.models import Project
from jobs.api.pagination import StandardSizePagination
from jobs.api.serializers import ProjectSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = StandardSizePagination
    lookup_field = 'pk'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'skills__skill', 'budget__min_price', 'budget__max_price',]
 
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
