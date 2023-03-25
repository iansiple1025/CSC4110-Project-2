import json
#creates json file for the app
with open('AppData.json','r') as openfile:
                Database=json.load(openfile)
sale=[2]
logFiles=[]
Database={}
users={}
price={}

#inventory
Database["regular"]=0
Database["expresso"]=0 
Database["milk"]=0      
Database["suger"]=0
Database["cocoa"]=0
Database["creamer"]=0
Database["revenue"]=0
Database["cost"]=0

#current sales
Database["current"]=sale

Database["usernames"]=users
Database["logs"]=logFiles

#menu prices
price["regular"]=0
price["expresso"]=0 
price["latte"]=0      
price["cappa"]=0
price["cocoaLatte"]=0
Database["prices"]=price

#reads the file user requested
with open("AppData.json","w") as out:
    json.dump(Database,out)