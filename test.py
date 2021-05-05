from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests as request

file_test = open("saida.txt")


response = request.get('https://www.bcb.gov.br/estabilidadefinanceira/fechamentodolar')
soup = BeautifulSoup(response.text, 'html.parser')
print(soup)
for data in soup.findAll('tr'):
    print(data)




