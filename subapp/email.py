from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from postmarker.core import PostmarkClient

postmark = PostmarkClient(server_token='92895c56-a7c3-4525-8a99-0bc297b6d354')
# send email function
def send_email():
    postmark.emails.send(
        From= "rmbugua@mgeniapp.com",
        To= "allan@bharathbrands.in",
        Subject= "Hello from Postmark",
        HtmlBody= "<strong>Hello</strong> dear Postmark user.",
        MessageStream="message"
    )
    
