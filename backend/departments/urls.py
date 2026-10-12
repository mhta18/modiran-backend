from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, DepartmentViewSet

router = DefaultRouter()
router.register(r"departments", DepartmentViewSet, basename="department")
router.register(r"courses", CourseViewSet, basename="course")

urlpatterns = router.urls