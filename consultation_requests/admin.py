from django.contrib import admin

from .models import ConsultationRequest


@admin.register(ConsultationRequest)
class ConsultationRequestAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "company_name",
        "service",
        "consultant",
        "created_at",
    )

    list_filter = (
        "service",
        "consultant",
        "created_at",
    )

    search_fields = (
        "company_name",
        "user__username",
        "description",
    )
