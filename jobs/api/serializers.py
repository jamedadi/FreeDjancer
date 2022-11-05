from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from jobs.models import Project, Budget, ProjectSkill
from accounts.api.serializers import UserReadOnlySerializer, SkillSerializer


class BudgetSerializer(ModelSerializer):

    class Meta:
        model = Budget
        fields = ['id', 'title', 'min_price', 'max_price']


class ProjectSkillSerializer(ModelSerializer):
    skill = SkillSerializer()

    class Meta:
        model = ProjectSkill
        fields = ['id', 'skill']


class ProjectSerializer(ModelSerializer):
    user = UserReadOnlySerializer()
    status = serializers.CharField(source='get_status_display')
    budget = BudgetSerializer()
    skills = ProjectSkillSerializer(many=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'user', 'budget', 'skills', 'status', 'expire_time', 'created_time']
        read_only_fields = ['user', 'status']