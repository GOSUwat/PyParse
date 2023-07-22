from pymongo import MongoClient
#from bs4 import BeautifulSoup
class DB:
    
    def db_connect(self,u_id,s_url,href,data):
        URI = "mongodb://localhost:32768"
        try:
            
            dic = {
                "id_id":href,
                "s_url":s_url,
                "data": data
            }
            
            client = MongoClient(URI)
            db = client.avito_parse
            collection = db[f"{u_id}"]
            
                
            self.db_insert(collection,dic)
        except Exception as e:
            print(e)
        finally:  
            client.close() 

    def db_insert(self,coll,dic):
        if coll.find_one({"id_id":dic.get("id_id")}):
            print(f"{dic.get('id_id')} уже есть в бд")
        else:
            coll.insert_one(dic)
