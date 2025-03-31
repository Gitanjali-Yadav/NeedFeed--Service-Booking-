from django.core.mail import send_mail
from django.conf import settings

def send_verification_email(user):
    subject = 'Verify Your Email Address'
    verification_url = f"http://localhost:8000/api/auth/verify-email/{user.verification_token}/"
    message = f"Click the link to verify your email: {verification_url}"
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])