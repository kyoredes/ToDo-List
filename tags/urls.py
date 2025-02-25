from rest_framework import routers
from tags.views import TagViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register("", TagViewSet)

urlpatterns = [path("", include(router.urls))]
