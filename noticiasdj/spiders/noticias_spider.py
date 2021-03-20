import scrapy
from ..articles import recupera_noticia


class NoticiasSpider(scrapy.Spider):
    name = "noticias"

    # def start_requests(self):
    start_urls = [
        'https://dj.org.br/categoria/noticias/',
    ]
        # for url in urls:
        #     yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        a_next = response.css('a.page-numbers.next')
        article = response.css('div.elementor-widget-container div.elementor-posts-container article.elementor-post')
        newslink = article.css('a.elementor-post__thumbnail__link::attr(href)')

        for link in newslink:
            next_page_url = link.get()
            nova_noticia = scrapy.Request(next_page_url)
            nova_noticia.callback = recupera_noticia
            yield nova_noticia

            # page = response.url.split("/")[-2]
            page = response.url
            filename = '[%s]' % page
            # with open(filename, 'wb') as f:
            #     f.write(response.body)
            self.log('Passing by address... %s' % filename)

        next_page_panel = a_next.css('a').attrib['href']
        if next_page_panel is not None:
            next_page_panel = response.urljoin(next_page_panel)
            yield scrapy.Request(next_page_panel, callback=self.parse)
        
    

