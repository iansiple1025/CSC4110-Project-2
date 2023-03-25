import json


class loginChecks:
    """logs user into the program or signs them up"""
    
              
    def checkLogin(username,password):
        with open('AppData.json','r') as openfile:
                data=json.load(openfile)
    
        
        if username in data["usernames"].keys() and password==data["usernames"][username][2]:
            
               return True
        else: 
              return False
    def sign(username,first,last,password):
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
         arr=[]
         arr.append(first)
         arr.append(last)
         arr.append(password)
         data['usernames'][username]=arr
         if check==0:
          
          with open("AppData.json","w") as out:
           json.dump(data,out)
           return 0
         else:
             return check
        
        

        
    

