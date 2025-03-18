from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# abre o navegador
navegador = webdriver.Chrome()

# abre o site
navegador.get('https://www.energiatotal.com.br/')

sleep(3)

elemento = navegador.find_element(By.CLASS_NAME, 'input-search')

# escreve no input de busca 
elemento.send_keys('painel solar')
elemento.send_keys(Keys.RETURN)

sleep(1000)








