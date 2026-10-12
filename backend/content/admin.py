from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import (
    Solution,
    Book,
    News,
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
