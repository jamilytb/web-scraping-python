# Biblioteca necessária para fazer requisições HTTP 
import requests

from bs4 import BeautifulSoup

# Fazendo uma requisição GET para a URL 
response = requests.get('https://www.neosolar.com.br/loja')

# Pegando o conteúdo da requisição
content = response.content

# Primeiro parametro é o conteúdo da requisição e o segundo é o parser (html.parser é o padrão do python)
site = BeautifulSoup(content, 'html.parser')

# Pegando o titulo da página (primeira opção)
products = site.find('strong', attrs={'class': 'product-item-name'})
print(products.text)    

# Pegando o titulo da página (segunda opção)
#products = site.find('strong', attrs={'class': 'product-item-name'}).a['title']
#print(products)  

