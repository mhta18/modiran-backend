from django.contrib import admin
from .models import Course
# Register your models here.


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
