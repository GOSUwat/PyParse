from pymongo import MongoClient
import config
from time import sleep

#from bs4 import BeautifulSoup


class DB():
    
    def __init__(self):
        try:  
            self.client = MongoClient(config.HOST)
            self.db = self.client["Avito_Parsing"]       
        except Exception as e:
            print(e)
            
     
    @property         
    def get_db(self):
        return self.db
        
    def db_createCont(self,item_href,price,price_curr):  #может можно kwargs?
        self.collection = self.db[f"{config.U_ID}"]
        self.item_href = item_href
        self.price = price
        self.price_curr = price_curr 
        self.dic = {
            "s_url":config.URL,
            "item_url": f"https://www.avito.ru{self.item_href}",
            "price": self.price,
            "price_curr": self.price_curr
            
        }                      
        return self.dic
      
    def db_isNewUrl(self) -> bool:
        is_new = False
        try:          
            if not self.collection.find_one({"s_url":self.dic.get("s_url")}):
                is_new = True
                self.collection.delete_many({})
                print("Новая ссылка")
        except Exception as e:
            print(e)          
        return is_new
                      
    def db_insert(self,dic):      
        try: 
            if self.db_isNewUrl():
                self.collection.delete_many({})      
            if self.collection.find_one({"item_url":dic.get("item_url")}):
                print(f"{dic.get('item_url')} уже есть в бд у {config.U_ID}")
            else:    
                self.collection.insert_one(dic)
        except Exception as e:
            print(e)
    
    def db_closeConn(self):
        self.client.close()
        
class FindOptimal(DB):
    
    @property
    def get_db(self):
        self.x = DB()
        return self.x.get_db
    
    @property
    def get_users(self):
        users = self.get_db.list_collection_names()  
        users.sort()
        return users
    
    def get_sUrl(self,user):
        collection = self.get_db [user]
        s_url = collection.find_one({"price": {"$exists": True}}, sort=[("price", 1)])["s_url"]
        return s_url

    def find_min(self,user):      
        collection = self.get_db[user]
        price = collection.find_one({"price": {"$exists": True}}, sort=[("price", 1)])["price"]
        url = collection.find_one({"price": {"$exists": True}}, sort=[("price", 1)])["item_url"]
        price_curr = collection.find_one({"price": {"$exists": True}}, sort=[("price", 1)])["price_curr"]
        price_curr = collection.find_one({"price": {"$exists": True}}, sort=[("price", 1)])["price_curr"]
        self.x.db_closeConn()
        return price, url, price_curr
        

    
          
            