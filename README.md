# Coleção de noticias do site DJ.ORG.BR
> Webscrapping dos dados da seção de notícias do site DJ, com uso de Python.

___Projeto pessoal___ 
**@author**: sliatecinos

## Instalação das dependências usadas no scrapping

Fazer a instalação via pip:
```bash
pip install scrapy
```

## Bloco de captura dos dados
```python
import scrapy 

# após a importação da lib
=======
# Função de recuperação dos dados (Html scrap, em "articles.py")
=======
def recupera_noticia(response):
    sitecontent = response.css('div.site-content')
    ast = sitecontent.css('div.ast-container')
    section = ast.css('section.elementor-section')
    titulo = section.css('h2.elementor-heading-title::text').get()
    noticias = section.css('div.elementor-widget-container')
    noticia = noticias[2].css('::text').getall()
    noticiafinal = ' '.join(noticia)
..    
    
```

## Estrutura do projeto
    .
    ├── data.json                 # JSON file to store crawled data
    ├── README.md
    ├── runner.py                 # Source files (alternatively `py`)
    ├── scrapy.cfg                # Scrapy config files                 
    └── noticiasdj                # Source files location
        ├── __pycache__              # Compiled files (alternatively `dist`)
        ├── articles.py              # Source files (alternatively `py`)
        ├── items.py                 # --Incompleted source-code (alternatively `py`)
        ├── middlewares.py           # Default Scrapy methods (alternatively `py`)
        ├── pipelines.py             # --Incompleted source-code (alternatively `py`)
        ├── settings.py              # Scrapy spider configs (alternatively `py`)
        └── spiders                  # Spider's location
            ├── __pycache__             # Compiled files (alternatively `dist`)
            ├── __init__.py             # Scrapy files (alternatively `py`)
            └── noticias_spider.py      # Source files (alternatively `py`)

## Links externos

Site de Scrapy: [dj](https://dj.org.br/)
Scrapy - official documentation: [DOCS](https://docs.scrapy.org/en/latest/index.html)
