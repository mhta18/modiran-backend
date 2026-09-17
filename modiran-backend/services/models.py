from django.db import models


class ServiceCategory(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان خدمت")

    description = models.TextField(verbose_name="توضیحات خدمت")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "خدمت"
        verbose_name_plural = "خدمات مشاوره"
