from django.db import models

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

    company_name = models.CharField(max_length=150, verbose_name="نام سازمان / شرکت")

    contact_name = models.CharField(max_length=100, verbose_name="نام درخواست‌دهنده")

    email = models.EmailField(verbose_name="ایمیل")

    phone = models.CharField(max_length=20, verbose_name="شماره تماس")

    business_industry = models.ForeignKey(
        BusinessIndustry,
        on_delete=models.PROTECT,
        related_name="consultation_requests",
        verbose_name="حوزه فعالیت"
    )

    contact_role = models.ForeignKey(
        ContactRole,
        on_delete=models.PROTECT,
        related_name="consultation_requests",
        verbose_name="سمت درخواست‌دهنده"
    )
    consultant_service = models.ForeignKey(
        ConsultantService,
        on_delete=models.PROTECT,
        related_name="consultation_requests",
        verbose_name="خدمت و مشاور انتخاب‌شده",
    )

    description = models.TextField(verbose_name="شرح نیاز و عارضه‌های سازمان")

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="تاریخ ثبت درخواست"
    )

    def __str__(self):
        return (
            f"درخواست {self.company_name} - "
            f"{self.consultant_service.consultant.name}"
        )

    class Meta:
        verbose_name = "درخواست مشاوره"
        verbose_name_plural = "درخواست‌های مشاوره"
        ordering = ["-created_at"]
