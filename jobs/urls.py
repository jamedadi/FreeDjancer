from django.urls import include, path
from rest_framework import routers

from jobs.api.views import ProjectViewSet, UserSkillProjectViewSet


router = routers.SimpleRouter()
router.register(r'projects', ProjectViewSet, basename='projects')
router.register('userskillprojects', UserSkillProjectViewSet,
                basename='userskillprojects')

urlpatterns = [
    path('', include(router.urls)),
]