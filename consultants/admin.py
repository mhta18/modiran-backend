from django.contrib import admin

from .models import (
    Consultant,
    Certification,
    ConsultantVideo,
)

@admin.register(Consultant)
class ConsultantAdmin(admin.ModelAdmin):

    list_display = [
        "name",
        "title",
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
        "title",
        "bio",
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

    search_fields = [
        "title",
        "description",
        "consultant__name",
    ]

    list_filter = [
        "published_at",
    ]
