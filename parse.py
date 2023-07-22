from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from pymongo import MongoClient
from db import DB


PAUSE_DURATION_SECONDS = 5



def get_source(u_id,url):  #парсинг всей страницы
    try:
        service = Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()
        driver.get(url)
#Добавить переxод на некст страницы
        with open("text.html","w",encoding="utf-8") as file:
            file.write(driver.page_source)  
              
    except Exception as e:
        print(e)
        driver.close()   
        driver.quit()
    finally:     
        driver.close()   
        driver.quit()
        get_items(u_id,url)

def get_items(u_id,URL): # вытаскивание обьявлений по названию класса 
    try:     
        with open("text.html",encoding="utf-8") as file:
            src = file.read()
            
        soup = BeautifulSoup(src, "lxml")
        item_divs = soup.find_all("div", class_="iva-item-root-_lk9K photo-slider-slider-S15A_ iva-item-list-rfgcH iva-item-redesign-rop6P iva-item-responsive-_lbhG items-item-My3ih items-listItem-Gd1jN js-catalog-item-enum")
        
        for item in item_divs:
            
            item_href = item.find("a",class_="iva-item-sliderLink-uLz1v").get("href")
            db = DB()
            db.db_connect(u_id,URL,str(item_href),str(item))
            #return str(item_href),str(item),len(item_divs)
                
    except Exception as e:
        print(e)
      

         


  
#def main():
#    get_source(url="https://www.avito.ru/kazan/avtomobili/audi-ASgBAgICAUTgtg3elyg?cd=1&radius=200&searchRadius=200")
#
#
#if __name__ == '__main__':
#    main()
#    get_items()