from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, EventRegistrationCreateView

router = DefaultRouter()
router.register(r"events", EventViewSet, basename="event")

urlpatterns = [
    path(
        "event-registrations/",
        EventRegistrationCreateView.as_view(),
        name="event-registrations",
    ),
    path("", include(router.urls)),
]
