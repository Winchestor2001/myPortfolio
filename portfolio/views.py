import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView
from django.core.mail import send_mail, EmailMessage

from portfolio.models import Portfolio, MyInfoConfig


def home_page(request):
    project = Portfolio.objects.all()
    myinfo = MyInfoConfig.objects.all()
    context = {'projects': project, 'myinfo': myinfo}
    return render(request, 'base.html', context=context)


def detail_page(request, pk):
    project = Portfolio.objects.filter(id=pk).first()
    print(project)
    context = {'project': project}
    return render(request, 'single-work.html', context=context)


@csrf_exempt
def contact(request):
    token = '827436479:AAGJ2u4Zl83aVMHZtPscb1mw4sUkniNXH1c'
    user_id = 591250245
    if request.method == "POST":
        message_name = request.POST['cf_name']
        message_email = request.POST['cf_email']
        message = request.POST['cf_message']
        context = f"Sender: {message_name}\n" \
                  f"Sender e-mail: {message_email}\n" \
                  f"Sender message: {message}"
        requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={user_id}&text={context}')
        return HttpResponse('correct')
    return redirect('home')


