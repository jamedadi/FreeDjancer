from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from jobs.models import Project
from accounts.api.serializers import UserReadOnlySerializer


class ProjectSerializer(ModelSerializer):
    user = UserReadOnlySerializer()
    status = serializers.CharField(source='get_status_display')

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'user', 'budget', 'status', 'expire_time', 'created_time']
        read_only_fields = ['user', 'status']