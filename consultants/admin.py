from django.contrib import admin

from .models import (
    Consultant,
    Certification,
    ConsultantVideo,
    ConsultantAvailability,
)


@admin.register(Consultant)
class ConsultantAdmin(admin.ModelAdmin):

    list_display = [
        "name",
        "email",
        "experience_years",
        "is_verified",
        "projects_count",
        "companies_count",
    ]

    list_filter = [
        "is_verified",
    ]

    search_fields = [
        "name",
        "email",
        "bio",
    ]

    ordering = [
        "-created_at",
    ]


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):

    list_display = [
        "title",
        "consultant",
        "issuer",
        "issue_date",
        "expiration_date",
    ]

    list_filter = [
        "issuer",
        "issue_date",
    ]

    search_fields = [
        "title",
        "issuer",
        "certificate_number",
        "consultant__name",
    ]


@admin.register(ConsultantVideo)
class ConsultantVideoAdmin(admin.ModelAdmin):

    list_display = [
        "title",
        "consultant",
        "published_at",
        "created_at",
    ]

    list_filter = [
        "published_at",
    ]

    search_fields = [
        "title",
        "description",
        "consultant__name",
    ]

    ordering = [
        "-published_at",
        "-created_at",
    ]


@admin.register(ConsultantAvailability)
class ConsultantAvailabilityAdmin(admin.ModelAdmin):

    list_display = [
        "consultant",
        "day_name",
        "start_time",
        "end_time",
        "is_available",
    ]

    list_filter = [
        "day_of_week",
        "is_available",
    ]

    search_fields = [
        "consultant__name",
    ]

    ordering = [
        "day_of_week",
        "start_time",
    ]

    @admin.display(description="روز هفته")
    def day_name(self, obj):
        return obj.get_day_of_week_display()
