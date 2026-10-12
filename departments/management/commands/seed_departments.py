# departments/management/commands/seed_departments.py

from django.core.management.base import BaseCommand
from departments.models import Department, Course


class Command(BaseCommand):
    help = "Seed database with initial departments and related courses"

    def handle(self, *args, **kwargs):
        departments_data = [
            {
                "key": "management",
                "title": "دپارتمان مدیریت و استراتژی",
                "description": "آموزش‌های پودمانی و تخصصی در حوزه استراتژی و رهبری سازمانی.",
                "icon": "🏢",
                "courses": [
                    {
                        "title": "مدرسه استراتژی و رهبری",
                        "instructor": "استاد ارشد مدیریت",
                        "duration": "۱۲ ساعت",
                        "course_type": "پودمانی",
                        "level": "پیشرفته",
                        "description": "اصول جامع تدوین و اجرای استراتژی‌های سازمانی.",
                    },
                    {
                        "title": "مدیریت تغییر و تحول سازمانی",
                        "instructor": "دکتر رضایی",
                        "duration": "۱۰ ساعت",
                        "course_type": "پودمانی",
                        "level": "متوسط",
                        "description": "مدیریت گذار سازمان در شرایط بحران و توسعه.",
                    },
                    {
                        "title": "دوره فشرده تفکر سیستمی",
                        "instructor": "مهندس تهرانی",
                        "duration": "۸ ساعت",
                        "course_type": "تک دوره‌ای",
                        "level": "مقدماتی",
                        "description": "نگاهی سیستمی به حل مسائل پیچیده سازمانی.",
                    },
                ],
            },
            {
                "key": "hr",
                "title": "دپارتمان منابع انسانی",
                "description": "توسعه مهارت‌های جذب، نگهداشت و مدیریت سرمایه انسانی.",
                "icon": "👥",
                "courses": [
                    {
                        "title": "مدیریت منابع انسانی پیشرفته",
                        "instructor": "دکتر اکبری",
                        "duration": "۱۶ ساعت",
                        "course_type": "پودمانی",
                        "level": "پیشرفته",
                        "description": "استراتژی‌های نوین مدیریت منابع انسانی.",
                    },
                    {
                        "title": "مصاحبه و جذب استعدادها",
                        "instructor": "سارا کریمی",
                        "duration": "۶ ساعت",
                        "course_type": "کارگاهی",
                        "level": "متوسط",
                        "description": "تکنیک‌های حرفه‌ای مصاحبه استخدامی.",
                    },
                ],
            },
            {
                "key": "sales",
                "title": "دپارتمان بازاریابی و فروش",
                "description": "افزایش فروش، بازاریابی دیجیتال و تکنیک‌های مذاکره پیشرفته.",
                "icon": "📢",
                "courses": [
                    {
                        "title": "مدیریت استراتژیک بازاریابی",
                        "instructor": "آرش سلطانی",
                        "duration": "۱۴ ساعت",
                        "course_type": "پودمانی",
                        "level": "پیشرفته",
                        "description": "تدوین کمپین و تحلیل بازار هدف.",
                    },
                    {
                        "title": "تکنیک‌های حرفه‌ای فروش و مذاکره",
                        "instructor": "کامران مولایی",
                        "duration": "۸ ساعت",
                        "course_type": "حضوری",
                        "level": "متوسط",
                        "description": "مهارت‌های کلیدی متقاعدسازی مشتری.",
                    },
                ],
            },
            {
                "key": "it",
                "title": "دپارتمان فناوری اطلاعات (IT)",
                "description": "امنیت شبکه، زیرساخت، هوش مصنوعی و تحول دیجیتال.",
                "icon": "💻",
                "courses": [
                    {
                        "title": "امنیت شبکه و داده‌ها",
                        "instructor": "مهندس راد",
                        "duration": "۲۰ ساعت",
                        "course_type": "پودمانی",
                        "level": "پیشرفته",
                        "description": "حفاظت از زیرساخت‌های فناوری اطلاعات.",
                    },
                    {
                        "title": "هوش مصنوعی در مدیریت",
                        "instructor": "دکتر عارف",
                        "duration": "۱۲ ساعت",
                        "course_type": "آنلاین",
                        "level": "متوسط",
                        "description": "کاربرد ابزارهای مدرن هوش مصنوعی در کسب‌وکار.",
                    },
                ],
            },
            {
                "key": "erp",
                "title": "دپارتمان صنایع و ERP",
                "description": "پیاده‌سازی سیستم‌های برنامه‌ریزی منابع سازمان و مدیریت زنجیره تامین.",
                "icon": "⚙️",
                "courses": [
                    {
                        "title": "پیاده‌سازی ERP در سازمان",
                        "instructor": "مهندس ناصری",
                        "duration": "۲۴ ساعت",
                        "course_type": "پودمانی",
                        "level": "پیشرفته",
                        "description": "مراحل استقرار و استقرار سیستم‌های یکپارچه.",
                    },
                    {
                        "title": "مدیریت زنجیره تامین (SCM)",
                        "instructor": "دکتر مرادی",
                        "duration": "۱۵ ساعت",
                        "course_type": "پودمانی",
                        "level": "متوسط",
                        "description": "بهینه‌سازی لجستیک و انبارداری.",
                    },
                ],
            },
            {
                "key": "finance",
                "title": "دپارتمان مالی و بازرگانی",
                "description": "مدیریت مالی برای مدیران، بودجه‌ریزی و قوانین مالیاتی.",
                "icon": "💰",
                "courses": [
                    {
                        "title": "مدیریت مالی برای مدیران غیرمالی",
                        "instructor": "دکتر همتی",
                        "duration": "۱۲ ساعت",
                        "course_type": "پودمانی",
                        "level": "مقدماتی",
                        "description": "درک صورت‌های مالی و بودجه‌بندی.",
                    },
                    {
                        "title": "قوانین مالیاتی و اظهارنامه",
                        "instructor": "استاد فلاح",
                        "duration": "۱۰ ساعت",
                        "course_type": "کارگاهی",
                        "level": "متوسط",
                        "description": "آشنایی با آخرین قوانین مالیاتی و بیمه.",
                    },
                ],
            },
            {
                "key": "iso",
                "title": "دپارتمان استقرار ISO و کیفیت",
                "description": "طراحی و استقرار استانداردهای ایزو، ممیزی و مدیریت کیفیت.",
                "icon": "🥇",
                "courses": [
                    {
                        "title": "پیاده‌سازی ISO 9001:2015",
                        "instructor": "مهندس پاک‌نیت",
                        "duration": "۱۶ ساعت",
                        "course_type": "پودمانی",
                        "level": "متوسط",
                        "description": "سیستم مدیریت کیفیت و ممیزی داخلی.",
                    },
                    {
                        "title": "مدیریت ایمنی و بهداشت (HSE)",
                        "instructor": "دکتر شکوهی",
                        "duration": "۱۴ ساعت",
                        "course_type": "حضوری",
                        "level": "پیشرفته",
                        "description": "ارزیابی ریسک و ایمنی صنعتی.",
                    },
                ],
            },
            {
                "key": "legal",
                "title": "دپارتمان حقوقی و قراردادها",
                "description": "حقوق کسب‌وکار، تنظیم قراردادهای تجاری و دعاوی کار.",
                "icon": "⚖️",
                "courses": [
                    {
                        "title": "اصول نگارش و تنظیم قراردادها",
                        "instructor": "دکتر دادگر",
                        "duration": "۱۰ ساعت",
                        "course_type": "پودمانی",
                        "level": "پیشرفته",
                        "description": "نکات حقوقی مهم در قراردادهای تجاری و شرکتی.",
                    },
                    {
                        "title": "قوانین کار و تامین اجتماعی",
                        "instructor": "وکیل منصوری",
                        "duration": "۸ ساعت",
                        "course_type": "آنلاین",
                        "level": "متوسط",
                        "description": "بررسی روابط کارگر و کارفرما بر اساس قانون.",
                    },
                ],
            },
        ]

        for dept_data in departments_data:
            courses_data = dept_data.pop("courses")
            department, created = Department.objects.update_or_create(
                key=dept_data["key"], defaults=dept_data
            )

            for course_data in courses_data:
                Course.objects.update_or_create(
                    title=course_data["title"],
                    department=department,
                    defaults=course_data,
                )

        self.stdout.write(
            self.style.SUCCESS("Successfully seeded departments and courses!")
        )
