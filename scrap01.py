# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 08:15 2019

@author: Icarpio
""" 

from bs4 import BeautifulSoup
import csv
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

http = urllib3.PoolManager()

web = http.request('GET','https://elpais.com')
#Contiene la web en html
soup = BeautifulSoup(web.data, "lxml")
#Contiene el titulo de pagina
titulo = soup.title.text

print(soup)
print(titulo)

#Quitar etiquetas y escribir todas las url en un csv con todos los enlaces de la pagina
file = csv.writer(open("links.csv","w"))
file.writerow(["Names","LinkT"])

links = soup.find_all('a')

for link in links:
    lin = link.get('href')
    textos = link.get_text()
    file.writerow([textos,lin])
