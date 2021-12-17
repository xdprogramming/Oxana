import requests
from bs4 import BeautifulSoup
import pyttsx3
import os

def get_news():
    try:
        
        url = "https://elpais.com/ultimas-noticias/"
        req = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(req.content, 'html.parser')
        content = soup.find_all("h2",class_="c_t")
        print("Las noticias del día en EL PAIS son las siguientes:\n")
        for i in content:
            print(i.text)
        print()    
        url = "https://elmundo.es"
        req = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(req.content, 'html.parser')
        content = soup.find_all("h2",class_="ue-c-cover-content__headline")
        print("Las noticias del día en EL MUNDO son las siguientes:\n")
        for i in content:
            print(i.text)
        print()
        
    except:
        print("SIMLE ALWAYS")

get_news()