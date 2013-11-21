import os

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMultiAlternatives
from scrapdeals.models import SubscribeForm, SubscribeModel



def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def index(request):
    # form = SubscribeForm()
    # context = {'form':form, 'value': 'Submit'}
    # print request
    # current_dir = os.getcwd()
    # os.remove("/Users/ajaikumar/ajai-lab/scrapyenv/deals/scrapdeals/static/items.json")
    # os.chdir("/Users/ajaikumar/ajai-lab/scrapyenv/superdeals")
    # os.system("scrapy crawl superdeal -o /Users/ajaikumar/ajai-lab/scrapyenv/deals/scrapdeals/static/items.json -t json")
    # os.chdir(current_dir)
    # news_letter()
    if not request.user.is_authenticated():
        return render(request, 'image_view.html')
    else:
        return HttpResponseRedirect('auth/auth')

def subscribe(request):
    form = SubscribeForm()
    context = { 'form' : form, 'value'  : 'Subscribe'}
    if request.method == 'POST': 
        form = SubscribeForm(request.POST) 
        try:
            if form.is_valid():
                email = form.cleaned_data['email']
                try:
                    new_user = SubscribeModel()
                    new_user.email = email
                    new_user.save()
                    context = {'value': 'Subscribed'}
                except:
                    context = {'value': 'Already Subscribed'}
            else:
                context = {'form':form, 'value': 'Resubmit'}
        except Exception, e:
            raise e
    return render(request, 'image_view.html', context)