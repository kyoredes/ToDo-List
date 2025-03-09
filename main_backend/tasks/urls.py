from rest_framework import routers
from tasks.views import TaskViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register("", TaskViewSet)

urlpatterns = [path("", include(router.urls))]
