from rest_framework.routers import DefaultRouter

from .views import (
    SolutionViewSet,
    BookViewSet,
    NewsViewSet,
    FeedbackViewSet,
)

router = DefaultRouter()

router.register(r"solutions", SolutionViewSet, basename="solution")
router.register(r"books", BookViewSet, basename="book")
router.register(r"news", NewsViewSet, basename="news")
router.register(r"feedbacks", FeedbackViewSet, basename="feedback")

urlpatterns = router.urls
