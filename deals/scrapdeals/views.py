import os

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def index(request):
	# print request
	# current_dir = os.getcwd()
	# os.remove("/Users/ajaikumar/ajai-lab/scrapyenv/deals/scrapdeals/static/items.json")
	# os.chdir("/Users/ajaikumar/ajai-lab/scrapyenv/superdeals")
	# os.system("scrapy crawl superdeal -o /Users/ajaikumar/ajai-lab/scrapyenv/deals/scrapdeals/static/items.json -t json")
	# os.chdir(current_dir)
	return render(request,'image_view.html')