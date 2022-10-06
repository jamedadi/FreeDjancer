from rest_framework.serializers import ModelSerializer

from jobs.models import Project


class ProjectSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'user', 'budget', 'status', 'expire_time', 'created_time']
        read_only_fields = ['user', 'status']