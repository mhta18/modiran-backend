from django.db import models
from consultants.models import Consultant


class Event(models.Model):

    title = models.CharField(max_length=200, verbose_name="عنوان سمینار / کنفرانس")

    consultant = models.ForeignKey(
        Consultant,
        on_delete=models.CASCADE,
        related_name="events",
        verbose_name="سخنران / مدرس",
    )

    date_held = models.DateTimeField(verbose_name="تاریخ برگزاری")

    description = models.TextField(verbose_name="توضیحات رویداد")

    price = models.DecimalField(
        max_digits=12, decimal_places=0, default=0, verbose_name="هزینه ثبت‌نام"
    )

    location = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="محل برگزاری"
    )

    capacity = models.PositiveIntegerField(blank=True, null=True, verbose_name="ظرفیت")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "رویداد / سمینار"
        verbose_name_plural = "سمینارها و کنفرانس‌ها"
        ordering = ["-date_held"]
