from rest_framework.routers import DefaultRouter

from .views import ConsultationRequestViewSet

router = DefaultRouter()

router.register(
    r"consultation-requests",
    ConsultationRequestViewSet,
    basename="consultation-request",
)

urlpatterns = router.urls
