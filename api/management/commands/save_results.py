import csv
from api.models import User


from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.conf import settings


def send_first_email(recEmail, recName):
    html_tpl_path = 'email_templates/index1.html'
    context_data = {'name': recName}
    email_html_template = get_template(html_tpl_path).render(context_data)
    receiver_email = recEmail
    email_msg = EmailMessage('Join Your New Community',
                             email_html_template,
                             settings. APPLICATION_EMAIL,
                             [receiver_email],
                             reply_to=[settings.APPLICATION_EMAIL]
                             )

    email_msg.content_subtype = 'html'
    email_msg.send(fail_silently=False)

with open('output11.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        try:
            user = User(last_name=line[0], first_name=line[1], email=line[2], school=line[3])
            user.save()
            #send_first_email(line[2], line[1])
        except:
            pass
