# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class SuperdealsItem(Item):
	"""
	simple container to collect scraped data
	"""
	deal_name = Field()
	# sub_name = Field()
	url = Field()
	# contents = Field()
	image = Field()
	deal_price = Field()
	original_price = Field()
	validity = Field()
	coupon = Field()
	discount = Field()
	website = Field()
	web_image = Field()