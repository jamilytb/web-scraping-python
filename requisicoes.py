# Biblioteca necessária para fazer requisições HTTP 
import requests

# Fazendo uma requisição GET para a URL 
response = requests.get('https://www.neosolar.com.br/loja')

# Exibindo o status code da requisição 
print('Status Code:', response.status_code)

# Exibindo os cabeçalhos da requisição 
print('↓↓ Headers ↓↓')
print(response.headers)

# Exibindo o conteúdo da requisição 
print('\n ↓↓ Content ↓↓')
print(response.content) 

