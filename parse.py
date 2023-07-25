from time import sleep
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from db import DB
import config



class Parsing:
    
    def get_source(self):  #парсинг всей страницы
        try:
            service = Service(executable_path=ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service)
            driver.maximize_window()
            driver.get(config.URL)
    #Добавить переxод на некст страницы
            with open("temp.html","w",encoding="utf-8") as file:
                file.write(driver.page_source)  

        except Exception as e:
            print(e)
        finally:     
            driver.close()   
            driver.quit()
            self.get_items()

    def get_items(self): # вытаскивание обьявлений по названию класса 
        try:     
            with open("temp.html",encoding="utf-8") as file:
                src = file.read()

            soup = BeautifulSoup(src, "lxml")
            item_divs = soup.find_all("div", class_="iva-item-root-_lk9K photo-slider-slider-S15A_ iva-item-list-rfgcH iva-item-redesign-rop6P iva-item-responsive-_lbhG items-item-My3ih items-listItem-Gd1jN js-catalog-item-enum")
            db = DB()
            for item in item_divs:

                item_href = item.find("a",class_="iva-item-sliderLink-uLz1v").get("href")
                price = item.find("meta", itemprop="price").get("content")
                price_curr = item.find("meta", itemprop="priceCurrency").get("content")
                print(price,price_curr,item_href)
                dic = db.db_createCont(item_href,price,price_curr)
                db.db_insert(dic)
            db.db_closeConn()
        except Exception as e:
            print(e)

         
#x = Parsing()
#config.URL="https://www.avito.ru/kazan/avtomobili/audi-ASgBAgICAUTgtg3elyg?cd=1&radius=200&searchRadius=200"
#x.get_source()

