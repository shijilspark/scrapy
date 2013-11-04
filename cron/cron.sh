#!/bin/sh
PATH=$PATH:/usr/local/bin
export PATH


rm /home/ubuntu/superdeals/deals/scrapdeals/static/items.json

cd /home/ubuntu/superdeals/superdeals

scrapy crawl superdeal -o /home/ubuntu/superdeals/deals/scrapdeals/static/items.json -t json


