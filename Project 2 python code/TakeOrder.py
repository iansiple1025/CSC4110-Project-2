from datetime import datetime
import json, os

main_path = os.path.join(os.path.dirname(os.path.realpath(__file__)))

class TakeOrders:
 def copyData():
         with open(os.path.join(main_path, os.path.join(main_path, "AppData.json")),'r') as openfile:
                OldData=json.load(openfile)
         with open(os.path.join(main_path, os.path.join(main_path, "CopyAppData.json")),'r') as openfile:
                newData=json.load(openfile)
                newData=OldData
            
         with open(os.path.join(main_path, "CopyAppData.json"),"w") as out:
              json.dump(newData,out)
         return 0
    
 def order(choice):
          total=[]
          with open(os.path.join(main_path, os.path.join(main_path, "CopyAppData.json")),'r') as openfile:
                Data=json.load(openfile)
          if choice==1:
                
                if Data["regular"]-10.6>=0 and Data['suger']-3>=0 and Data['creamer']-2>=0:
                      Data["regular"]-=0.38
                      Data['suger']-=3
                      Data['creamer']-=2
                      print(Data['current'][0])
                      Data['current'][0]+=Data['prices']['regular']
                      total.append(Data['prices']['regular'])
                      total.append(Data['current'][0])
                      Data['current'][1]+="regular "
                      with open(os.path.join(main_path, "CopyAppData.json"),"w") as out:
                         json.dump(Data,out)
                      return total
                      
                else:
                      return False
          elif choice==2:
                if Data["expresso"]-10.6>=0 and Data['suger']-3>=0 and Data['creamer']-2>=0:
                      Data["expresso"]-=0.38
                      Data['suger']-=3
                      Data['creamer']-=2
                      Data['current'][0]+=Data['prices']['expresso']
                      total.append(Data['prices']['expresso'])
                      total.append(Data['current'][0])
                      Data['current'][1]+="expresso "
                      with open(os.path.join(main_path, "CopyAppData.json"),"w") as out:
                         json.dump(Data,out)
                      return total
                      
                else:
                      return False
    
          elif choice==3:
                if Data["expresso"]-10.6>=0 and Data['suger']-2>=0 and Data['milk']-4>=0:
                      Data["expresso"]-=0.38
                      Data['suger']-=2
                      Data['milk']-=4
                      Data['current'][0]+=Data['prices']['latte']
                      total.append(Data['prices']['latte'])
                      total.append(Data['current'][0])
                      Data['current'][1]+="latte "
                      with open(os.path.join(main_path, "CopyAppData.json"),"w") as out:
                         json.dump(Data,out)
                      return total
                      
                else:
                      return False
          elif choice==4:
                
                if Data["expresso"]-10.6>=0 and Data['suger']-2>=0 and Data['milk']-2>=0:
                      Data["expresso"]-=0.38
                      Data['suger']-=2
                      Data['milk']-=2
                      Data['current'][0]+=Data['prices']['cappa']
                      total.append(Data['prices']['cappa'])
                      total.append(Data['current'][0])
                      Data['current'][1]+="cappa "
                      with open(os.path.join(main_path, "CopyAppData.json"),"w") as out:
                         json.dump(Data,out)
                      return total
                      
                else:
                      return False
          elif choice==5:
                
                if Data["expresso"]-10.6>=0 and Data['suger']-2>=0 and Data['milk']-2>=0 and Data['cocoa']-14.3>=0:
                      Data["expresso"]-=0.38
                      Data['suger']-=2
                      Data['milk']-=2
                      Data['cocoa']-=14.3
                      Data['current'][0]+=Data['prices']['cocoaLatte']
                      total.append(Data['prices']['cappa'])
                      Data['current'][1]+="cocoa latte "
                      total.append(Data['current'][0])
                      
                      with open(os.path.join(main_path, "CopyAppData.json"),"w") as out:
                         json.dump(Data,out)
                      return total
                      
                else:
                      return False
                
 def checkOut(user):
         time= datetime.now()
         time = time.strftime("%H:%M:%S")
         
         with open(os.path.join(main_path, os.path.join(main_path, "CopyAppData.json")),'r') as openfile:
                OldData=json.load(openfile)
         with open(os.path.join(main_path, os.path.join(main_path, "AppData.json")),'r') as openfile:
                NewData=json.load(openfile)
         NewData=OldData
         id=NewData['orderID']
         NewData['revenue']+=OldData['current'][0]
         #log
         log="Transaction #: "+str(NewData['orderID'])+", Employee: "+str(NewData['usernames'][user][0])+", order: "+str(OldData['current'][1])+ ", total= "+str(OldData['current'][0])+"$"+" at "+str(time)
         
         NewData['logs'][NewData['orderID']]=log
         
         NewData['orderID']+=1
         NewData['current'][0]=0
         NewData['current'][1]=""
         with open(os.path.join(main_path, "AppData.json"),"w") as out:
                        json.dump(NewData,out)
         return id


                  

    
        
        