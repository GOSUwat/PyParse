from pymongo import MongoClient
from bs4 import BeautifulSoup
class DB:
    
    def db_connect(self,data,href,uri = "mongodb://localhost:32768"):
        URI = uri
        try:
            
            client = MongoClient(URI)
            db = client.parse_data
            coll = db.data
            self.db_insert(coll,href,data)
        except Exception as e:
            print(e)
        finally:  
            client.close() 

    def db_insert(self,coll,href,data):
        if coll.find_one({"href_id":href}):
            print(f"{href} уже есть в бд")
        else:
            coll.insert_one({"href_id":href,"data": data})
