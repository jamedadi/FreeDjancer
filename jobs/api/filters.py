from rest_framework import filters

from jobs.models import Skill, ProjectSkill


class IsAuthenticatedFilterBackend(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        user_skills = Skill.objects.filter(users__in=request.user.skills.all())
        project_skills = ProjectSkill.objects.filter(skill__in=user_skills)
        return queryset.filter(skills__in=project_skills)

