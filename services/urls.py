from rest_framework.routers import DefaultRouter
from .views import ServiceCategoryViewSet

router = DefaultRouter()

router.register(r"services", ServiceCategoryViewSet, basename="service")

urlpatterns = router.urls
