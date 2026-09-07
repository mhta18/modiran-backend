from django.db import models

from services.models import ServiceCategory
from consultants.models import ConsultantService


class ContactRole(models.Model):

    title = models.CharField(max_length=100, unique=True, verbose_name="سمت")

    is_active = models.BooleanField(default=True, verbose_name="فعال")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "سمت درخواست‌دهنده"
        verbose_name_plural = "سمت‌های درخواست‌دهنده"


class BusinessIndustry(models.Model):

    title = models.CharField(max_length=150, unique=True, verbose_name="حوزه کسب‌وکار")

    is_active = models.BooleanField(default=True, verbose_name="فعال")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "حوزه کسب‌وکار"
        verbose_name_plural = "حوزه‌های کسب‌وکار"


class ConsultationRequest(models.Model):

    INDUSTRY_CHOICES = [
        ("IT", "فناوری اطلاعات"),
        ("MANUFACTURING", "تولیدی"),
        ("FOOD", "صنایع غذایی"),
        ("PHARMA", "دارویی"),
        ("FINANCE", "مالی و بانکی"),
        ("CONSTRUCTION", "ساختمان و عمران"),
        ("OTHER", "سایر"),
    ]

    CONTACT_ROLE_CHOICES = [
        ("CEO", "مدیرعامل"),
        ("CEO_OFFICE", "دفتر مدیرعامل"),
        ("HR", "مدیر منابع انسانی"),
        ("FINANCE", "مدیر مالی"),
        ("IT_MANAGER", "مدیر فناوری اطلاعات"),
        ("OTHER", "سایر"),
    ]

    company_name = models.CharField(max_length=150, verbose_name="نام سازمان / شرکت")

    contact_name = models.CharField(max_length=100, verbose_name="نام درخواست‌دهنده")

    email = models.EmailField(verbose_name="ایمیل")

    phone = models.CharField(max_length=20, verbose_name="شماره تماس")

    business_industry = models.CharField(
        max_length=30, choices=INDUSTRY_CHOICES, verbose_name="حوزه فعالیت"
    )

    contact_role = models.CharField(
        max_length=30, choices=CONTACT_ROLE_CHOICES, verbose_name="سمت درخواست‌دهنده"
    )

    service = models.ForeignKey(
        ServiceCategory,
        on_delete=models.PROTECT,
        related_name="consultation_requests",
        verbose_name="خدمت مورد نظر",
        null=True,  
        blank=True,
    )

    consultant_service = models.ForeignKey(
        ConsultantService,
        on_delete=models.PROTECT,
        related_name="consultation_requests",
        verbose_name="خدمت و مشاور انتخاب‌شده",
        null=True,
        blank=True,
    )

    description = models.TextField(verbose_name="شرح نیاز و عارضه‌های سازمان")

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="تاریخ ثبت درخواست"
    )

    def __str__(self):
        if self.consultant_service:
            consultant_name = self.consultant_service.consultant.name
            return f"درخواست {self.company_name} - {consultant_name}"

        return f"درخواست {self.company_name} - درخواست عمومی"

    class Meta:
        verbose_name = "درخواست مشاوره"
        verbose_name_plural = "درخواست‌های مشاوره"
        ordering = ["-created_at"]
