from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import (
    Solution,
    Book,
    Course,
    News,
    Media,
    Feedback,
)


@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "is_active",
        "order",
        "created_at",
    )
    list_filter = ("is_active",)
    search_fields = ("title", "description")
    ordering = ("order",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "is_active",
        "created_at",
    )
    list_filter = ("is_active",)
    search_fields = ("title", "author")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "instructor",
        "duration",
        "is_active",
        "created_at",
    )
    list_filter = ("is_active",)
    search_fields = ("title", "instructor")


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "is_published",
        "published_at",
        "created_at",
    )
    list_filter = ("is_published",)
    search_fields = ("title", "summary", "content")


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "media_type",
        "is_active",
        "created_at",
    )
    list_filter = ("media_type", "is_active")
    search_fields = ("title", "description")


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "company",
        "is_active",
        "order",
        "created_at",
    )
    list_filter = ("is_active",)
    search_fields = ("name", "company", "message")
    ordering = ("order",)
