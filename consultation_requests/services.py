from django.core.mail import send_mail
from django.conf import settings


def send_consultation_request_email(consultation_request):

    consultant = consultation_request.consultant

    subject = f"درخواست مشاوره جدید - " f"{consultation_request.company_name}"

    message = f"""
سلام {consultant.name}

یک درخواست مشاوره جدید برای شما ثبت شده است.

نام سازمان:
{consultation_request.company_name}

نام درخواست‌دهنده:
{consultation_request.contact_name}

ایمیل:
{consultation_request.email}

شماره تماس:
{consultation_request.phone}

خدمت مورد نیاز:
{consultation_request.service.title}

شرح درخواست:
{consultation_request.description}

تاریخ ثبت:
{consultation_request.created_at}

لطفاً درخواست را بررسی کنید.

با احترام
مدیران
"""

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[consultant.email],
        fail_silently=False,
    )
