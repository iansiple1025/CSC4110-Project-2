import json, os

main_path = os.path.join(os.path.dirname(os.path.realpath(__file__)))

#creates json file for the app
with open(os.path.join(main_path, "AppData.json"),'r') as openfile:
   Database=json.load(openfile)

sale=[0,""]
logFiles={}
#logFiles=[]
hotsales=[0,0,0,0,0]
Database={}
users={}
price={}

#inventory
Database["orderID"]=10000
Database["regular"]=200
Database["expresso"]=200 
Database["milk"]=10      
Database["suger"]=100
Database["cocoa"]=200
Database["creamer"]=100

#cost and revenue
Database["revenue"]=10
Database["cost"]=0

#sale info
Database["current"]=sale
Database['hotSales']=hotsales
Database["usernames"]=users
Database["logs"]=logFiles

#menu prices
price["regular"]=2.25
price["expresso"]=2.50 
price["latte"]=3.45      
price["cappa"]=3.25
price["cocoaLatte"]=3.75
Database["prices"]=price


#reads the file user requested
with open(os.path.join(main_path, "CopyAppData.json"),"w") as out:
    json.dump(Database,out)
