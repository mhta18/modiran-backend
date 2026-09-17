from rest_framework.routers import DefaultRouter

from .views import (
    SolutionViewSet,
    BookViewSet,
    CourseViewSet,
    NewsViewSet,
    MediaViewSet,
    FeedbackViewSet,
)

router = DefaultRouter()

router.register(r"solutions", SolutionViewSet, basename="solution")
router.register(r"books", BookViewSet, basename="book")
router.register(r"courses", CourseViewSet, basename="course")
router.register(r"news", NewsViewSet, basename="news")
router.register(r"media", MediaViewSet, basename="media")
router.register(r"feedback", FeedbackViewSet, basename="feedback")

urlpatterns = router.urls
