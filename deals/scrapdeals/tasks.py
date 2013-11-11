import os
import json
from django.core.mail import EmailMultiAlternatives
from scrapdeals.models import SubscribeModel
from datetime import timedelta
from celery import task


@task()
def news_letter():
	path = os.path.dirname(os.path.abspath(__file__))+'/static/items.json'
	json_data = open(path)
	flipitems = []
	h8items = []
	infyitems = []
	tradusitems = []
	indiatimesitems = []   
	data = json.load(json_data)
	for key in data:
		if key['website'] == 'flipkart':
			flipitem = {}
			flipitem['deal_name'] = ''.join(key['deal_name'])
			flipitem['image'] = ''.join(key['image'])
			flipitem['original_price'] = ''.join(key['original_price'])
			flipitem['deal_price'] = ''.join(key['deal_price'])
			flipitem['website'] = key['website']
			flipitems.append(flipitem)
			

		elif key['website'] == 'homeshop18':
			h8item = {}
			h8item['deal_name'] = ''.join(key['deal_name'])
			h8item['image'] = ''.join(key['image'])
			h8item['original_price'] = ''.join(key['original_price'])
			h8item['deal_price'] = ''.join(key['deal_price'])
			h8item['website'] = key['website']
			h8items.append(h8item)

		elif key['website'] == 'indiatimes':
			indiatimesitem = {}
			indiatimesitem['deal_name'] = ''.join(key['deal_name'])
			indiatimesitem['image'] = ''.join(key['image'])
			indiatimesitem['original_price'] = ''.join(key['original_price'])
			indiatimesitem['deal_price'] = ''.join(key['deal_price'])
			indiatimesitem['website'] = key['website']
			indiatimesitems.append(indiatimesitem)

		elif key['website'] == 'tradus':
			tradusitem = {}
			tradusitem['deal_name'] = ''.join(key['deal_name'])
			tradusitem['image'] = ''.join(key['image'])
			tradusitem['original_price'] = ''.join(key['original_price'])
			tradusitem['deal_price'] = ''.join(key['deal_price'])
			tradusitem['website'] = key['website']
			tradusitems.append(tradusitem)

		elif key['website'] == 'infibeam':
			infyitem = {}
			infyitem['deal_name'] =  ''.join(key['deal_name'])
			infyitem['image'] = ''.join(key['image'])
			infyitem['original_price'] = ''.join(key['original_price'])
			infyitem['deal_price'] = ''.join(key['deal_price'])
			infyitem['website'] = key['website']
			infyitems.append(infyitem)
		else:
			pass
	json_data.close()

	if flipitems:
		website = flipitems[0]['website']
		image = flipitems[0]['image']
		deal_price = flipitems[0]['deal_price']
		original_price = flipitems[0]['original_price']
		deal_name = flipitems[0]['deal_name']

		flipkart_offer = '<td ><div id="my_box">\
		<h2>'+website+'</h2> <img src="'+image+'" style="width:200px;height:200px;">\
		<p> Rs.'+deal_price+'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <strike> Rs.'\
		+original_price+'</strike></p><p>'+deal_name+'</p></div></td>'
	else:
		flipkart_offer = ''

	if h8items:
		website = h8items[0]['website']
		image = h8items[0]['image']
		deal_price = h8items[0]['deal_price']
		original_price = h8items[0]['original_price']
		deal_name = h8items[0]['deal_name']

		homeshop18_offer = '<td ><div id="my_box">\
		<h2>'+website+'</h2> <img src="'+image+'" style="width:200px;height:200px;">\
		<p> Rs.'+deal_price+'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <strike> Rs.'\
		+original_price+'</strike></p><p>'+deal_name+'</p></div></td>'
	else:
		homeshop18_offer = ''

	if indiatimesitems:
		website = indiatimesitems[0]['website']
		image = indiatimesitems[0]['image']
		deal_price = indiatimesitems[0]['deal_price']
		original_price = indiatimesitems[0]['original_price']
		deal_name = indiatimesitems[0]['deal_name']

		indiatimes_offer =  '<td ><div id="my_box">\
		<h2>'+website+'</h2> <img src="'+image+'" style="width:200px;height:200px;">\
		<p> Rs.'+deal_price+'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <strike> Rs.'\
		+original_price+'</strike></p><p>'+deal_name+'</p></div></td>'
	else:
		indiatimes_offer = ''

	if tradusitems:
		website = tradusitems[0]['website']
		image = tradusitems[0]['image']
		deal_price = tradusitems[0]['deal_price']
		original_price = tradusitems[0]['original_price']
		deal_name = tradusitems[0]['deal_name']

		tradus_offer = '<td ><div id="my_box">\
		<h2>'+website+'</h2> <img src="'+image+'" style="width:200px;height:200px;">\
		<p> Rs.'+deal_price+'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <strike> Rs.'\
		+original_price+'</strike></p><p>'+deal_name+'</p></div></td>'
	else:
		tradus_offer = ''

	if infyitems:
		website = infyitems[0]['website']
		image = infyitems[0]['image']
		deal_price = infyitems[0]['deal_price']
		original_price = infyitems[0]['original_price']
		deal_name = infyitems[0]['deal_name']

		infibeam_offer = '<td ><div id="my_box">\
		<h2>'+website+'</h2> <img src="'+image+'" style="width:200px;height:200px;">\
		<p> Rs.'+deal_price+'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <strike> Rs.'\
		+original_price+'</strike></p><p>'+deal_name+'</p></div></td>'
	else:
		infibeam_offer = ''



	subject, from_addr = 'Subscribe Scrapy', 'info@scarpy.com'
	text_content = 'This is an important message.'
	html_content = '<html><body><link href="http://fonts.googleapis.com/css?family=Overlock+SC|Oxygen|Nunito" rel="stylesheet" type="text/css">\
	<style>#my_box{margin:5px;height:400px; background:rgb(240,238,235);border-radius:5px; border:1px solid rgba(210,208,205,0.7);}\
	p {font-family: Overlock SC, sans-serif; color:rgb(100,98,95); text-align:center; font-weight:bold;}\
	img{border:5px solid white; border-radius:5px; width:100px; display: block; margin:0 auto;}\
	h2{font-family: Nunito, sans-serif;color:rgb(42,166,203); text-align:center;}</style>\
	<table width=auto><tr>'+flipkart_offer+homeshop18_offer+indiatimes_offer+'</tr><tr>\
	'+tradus_offer+infibeam_offer+'</tr></table><p><a href="http://50.19.241.168:8008/" target="_blank">For more items</a> </p></body></html>'
	
	subscribe_list = SubscribeModel.objects.values_list('email', flat=True)
	for email in subscribe_list:
		msg = EmailMultiAlternatives(subject, text_content,from_addr, [str(email)])
		msg.attach_alternative(html_content, "text/html")
		msg.send()
