# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 09:03:00 2019

@author: Icarpio
"""

""
from bs4 import BeautifulSoup
import csv
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

file= csv.writer(open("people.csv","w"))
file.writerow(["Nombre","Posicion"])


http = urllib3.PoolManager()
lista= range(1, 50,1)

for i in lista:
    web = http.request('GET','https://www.icfo.es/people/people_details?people_id=' + str(i))
    soup = BeautifulSoup(web.data,"lxml")
    name= soup.find_all('h4')
    print(str(i)+'-------------------')
    if len(name) > 0:
        name = soup.find_all('h4')
        namefile = name[0].get_text()
        pos=soup.find_all(class_='position')
        posfile=pos[0].get_text()
        file.writerow([namefile,posfile])
    else:
        print('url vacia')