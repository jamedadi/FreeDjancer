from rest_framework.viewsets import ModelViewSet

from jobs.models import Project
from jobs.pagination import StandardSizePagination
from jobs.serializers import ProjectSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = StandardSizePagination
    lookup_field = 'pk'
