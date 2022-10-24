from rest_framework import routers

from jobs.api.views import ProjectViewSet

router = routers.SimpleRouter()
router.register('project', ProjectViewSet)

urlpatterns = [

] + router.urls