# -*- coding: latin1 -*-


def recupera_noticia(response):
    sitecontent = response.css('div.site-content')
    ast = sitecontent.css('div.ast-container')
    section = ast.css('section.elementor-section')
    titulo = section.css('h2.elementor-heading-title::text').get()
    noticias = section.css('div.elementor-widget-container')
    noticia = noticias[2].css('::text').getall()
    noticiafinal = ' '.join(noticia)

    #   #Give the extracted content row wise
    #   news = zip(newstitle, newsdate, newsauthor, newsmemo)
    #   for item in news:
    
    #create a dictionary to store the scraped info
    scraped_news = {
        'titulo' : titulo,
        # 'data' : newsdate,
        # 'autor' : newsauthor,
        'noticia' : noticiafinal,
    }

    #yield or give the scraped news to scrapy
    yield scraped_news
