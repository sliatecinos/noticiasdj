# -*- coding: latin1 -*-
<<<<<<< HEAD


def recupera_noticia(response):
    # meta tags infos
    postlink = response.xpath("//link[@rel='canonical']/@href")[0].extract()
    postdate = response.xpath("//meta[@property='article:published_time']/@content")[0].extract()
    postauthor = response.xpath("//meta[@property='article:author']/@content")[0].extract()
    postimg = response.xpath("//meta[@property='og:image']/@content")[0].extract()

    # html DIV tags infos
    main = response.css('main')
    wrap = main.css('div.elementor-section-wrap')
    section = wrap.css('section div div div div div section')
    widget = section.css('div.elementor-widget-wrap')

    titulo = widget.css('h2.elementor-heading-title::text').get()
    noticias = widget.xpath('//div[@data-widget_type="theme-post-content.default"]')
    noticia = noticias.css('::text').getall()
    noticiafinal = ' '.join(noticia)
=======
# import scrapy


def recupera_noticia(response):
    sitecontent = response.css('div.site-content')
    ast = sitecontent.css('div.ast-container')
    section = ast.css('section.elementor-section')
    titulo = section.css('h2.elementor-heading-title::text').get()
    noticias = section.css('div.elementor-widget-container')
    noticia = noticias[2].css('::text').getall()
    noticiafinal = ' '.join(noticia)
    # newsauthor = article.css('div.entry-meta span.meta-author span a::text').get()
    # newstext = article.css('p::text').getall()
    # newsmemo = '\n'.join(i for i in newstext)
>>>>>>> cae17dc (Commit init)

    #   #Give the extracted content row wise
    #   news = zip(newstitle, newsdate, newsauthor, newsmemo)
    #   for item in news:
    
    #create a dictionary to store the scraped info
    scraped_news = {
<<<<<<< HEAD
        'data' : postdate,
        'titulo' : titulo,
        'autor' : postauthor,
        'link' : postlink,
        'image' : postimg,
=======
        'titulo' : titulo,
        # 'data' : newsdate,
        # 'autor' : newsauthor,
>>>>>>> cae17dc (Commit init)
        'noticia' : noticiafinal,
    }

    #yield or give the scraped news to scrapy
    yield scraped_news
