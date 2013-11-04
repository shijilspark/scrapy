# Scrapy settings for superdeals project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'superdeals'

SPIDER_MODULES = ['superdeals.spiders']
NEWSPIDER_MODULE = 'superdeals.spiders'

# DOWNLOADER_MIDDLEWARES = {
#     'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
#     'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': 500,
#     # 'superdeals.middlewares.ProxyMiddleware': 100,
#     'superdeals.middlewares.RetryChangeProxyMiddleware': 600,
# }



# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'superdeals (+http://www.yourdomain.com)'
