from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from superdeals.items import SuperdealsItem

import socket
ip = socket.gethostbyname(socket.gethostname())

from scrapy import log
log.msg('ip= '+ip)

class SuperDealsSpider(BaseSpider):
	"""
	Base spider which defines the url's to be scraped
	"""
	name = "superdeal"
	allowed_domains = ["http://www.homeshop18.com/","http://www.flipkart.com","http://www.infibeam.com/","http://www.tradus.com/","http://www.indiatimes.com"]
	start_urls = [
		"http://www.homeshop18.com/superdeals/",
		"http://www.flipkart.com/offers/electronics",
		"http://www.flipkart.com/offers/fashion",
		"http://www.flipkart.com/offers/books-and-more",
		"http://www.infibeam.com/Hot_Deals/search",
		"http://www.tradus.com/deals",
		"http://shopping.indiatimes.com/deals/"
		# "http://192.168.1.116:8000/"
	]

	def parse(self, response):
		"""
		scraping data from various shopping websites
		"""
		hxs = HtmlXPathSelector(response)
		sites = hxs.select('//ul[@id="liveDealsList"]/li')
		flips = hxs.select("//div[@class='unit size1of3']/div[@class]")
		infy = hxs.select("//div[@id='resultsPane']/div/ul[@class='srch_result default']/li")
		tradus = hxs.select("//div[@class='cartListDiv']/div[@class='cartList filt']")
		indiatimes = hxs.select("//div[@class='productlisting']/div[@class='productrow']/ul[@class='overview']/div[@class='productcoloumn zur ']")
		items = []
		flipitems = []
		infyitems = []
		tradusitems = []
		indiatimesitems = []
		for site in sites:
			item = SuperdealsItem()
			item['deal_name'] = site.select('p[@class="name"]/a/span/text()').extract()
			# item['sub_name'] = site.select('h4/text()').extract()
			item['url'] = site.select('p[@class="name"]/a/@href').extract()
			# item['contents'] = site.select('span[@class="product_title"]/text()').extract()
			item['image'] = site.select('div/a/img/@src').extract()
			item['original_price'] = site.select('p[@class="price"]/em/span[@id]/text()').extract()
			item['deal_price'] = site.select('p[@class="price"]/span[@id]/text()').extract()
			item['validity'] = site.select('p[@class="timer"]/span[@id]/text()').extract()
			item['coupon'] = site.select('p[@class="discount"]/span[@class="coupon"]/text()').extract()
			item['discount'] = ''
			item['website'] = 'homeshop18'
			item['web_image'] = 'http://stat2.homeshop18.com/homeshop18/cms_hydrant/widgets/HS18Logo/HorizontalBannerImage_1365544594659.png'
			items.append(item)

		for flip in flips:
			flipitem = SuperdealsItem()
			flipitem['deal_name'] = flip.select("a[@class='productInfo']/div[@class='title']/b/text()").extract()
			url = flip.select("a[@class='productInfo']/@href").extract()
			appendurl = 'http://www.flipkart.com'
			flipitem['url'] = [appendurl+s for s in url]
			flipitem['image'] = flip.select("a[@class='productInfo']/div[@class='image']/img/@data-src").extract()
			original_price = flip.select("div[@class='priceInfo']/div[@class='priceBox beforeDiscount']/div[@class='price']/text()").extract()
			flipitem['original_price'] = [s.split('. ')[1].replace(",","") for s in original_price]
			deal_price = flip.select("div[@class='priceInfo']/div[@class='priceBox']/div[@class='price']/text()").extract()
			flipitem['deal_price'] = [s.split('. ')[1].replace(",","") for s in deal_price]
			flipitem['validity'] = ''
			flipitem['coupon'] = ''
			flipitem['discount'] = flip.select("a[@class='productInfo']/div[@class='offerTag DISCOUNT']/div[@class='offerText']/text()").extract()
			flipitem['website'] = 'flipkart'
			flipitem['web_image'] = 'http://img6a.flixcart.com/www/prod/images/flipkart_india-5ef1726d.png'
			flipitems.append(flipitem)

		for x in infy:
			infyitem = SuperdealsItem()
			appendurl = 'http://www.infibeam.com'
			url = x.select("a/@href").extract()
			infyitem['url'] = [appendurl+s for s in url]
			infyitem['image'] = x.select("a/img/@src").extract()
			infyitem['deal_name'] = x.select("a/span[@class='title']/text()").extract()
			discount = x.select("a/span[@class='discount']/img/@src").extract()
			infyitem['discount'] = [s.split('/')[6].split('.')[0] + ' %'+' off' for s in discount]
			deal_price = x.select("div[@class='price']/span[@class='normal' or @class='price']/text()").extract()
			infyitem['deal_price'] = [s.replace(",","") for s in deal_price]
			original_price = x.select("div[@class='price']/span[@class='scratch']/text()").extract()
			infyitem['original_price'] = [s.replace(",","") for s in original_price]
			infyitem['coupon'] = ''
			infyitem['validity'] = ''
			infyitem['website'] = 'infibeam'
			infyitem['web_image'] = 'http://www.infibeam.com/assets/skins/common/images/infibeam_logo.png'
			infyitems.append(infyitem)

		for x in tradus:
			tradusitem = SuperdealsItem()
			tradusitem['deal_name'] = x.select("div[@class='DiscountDiv']/a/text()").extract()
			url = x.select("div[@class='DiscountDiv']/a/@href").extract()
			appendurl = 'http://www.tradus.com'
			tradusitem['url'] = [appendurl+s for s in url]
			tradusitem['deal_price'] = x.select("div[@class='Discount_bg']/div[@class='signDiv2']/text()")[1].extract()
			tradusitem['image'] = x.select("div[@class='Discount_bg']/div/a/div[@class='toshiba']/img/@data-original").extract()
			tradusitem['discount'] = x.select("div[@class='Discount_bg']/div[@class='offDiv_20']/span[@style='top: 30px; position: relative;']/text()").extract()
			tradusitem['validity'] = x.select("div[@class='viewDiv']/div[@class='view_timeleft']/span/strong").extract()
			tradusitem['coupon'] = ''
			tradusitem['original_price'] = ''
			tradusitem['website'] = 'tradus'
			tradusitem['web_image'] = 'http://static.tradus.ibcdn.com/sites/all/themes/basic/images/ci_images/tradus_logo/tradus_new_logo.jpg'
			tradusitems.append(tradusitem)

		for x in indiatimes:
			indiatimesitem = SuperdealsItem()
			indiatimesitem['deal_name'] = x.select("div[@class='productdetail  ']/a/@title").extract()
			url = x.select("div[@class='productdetail  ']/a/@href").extract()
			appendurl = 'http://shopping.indiatimes.com'
			indiatimesitem['url'] = [appendurl + s for s in url]
			indiatimesitem['deal_price'] = x.select("div[@class='productdetail  ']/div[@class='view-attr']/div[@class='frt view-price']/div[@class='newprice' or 'newprice pricefont']/span[@class='price' or 'pricefont']/text()")[0].extract().strip('`').replace(",","")
			original_price = x.select("div[@class='productdetail  ']/div[@class='view-attr']/div[@class='frt view-price']/div[@class='oldprice']/span[@class='price pricefont']/text()").extract()
			indiatimesitem['original_price'] = [s.split('`')[1].replace(",","") for s in original_price]
			indiatimesitem['image'] = x.select("div[@class='productthumb']/a/img/@data-original").extract()
			discount = x.select("div[@class='productdetail']/div[@class='view-attr']/div[@class='frt view-price']/span[@class='getoff']/b/text()").extract()
			indiatimesitem['discount'] = [s+' %'+' off' for s in discount]
			indiatimesitem['coupon'] = ''
			indiatimesitem['validity'] = ''
			indiatimesitem['website'] = 'indiatimes'
			indiatimesitem['web_image'] = ''
			indiatimesitems.append(indiatimesitem)
		return items + flipitems + infyitems + tradusitems + indiatimesitems