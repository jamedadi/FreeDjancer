from django.urls import path
from rest_framework import routers

from jobs.views import ProjectViewSet

router = routers.SimpleRouter()
router.register(r'project', ProjectViewSet)

urlpatterns = [

] + router.urls