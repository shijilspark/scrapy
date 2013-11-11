# Importing base64 library because we'll need it ONLY in case if the proxy we are going to use requires authentication
import base64
from random import choice
from scrapy.contrib.downloadermiddleware.retry import RetryMiddleware

 
# Start your middleware class
# class ProxyMiddleware(object):
#     # overwrite process request
#     def process_request(self, request, spider):
#         # Set the location of the proxy
#         proxylist = ['http://101.226.74.168:8081','http://110.80.37.18:8090','http://111.123.180.27:8090','http://114.113.156.33:8090','http://114.113.229.39:8000','http://114.255.7.186:80','http://115.238.253.85:8090','http://118.151.221.226:80','http://121.11.69.14:8090']
#         request.meta['proxy'] = choice(proxylist)
 
#         # Use the following lines if your proxy requires authentication
#         # proxy_user_pass = "USERNAME:PASSWORD"
#         # # setup basic authentication for the proxy
#         # encoded_user_pass = base64.encodestring(proxy_user_pass)
#         # request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass


class RetryChangeProxyMiddleware(RetryMiddleware):
    def _retry(self, request, reason, spider):
        log.msg('Changing-proxy')
        tn = telnetlib.Telnet('127.0.0.1', 9051)
        tn.read_until("Escape character is '^]'.", 2)
        tn.write('AUTHENTICATE "267765"\r\n')
        tn.read_until("250 OK", 2)
        tn.write("signal NEWNYM\r\n")
        tn.read_until("250 OK", 2)
        tn.write("quit\r\n")
        tn.close()
        time.sleep(3)
        log.msg('Proxychanged')
        return RetryMiddleware._retry(self, request, reason, spider)