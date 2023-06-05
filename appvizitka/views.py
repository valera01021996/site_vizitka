from django.http import HttpResponse
from django.shortcuts import render
import os
from dotenv import load_dotenv
import requests


# Create your views here.

load_dotenv()



def index(request):
    return render(request, "appvizitka/index.html")


def test_page(request):
    name = request.POST['name']
    number = request.POST['phone']
    token = os.getenv("BOT_TOKEN")
    requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id=43031788&text={name} {number}")
    return render(request, "appvizitka/test.html", {'name': name,
                                                    'phone': number})
