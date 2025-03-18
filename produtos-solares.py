# - OBTENDO PRODUTOS SOLARES DA CONCORRENCIA PARTIR DE UMA BUSCA DO USUARIO

import requests
from bs4 import BeautifulSoup

url_base = 'https://www.energiatotal.com.br/painel-solar'

response = requests.get(url_base)
response.encoding = 'utf-8'

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div', attrs={'class': 'product nb show-down'})

for produto in produtos:

    titulo = produto.find('div', attrs={'class': 'product-name'})
    price = produto.find('div', attrs={'class': 'box-price'})
    link = produto.find('a', attrs={'class': 'info-product'})

    print('Nome do Produto:', titulo.text)
    print('Preço do Produto:', price.text)
    print('Link do Produto:', link['href'])

    print('\n\n')
