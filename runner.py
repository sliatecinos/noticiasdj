import scrapy
from scrapy.crawler import CrawlerProcess

from noticiasdj.spiders.noticias_spider import NoticiasSpider

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'FEED_FORMAT': 'json',
    'FEED_URI': 'data.json'
})

process.crawl(NoticiasSpider)
process.start() # the script will block here until the crawling is finished
