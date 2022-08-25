from rest_framework.viewsets import ModelViewSet

from jobs.models import Project
from jobs.serializers import ProjectSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'pk'
