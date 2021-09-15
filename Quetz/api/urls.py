from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import UserViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="usuarios")

urlpatterns = [
    path("", include(router.urls)),
]
