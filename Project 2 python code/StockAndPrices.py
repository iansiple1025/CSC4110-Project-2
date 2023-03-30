import json
from datetime import datetime

class inventory:
   def reStock(reg,expr,milk,sugar,creamer,coca,username):
        
        cost=0
        time= datetime.now()
        time = time.strftime("%H:%M:%S, %m/%d/%Y")
        with open('AppData.json','r') as openfile:
            Database=json.load(openfile)
        regPrice=0.11; exprPrice=.14;milkPrice=4.36;sugarPrice=0.19; creamerPrice=0.08;cocaPrice=0.56
        if(reg!="" and reg.isdigit()):
            cost+=float(reg)*regPrice
            Database['regular']+=float(reg)
        if(expr!="" and expr.isdigit()):
            cost+=float(expr)*exprPrice
            Database['expresso']+=float(expr)
        if(milk!="" and milk.isdigit()):
            cost+=float(milk)*milkPrice
            Database['milk']+=float(milk)
        if(sugar!="" and sugar.isdigit()):
            cost+=float(sugar)*sugarPrice
            Database['sugar']+=int(sugar)
        if(creamer!="" and creamer.isdigit()):
            cost+=int(creamer)*creamerPrice
            Database['creamer']+=int(creamer)
        if(coca!="" and coca.isdigit()):
            cost+=float(coca)*cocaPrice
            Database['cocoa']+=float(coca)
        Database['cost']+=cost
        cost="{:.2f}".format(float(cost))
        log="Transaction #: "+str(Database['orderID'])+", Employee: "+str(Database['usernames'][username][0])\
         +", Re-stock completed total= "+str(cost)+"$"+" at "+str(time)
        
        Database['logs'][Database['orderID']]=log
        Database['orderID']+=1
        with open("AppData.json","w") as out:
            json.dump(Database,out)
        return cost
 
   def ViewInventory(choice):
       with open('AppData.json','r') as openfile:
            Database=json.load(openfile)
       
       if choice==0:
           reg="{:.2f}".format(Database["regular"])
           return "regular coffee: "+str(reg)+"(oz)"
       
       elif choice==1:
            expr="{:.2f}".format(Database["expresso"])
            return "expresso: "+str(expr)+"(oz)"
       elif choice==2:
            milk="{:.2f}".format(Database["milk"])
            return "1% milk: "+str(milk)+"(gal)"
       elif choice==3:
           sugar=Database["sugar"]
           return "sugar: "+str(sugar)+"(packets)"
       elif choice==4:
           cocoa="{:.2f}".format(Database["cocoa"])
           return "cocoa powder: "+str(cocoa)+"(oz)"
       elif choice==5:
           cream=Database["creamer"]
           return "Creamer: "+str(cream)+"(packets)"
       
   def ViewPrices(choice):
       with open('AppData.json','r') as openfile:
            Database=json.load(openfile)
       
       if choice==0:
           reg="{:.2f}".format(Database["prices"]['regular'])
           return "regular: "+str(reg)+"$"
       
       elif choice==1:
            expr="{:.2f}".format(Database["prices"]['expresso'])
            return "expresso: "+str(expr)+"$"
       elif choice==2:
            latte="{:.2f}".format(Database["prices"]['latte'])
            return "latte: "+str(latte)+"$"
       elif choice==3:
           cappa="{:.2f}".format(Database["prices"]['cappa'])
           return "cappuccino: "+str(cappa)+"$"
       elif choice==4:
           cocoa="{:.2f}".format(Database["prices"]['cocoaLatte'])
           return "cocoa latte: "+str(cocoa)+"$"
    
   def setPrice(reg,expr,latte,capa,cocoa,username):
        
        time= datetime.now()
        time = time = time.strftime("%H:%M:%S, %m/%d/%Y")
        with open('AppData.json','r') as openfile:
            Database=json.load(openfile)
        regPrice=0.11; exprPrice=.14;milkPrice=4.36;sugarPrice=0.19; creamerPrice=0.08;cocaPrice=0.56
        if(reg!="" and reg.isdigit()):
            Database["prices"]['regular']=float(reg)
        if(expr!="" and expr.isdigit()):
            Database["prices"]['expresso']=float(expr)
        if(latte!="" and latte.isdigit()):
            Database["prices"]['latte']=float(latte)
        if(capa!="" and capa.isdigit()):
            Database["prices"]['cappa']=float(capa)
            
        if(cocoa!="" and cocoa.isdigit()):
            Database["prices"]['cocoaLatte']=float(cocoa)
        
            
        log="Transaction #: "+str(Database['orderID'])+", Employee: "+str(Database['usernames'][username][0])\
         +", re-pricing completed at "+str(time)
        Database['logs'][Database['orderID']]=log
        Database['orderID']+=1
        with open("AppData.json","w") as out:
            json.dump(Database,out)
    

        
   def viewStats(choice):
            drinks=["regular","expresso","latte","cappuccino","cocoa latte"]
            with open('AppData.json','r') as openfile:
             Database=json.load(openfile)
            rev="{:.2f}".format(float(Database['revenue']))
            cost="{:.2f}".format(float(Database['cost']))
            gross="{:.2f}".format(float(rev)-float(cost))
            margin="{:.2f}".format(float(gross)/float(rev)*100)

            #hot seller
            hotSeller=max(Database["hotSeller"])
            index=Database["hotSeller"].index(hotSeller)
            
            if choice==0:
                return "Hot Seller: "+str(drinks[index])
            elif choice==1:  
                return "Renvenue: "+str(rev)+"$"
            
            elif choice==2:       
                    return "Cost: "+str(cost)+"$"
            elif choice==3:
                    return "Gross Profit: "+str(gross)+"$"
            elif choice==4:
                    return "Gross Margin: "+str(margin)+"%"
                

       
      
       
        
