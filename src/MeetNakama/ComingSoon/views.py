from django.shortcuts import render
from django.contrib import messages
from django.conf import settings

from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError

api_key = settings.MAILCHIMP_API_KEY
server = settings.MAILCHIMP_DATA_CENTER
list_id = settings.MAILCHIMP_EMAIL_LIST_ID

# Create your views here.
def subscribe(email):

    mailchimp = Client()
    mailchimp.set_config({
        "api_key": api_key,
        "server": server,
    })

    member_info = {
        "email_address": email,
        "status": "subscribed",
    }

    try:
        response = mailchimp.lists.add_list_member(list_id, member_info)
        print("response: {}".format(response))
    except ApiClientError as error:
        print("An exception occured: {}".format(error.text))


def ComingSoon(request):

    if request.method == "POST":
        email = request.POST['email']
        print(email)
        subscribe(email)
        messages.success(request, "Email received. Thank you!")

    return render(request, 'index.html')
