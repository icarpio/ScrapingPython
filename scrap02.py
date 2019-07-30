# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 08:46:14 2019

@author: Icarpio
"""
from bs4 import BeautifulSoup
import csv
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

http = urllib3.PoolManager()

i_list = range(1,1944,1)
web= http.request('GET','https://www.icfo.es/people/people_details?people_id=296')
soup = BeautifulSoup(web.data, "lxml")
name = soup.find_all('h4')
print(name[0].get_text())
position=soup.find_all(class_='position')
print(position[0].get_text())
phone=soup.find_all(class_='destacado')
print(phone[6].get_text())
