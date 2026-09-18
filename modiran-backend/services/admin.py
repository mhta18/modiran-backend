from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ServiceCategory


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    # Columns displayed in the list view table
    list_display = ("id", "title", "short_description")

    # Search bar enabling searches by service title or description
    search_fields = ("title", "description")

    ordering = ("title",)

    list_per_page = 20

    @admin.display(description="توضیحات کوتاه")
    def short_description(self, obj):
        if obj.description and len(obj.description) > 60:
            return f"{obj.description[:60]}..."
        return obj.description
