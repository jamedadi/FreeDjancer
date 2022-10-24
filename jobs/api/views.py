from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from accounts.models import UserSkill
from jobs.models import Project,ProjectSkill, Skill
from jobs.api.pagination import StandardSizePagination
from jobs.api.serializers import ProjectSerializer


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    pagination_class = StandardSizePagination
    lookup_field = 'pk'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'skills__skill', 'budget__min_price', 'budget__max_price',]

    def get_queryset(self):
        is_authenticated = self.request.user.is_authenticated

        if is_authenticated:   
            user = self.request.user
            user_skills = UserSkill.objects.filter(user=user).values('skill')
            projects = ProjectSkill.objects.filter(skill__in=user_skills).values('project')
            print(projects)
            return projects 
 
 
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
