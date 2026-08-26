from rest_framework.routers import DefaultRouter
from .views import (
    ConsultantViewSet,
    CertificationViewSet,
    ConsultantVideoViewSet,
)

router = DefaultRouter()

router.register(r"consultants", ConsultantViewSet, basename="consultant")
router.register("certifications", CertificationViewSet, basename="certification")
router.register("videos", ConsultantVideoViewSet, basename="consultant-video")

urlpatterns = router.urls
