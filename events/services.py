from django.core.mail import send_mail
from django.conf import settings

def send_event_registration_email(registration):
    subject = f"ثبت‌نام جدید در رویداد - {registration.event.title}"
    message = f"""
سلام،

یک ثبت‌نام جدید برای رویداد زیر در وب‌سایت مدیران انجام شد:

عنوان رویداد:
{registration.event.title}

اطلاعات شرکت‌کننده:

نام و نام خانوادگی:
{registration.contact_name}

نام سازمان / شرکت:
{registration.company_name}

ایمیل:
{registration.email}

شماره تماس:
{registration.phone}

حوزه فعالیت:
{registration.business_industry}

سمت:
{registration.contact_role}

تاریخ ثبت:
{registration.created_at}

با احترام،
سیستم مدیریت مدیران
"""

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.ADMIN_EMAIL],
        fail_silently=False,
    )