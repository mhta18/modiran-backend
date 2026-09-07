from django.core.mail import send_mail
from django.conf import settings


def send_consultation_request_email(consultation_request):
    subject = f"درخواست مشاوره جدید - {consultation_request.company_name}"

    # Determine if it's a specific consultant request or a general request
    if consultation_request.consultant_service:
        request_type = "درخواست اختصاصی (با مشاور)"
        consultant_name = consultation_request.consultant_service.consultant.name
        service_title = consultation_request.consultant_service.service.title
    else:
        request_type = "درخواست عمومی (بدون مشاور)"
        consultant_name = "انتخاب نشده (درخواست عمومی)"
        service_title = (
            consultation_request.service.title
            if consultation_request.service
            else "مشخص نشده"
        )

    message = f"""
سلام،

یک درخواست مشاوره جدید در سایت مدیران ثبت شده است.

نوع درخواست:
{request_type}

اطلاعات درخواست:

نام سازمان:
{consultation_request.company_name}

نام درخواست‌دهنده:
{consultation_request.contact_name}

ایمیل:
{consultation_request.email}

شماره تماس:
{consultation_request.phone}

مشاور انتخاب‌شده:
{consultant_name}

خدمت مورد نیاز:
{service_title}

شرح درخواست:
{consultation_request.description}

تاریخ ثبت:
{consultation_request.created_at}

لطفاً درخواست را بررسی و پیگیری کنید.

با احترام
مدیران
"""

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.ADMIN_EMAIL],
        fail_silently=False,
    )
