from rest_framework.routers import DefaultRouter
from .views import (
    ConsultantViewSet,
    CertificationViewSet,
    ConsultantVideoViewSet,
    ConsultantServiceViewSet,
)

router = DefaultRouter()

router.register(r"consultants", ConsultantViewSet, basename="consultant")
router.register("certifications", CertificationViewSet, basename="certification")
router.register("videos", ConsultantVideoViewSet, basename="consultant-video")
router.register(
    "consultant-services", ConsultantServiceViewSet, basename="consultant-service"
)

urlpatterns = router.urls
