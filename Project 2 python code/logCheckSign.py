
from datetime import datetime
import json


class loginChecks:
    """logs user into the program or signs them up"""
    
              
    def checkLogin(username,password):
        """Checks to see if username and password match"""
        #current time
        username=username.lower()
        
        time= datetime.now()
        time = time.strftime("%H:%M:%S")
        
        
        
        with open('AppData.json','r') as openfile:
                data=json.load(openfile)
    
        
        if username in data["usernames"].keys() and password==data["usernames"][username][2]:
               #logs event
               data['logs'].append("User name "+username+" logged in "+"at: "+time)
               with open("AppData.json","w") as out:
                 json.dump(data,out)
               return True
        else:
              data['logs'].append("User name "+username+" failed to log in "+"at: "+time)
              with open("AppData.json","w") as out:
               json.dump(data,out)
              return False
    def sign(username,first,last,password):
         username=username.lower()
         """Signs up user"""
         time= datetime.now()
         #current time
         time= datetime.now()
         time = time.strftime("%H:%M:%S")
         #gets rid of spaces
         username=username.replace(" ","")
         last=last.replace(" ","")
         password.replace(" ","")
         check=0
         with open('AppData.json','r') as openfile:
                data=json.load(openfile)
         if username in data['usernames'].keys()or username=="":
            check=1
         elif first.isalpha()==False:
            check=2
            
         elif last.isalpha()==False:
            check=3    
         elif len(password)<6:
            check=4
         
         if check==0:
             
             arr=[]
             arr.append(first)
             arr.append(last)
             arr.append(password)
             data['usernames'][username]=arr
             #logs event
             data['logs'].append("User name "+username+" is registered "+"at: "+time)
             with open("AppData.json","w") as out:
              json.dump(data,out)

             return 0
         else:
             data['logs'].append("User name "+username+" failed to register "+"at: "+time)
             with open("AppData.json","w") as out:
              json.dump(data,out)
             return check
        
        

        
    

