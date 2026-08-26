from django.db import models

from consultants.models import Consultant
from services.models import ServiceCategory


class ConsultationRequest(models.Model):

    company_name = models.CharField(max_length=150, verbose_name="نام سازمان / شرکت")

    contact_name = models.CharField(max_length=100, verbose_name="نام درخواست‌دهنده")

    email = models.EmailField(verbose_name="ایمیل")

    phone = models.CharField(max_length=20, verbose_name="شماره تماس")

    service = models.ForeignKey(
        ServiceCategory,
        on_delete=models.PROTECT,
        related_name="consultation_requests",
        verbose_name="نوع خدمت مورد نیاز",
    )

    consultant = models.ForeignKey(
        Consultant,
        on_delete=models.PROTECT,
        related_name="consultation_requests",
        verbose_name="مشاور انتخاب‌شده",
    )

    description = models.TextField(verbose_name="شرح نیاز و عارضه‌های سازمان")

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="تاریخ ثبت درخواست"
    )

    def __str__(self):
        return f"درخواست {self.company_name} - " f"{self.consultant.name}"

    class Meta:
        verbose_name = "درخواست مشاوره"
        verbose_name_plural = "درخواست‌های مشاوره"
        ordering = ["-created_at"]
