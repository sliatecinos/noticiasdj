<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a1b290a (Rebasing conflicts #2)
<<<<<<< HEAD
>>>>>>> 2e472c7 (Rebasing conflicts #7)
=======
>>>>>>> 084fa38 (Rebasing conflicts #10)
# Coleção de noticias do site DJ.ORG.BR
> Webscrapping dos dados da seção de notícias do site dj, com uso de Python.

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
<<<<<<< HEAD

# após a importação da lib
=======
# Função de recuperação dos dados (Html scrap, em "")
=======
<<<<<<< HEAD
# após a importação da lib

# Função de recuperação dos dados (Html scrap, em "")

=======

<<<<<<< HEAD
# após a importação da lib
=======
# Função de recuperação dos dados (Html scrap, em "")
>>>>>>> 5f78d2b (Publish release)
>>>>>>> 2e472c7 (Rebasing conflicts #7)
>>>>>>> 084fa38 (Rebasing conflicts #10)
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

<<<<<<< HEAD
    .
=======
<<<<<<< HEAD
=======
    .
    ├── ...             
    ├── .pytest_cache             # Compiled files (alternatively `dist`)
<<<<<<< HEAD
    ├── .vscode                   # Compiled files (alternatively `dist`)
    ├── README.md                  
    └── noticiasdj                            # Source files (alternatively `py`)
<<<<<<< HEAD
                 ├── __pycache__              # Compiled files (alternatively `dist`)
                 └── spiders                  # Runner "spider" location
                            └── __pycache__   # Compiled files (alternatively `dist`)
=======
>>>>>>> 2e472c7 (Rebasing conflicts #7)
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

<<<<<<< HEAD

=======
>>>>>>> c6d9946 (Publish release)
=======
        ├── __pycache__              # Compiled files (alternatively `dist`)
        └── spiders                  # Runner "spider" location
            └── __pycache__   # Compiled files (alternatively `dist`)
>>>>>>> 3015516 (Adicao de outputs do scrapping)

## Links externos

Site de Scrapy: [dj](https://dj.org.br/)

Scrapy - official documentation: [DOCS](https://docs.scrapy.org/en/latest/index.html)
>>>>>>> 34b1ec9 (Rebasing conflicts)
=======
## Coleção de noticias do site DJ.ORG.BR

**@author**: sliatecinos

___Projeto pessoal___
>>>>>>> edca78d (Update readme)
<<<<<<< HEAD
=======
# Coleção de noticias do site DJ.ORG.BR
> Webscrapping dos dados da seção de notícias do site dj, com uso de Python.

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
    ├── .pytest_cache             # Compiled files (alternatively `dist`)
    ├── .vscode                   # Compiled files (alternatively `dist`)
    ├── README.md                  
    └── noticiasdj                            # Source files (alternatively `py`)
                 ├── __pycache__              # Compiled files (alternatively `dist`)
                 └── spiders                  # Runner "spider" location
                            └── __pycache__   # Compiled files (alternatively `dist`)
>>>>>>> 2e472c7 (Rebasing conflicts #7)

## Links externos

Site de Scrapy: [dj](https://dj.org.br/)

Scrapy - official documentation: [DOCS](https://docs.scrapy.org/en/latest/index.html)
<<<<<<< HEAD

>>>>>>> 22bfc64 (Update readme)
=======
>>>>>>> e3cf535 (Update readme)
=======
# Coleção de noticias do site DJ.ORG.BR
> Webscrapping dos dados da seção de notícias do site dj, com uso de Python.

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

<<<<<<< HEAD
# após a importação da lib
=======
# Função de recuperação dos dados (Html scrap, em "")
>>>>>>> 5f78d2b (Publish release)
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
    ├── .pytest_cache             # Compiled files (alternatively `dist`)
<<<<<<< HEAD
    ├── .vscode                   # Compiled files (alternatively `dist`)
    ├── README.md                  
    └── noticiasdj                            # Source files (alternatively `py`)
                 ├── __pycache__              # Compiled files (alternatively `dist`)
                 └── spiders                  # Runner "spider" location
                            └── __pycache__   # Compiled files (alternatively `dist`)
=======
>>>>>>> 084fa38 (Rebasing conflicts #10)
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

<<<<<<< HEAD
=======
>>>>>>> c6d9946 (Publish release)
>>>>>>> 084fa38 (Rebasing conflicts #10)

## Links externos

Site de Scrapy: [dj](https://dj.org.br/)

Scrapy - official documentation: [DOCS](https://docs.scrapy.org/en/latest/index.html)
>>>>>>> 490770f (Rebasing)
>>>>>>> 8f7a03d (Rebasing conflicts #3)
=======
>>>>>>> a1b290a (Rebasing conflicts #2)
>>>>>>> 2e472c7 (Rebasing conflicts #7)
