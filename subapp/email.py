from django.core.mail import EmailMultiAlternatives
from django.conf import settings

def send_email(to):
    subject = 'MGENI Invitation Code'
    from_email = settings.EMAIL_HOST_USER
    to = str(to)
    text_content = 'This is an important message.'
    html_content = '<p>This is an <strong>important</strong> message.</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

