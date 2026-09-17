from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import (
    Solution,
    Book,
    Course,
    News,
    Media,
    Feedback,
)

from .serializers import (
    SolutionSerializer,
    BookSerializer,
    CourseSerializer,
    NewsSerializer,
    MediaSerializer,
    FeedbackSerializer,
)


class SolutionViewSet(viewsets.ModelViewSet):
    serializer_class = SolutionSerializer

    def get_queryset(self):
        return Solution.objects.filter(is_active=True).order_by("order")


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.filter(is_active=True).order_by("-created_at")


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer

    def get_queryset(self):
        return Course.objects.filter(is_active=True).order_by("-created_at")


class NewsViewSet(viewsets.ModelViewSet):
    serializer_class = NewsSerializer

    def get_queryset(self):
        return News.objects.filter(is_published=True).order_by(
            "-published_at", "-created_at"
        )


class MediaViewSet(viewsets.ModelViewSet):
    serializer_class = MediaSerializer

    def get_queryset(self):
        return Media.objects.filter(is_active=True).order_by("-created_at")


class FeedbackViewSet(viewsets.ModelViewSet):
    serializer_class = FeedbackSerializer

    def get_queryset(self):
        return Feedback.objects.filter(is_active=True).order_by("order")
