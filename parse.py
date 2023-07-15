from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from pymongo import MongoClient


PAUSE_DURATION_SECONDS = 5



def get_source(url):  #парсинг всей страницы
    try:
        service = Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()
        driver.get(url)
        
        with open("text.html","w",encoding="utf-8") as file:
            file.write(driver.page_source)  
              
    except Exception as e:
        print(e)
    finally:     
        driver.close()   
        driver.quit()

def get_items(): # вытаскивание обьявлений по названию класса 
    try:     
        with open("text.html",encoding="utf-8") as file:
            src = file.read()
            
        soup = BeautifulSoup(src, "lxml")
        item_divs = soup.find_all("div", class_="iva-item-root-_lk9K photo-slider-slider-S15A_ iva-item-list-rfgcH iva-item-redesign-rop6P iva-item-responsive-_lbhG items-item-My3ih items-listItem-Gd1jN js-catalog-item-enum")
        
        for item in item_divs:
            
            item_href = item.find("a",class_="iva-item-sliderLink-uLz1v").get("href")
            #prices.append(price)
            #items.append(item)
            db_connect(str(item),str(item_href))
            #сделать проверку по href 
            #Возможно можно сделать items в виде словаря и не открывать соединение каждый раз 
                
    except Exception as e:
        print(e)
      
def db_connect(data,href):
    URI = "mongodb://localhost:27017"
    client = MongoClient(URI)
    db = client.parse_data
    coll = db.data
    if coll.find_one({"href_id":href}):
        print(f"{href} уже есть в бд")
    else:
        coll.insert_one({"href_id":href,"data": data})
    client.close() 
         


  
def main():
    get_source(url="https://www.avito.ru/kazan/avtomobili/audi-ASgBAgICAUTgtg3elyg?cd=1&radius=200&searchRadius=200")


if __name__ == '__main__':
    main()
    get_items()