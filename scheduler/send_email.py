from django.core.mail import EmailMultiAlternatives, EmailMessage
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from SmartForm import settings
from smart_formApp.forms import UserForm
from smart_formApp.models import User


def send_once_email( email):

    # send a confirmation mail
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email,]

    subject, from_email, to = 'NewsLetter Subscription', email_from, email

    context = {'first_name':"ELG-Fireamrs Member",
               'last_name':"",
               'body': 'Just testing water maybe this will work but it may not work'}

    message_html = render_to_string('email_templates/thankyou.html', context)


    email_message = EmailMessage(subject, '', from_email, recipient_list)
    email_message.content_subtype = "html"
    email_message.body = message_html
    email_message.send()


    print("Email was Sent!!")
    return True


def welcome_email(email, first_name, last_name):
    try:
        # send a confirmation mail
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email,]

        subject, from_email, to = 'NewsLetter Subscription', email_from, email

        context = {'first_name':first_name,
                   'last_name':last_name,
                   'body': 'Just testing water maybe this will work but it may not work'}

        message_html = render_to_string('email_templates/thankyou.html', context)
        email_message = EmailMessage(subject, '', from_email, recipient_list)
        email_message.content_subtype = "html"
        email_message.body = message_html
        email_message.send()

        print("Email was Sent!!################################")
        return True
    except:
        return False
