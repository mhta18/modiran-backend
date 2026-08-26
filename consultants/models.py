from django.db import models


class Consultant(models.Model):

    name = models.CharField(max_length=100, verbose_name="نام و نام خانوادگی")
    
    email = models.EmailField(
        unique=True,
        verbose_name="ایمیل"
    )

    title = models.CharField(max_length=150, verbose_name="عنوان شغلی / تخصص اصلی")

    bio = models.TextField(verbose_name="بیوگرافی")

    experience_years = models.PositiveIntegerField(
        default=0, verbose_name="سابقه کار (سال)"
    )

    image_url = models.URLField(blank=True, null=True, verbose_name="لینک عکس")

    is_verified = models.BooleanField(default=False, verbose_name="مشاور تایید شده")

    response_time = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="زمان پاسخگویی"
    )

    projects_count = models.PositiveIntegerField(
        default=0, verbose_name="تعداد پروژه‌ها"
    )

    companies_count = models.PositiveIntegerField(
        default=0, verbose_name="تعداد شرکت‌های مشاوره داده شده"
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    updated_at = models.DateTimeField(auto_now=True, verbose_name="آخرین بروزرسانی")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "مشاور"
        verbose_name_plural = "مشاوران"
        ordering = ["-created_at"]


class Certification(models.Model):

    consultant = models.ForeignKey(
        Consultant,
        on_delete=models.CASCADE,
        related_name="certifications",
        verbose_name="مشاور",
    )

    title = models.CharField(max_length=200, verbose_name="عنوان گواهینامه")

    issuer = models.CharField(max_length=200, verbose_name="صادرکننده")

    certificate_number = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="شماره گواهینامه"
    )

    issue_date = models.DateField(blank=True, null=True, verbose_name="تاریخ صدور")

    expiration_date = models.DateField(
        blank=True, null=True, verbose_name="تاریخ انقضا"
    )

    document_url = models.URLField(blank=True, null=True, verbose_name="لینک مدرک")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    def __str__(self):
        return f"{self.title} - {self.consultant.name}"

    class Meta:
        verbose_name = "گواهینامه"
        verbose_name_plural = "گواهینامه‌ها"
        ordering = ["-issue_date"]


class ConsultantVideo(models.Model):

    consultant = models.ForeignKey(
        Consultant,
        on_delete=models.CASCADE,
        related_name="videos",
        verbose_name="مشاور",
    )

    title = models.CharField(max_length=200, verbose_name="عنوان ویدیو")

    description = models.TextField(blank=True, verbose_name="توضیحات")

    video_url = models.URLField(verbose_name="لینک ویدیو")

    thumbnail_url = models.URLField(
        blank=True, null=True, verbose_name="لینک تصویر ویدیو"
    )

    published_at = models.DateTimeField(
        blank=True, null=True, verbose_name="تاریخ انتشار"
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    def __str__(self):
        return f"{self.title} - {self.consultant.name}"

    class Meta:
        verbose_name = "ویدیو مشاور"
        verbose_name_plural = "ویدیوهای مشاوران"
        ordering = ["-published_at", "-created_at"]


class ConsultantAvailability(models.Model):

    DAYS_OF_WEEK = [
        (0, "شنبه"),
        (1, "یکشنبه"),
        (2, "دوشنبه"),
        (3, "سه‌شنبه"),
        (4, "چهارشنبه"),
        (5, "پنجشنبه"),
        (6, "جمعه"),
    ]

    consultant = models.ForeignKey(
        Consultant,
        on_delete=models.CASCADE,
        related_name="availabilities",
        verbose_name="مشاور",
    )

    day_of_week = models.IntegerField(choices=DAYS_OF_WEEK, verbose_name="روز هفته")

    start_time = models.TimeField(verbose_name="ساعت شروع")

    end_time = models.TimeField(verbose_name="ساعت پایان")

    is_available = models.BooleanField(default=True, verbose_name="فعال")

    def __str__(self):
        return f"{self.consultant.name} - " f"{self.get_day_of_week_display()}"

    class Meta:
        verbose_name = "زمان دسترسی مشاور"
        verbose_name_plural = "زمان‌های دسترسی مشاوران"
        ordering = ["day_of_week", "start_time"]
