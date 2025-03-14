# Biblioteca para fazer requisições HTTP 
import requests

# RASCUNHO DE POSSIVEIS STATUS CODE:
# 200 – OK (requisição bem-sucedida)
# 301/302 – Redirecionamento (o conteúdo foi movido para outra URL)
# 403 – Proibido (acesso negado)
# 404 – Não encontrado (a página não existe)
# 500 – Erro interno do servidor

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

