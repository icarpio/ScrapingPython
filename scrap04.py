# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 10:01 2019

@author: Icarpio
@Scrap Weather
"""

from bs4 import BeautifulSoup
import pandas as pd
import requests


pagina = requests.get("https://www.eltiempo.es/alcazar-de-san-juan.html")
soup = BeautifulSoup(pagina.content, 'html.parser')
city=soup.find(id="cityTable")
week = city.find_all(class_="m_table_weather_day_temp_wrapper")

#Imprimimos por consola la primera linea de la tabla
day = week[3]
date = [day.attrs['popup_date']]
weather = [day.attrs['popup_forecast']]
wind=[day.attrs['popup_wind']]
rain=[day.attrs['popup_prob_rain']]
print('Tiempo en Alcazar City: ' , date, weather, wind, rain)

#Imprimimos con pandas toda la pagina

pagina = requests.get("https://www.eltiempo.es/madrid.html")
soup = BeautifulSoup(pagina.content, 'html.parser')
city=soup.find(id="cityTable")
week = city.find_all(class_="m_table_weather_day_temp_wrapper")
week = week[3:33]

date = [day.attrs['popup_date'] for day in week]
weather = [day.attrs['popup_forecast']for day in week]
wind=[day.attrs['popup_wind']for day in week]
rain=[day.attrs['popup_prob_rain']for day in week]

prediccion = pd.DataFrame({
        "Fecha": date,
        "Tiempo": weather,
        "Viento": wind,
        "LLuvia": rain})

print('El Tiempo en Madrid:\n',prediccion)

#Jupyter Notebook
#prediccion.head(30)







