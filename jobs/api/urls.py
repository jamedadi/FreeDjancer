from rest_framework import routers

from jobs.api.views import ProjectViewSet, UserSkillProjectViewSet


router = routers.SimpleRouter()
router.register(r'projects', ProjectViewSet)
router.register('userskillprojects', UserSkillProjectViewSet)

urlpatterns = [

] + router.urls