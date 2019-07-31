# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 10:29 2019

@author: Icarpio
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def go_to_web(cadena,city):
    driver = webdriver.Chrome('C:/Users/Yvan/Documents/Python Scripts/Drivers/chromedriver.exe')
    driver.get('https://www.paginas.amarillas.es/')
    data_list = []
    try:
        WebDriverWait(driver,5).until(EC.presence_of_all_elements_located((By.ID,"whatInput")))
        input_name = driver.find_element_by_id("whatInput")
        input_name.send_keys(cadena)
        input_where = driver.find_element_by_id("whereInput")
        input_where.send_keys(city)
        button = driver.find_element_by_id("submitBtn")
        button.click()
    except:
        print('El elemento no esta presente')
    try:
        WebDriverWait(driver,5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "listado-item")))
    except:
        print('Elementos no encontrados')
        
    results = driver.find_elements_by_class_name("listado-item")
    for res in results:
        try:
            data = res.find_element_by_class_name("box")
            print('datos=', data.text)
        except:
            data ='-'
            print('datos=0')
        print('------------------------------------------------')
    driver.close()
    return data_list

def main():
    what = input('Que estas buscando?')
    where = input('Donde lo estas buscando?')
    print(go_to_web(what,where))
    
main()

            
        