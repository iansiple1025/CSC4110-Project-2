import tkinter as tk
import json
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from logCheckSign import loginChecks
from TakeOrder import TakeOrders
from StockAndPrices import inventory

class App(tk.Tk):
    def __init__(self):
        """Main window"""
        super().__init__()
        
        totalLabel=Label(self)
        #window creation
        self.title("Warrior Cafe")
        self.geometry("800x600")
        self.configure(bg="#EEEEE8")
        #logo
        self.logo=ImageTk.PhotoImage(Image.open("logo1.png").resize((500,180)))
        self.label0=Label(image=self.logo,background="#EEEEE8")
        self.label0.place(relx=0.5,rely=0.1,anchor=CENTER)
        global entry1
        global entry2
        #labels and buttons
        self.label2=ttk.Label(master=self,text='Copyright Datatree, 2023',font=("Themed Label", 10),
                    background="#EEEEE8").place(relx=0,rely=.98,anchor="w")
        self.label3=ttk.Label(master=self,text='username',font=("Themed Label", 9),
                    background="#EEEEE8").place(relx=0.5,rely=0.26,anchor=CENTER)
        self.label4=ttk.Label(master=self,text='password',font=("Themed Label", 9),
                    background="#EEEEE8").place(relx=0.5,rely=0.36,anchor=CENTER)
        self.button1 = tk.Button(master=self,text="Log in", font="Helvetica",width="18",height="3",fg="white",bg="SpringGreen3",
        command=lambda: self.loginOrHub(1,self,1)).place(relx=0.5,rely=0.52,anchor=CENTER)
        self.button2 = tk.Button(master=self,text="Sign up", font="Helvetica",width="15",height="3",fg="white",
         bg="SpringGreen3",command= lambda:self.loginOrHub(2,self,1)).place(relx=0.2,rely=0.8,anchor=CENTER)
        self.button3 = tk.Button(master=self,text="Simulation mode",font="Helvetica",
            width="15",height="3",fg="white",bg="SpringGreen3").place(relx=0.5,rely=0.8,anchor=CENTER)
        self.button4 = tk.Button(master=self,text="Exit",font="Helvetica",width="15",height="3",fg="white",
        bg="SpringGreen3",command=self.destroy).place(relx=0.8,rely=0.8,anchor=CENTER) 
        entry1=tk.Entry(master=self, width=34)
        entry2=tk.Entry(master=self, width=34,show="*")
        entry1.place(relx=0.5,rely=0.3,anchor=CENTER)
        entry2.place(relx=0.5,rely=0.4,anchor=CENTER)

    def addItems(self,choice):
            
            str=""
            total=""
            drinks=["Regular","Expresso","Latte","Cappuccino","Cocoa latte"]
            x=TakeOrders.order(choice)
            
            if x==False:
                messagebox.showwarning(parent=Win2,message="Not enough ingredients to make "+drinks[choice-1])
            else:
                str="{:.2f}".format(x[0])
                total="{:.2f}".format(x[1])
                
                totalLabel=Label(master=Win2,text=total+"$",font=("Helvetica", 20),background="#EEEEE8")
                totalLabel.place(relx=0.78,rely=0.73,anchor=CENTER)
                list1.insert(END,drinks[choice-1]+": "+str)
            

                
    def checkOut(self,main):
        """Checks out users asks the if they are sure and processes if they click yes"""
        ch=messagebox.askquestion("Checkout","Are your sure you want to checkout",parent=Win2)
        if ch=='yes':
            id=TakeOrders.checkOut(username1)
            messagebox.showinfo(parent=Win2,message="Transaction complete oderID: "+str(id))
            self.close(2,main)
            self.newWindow(main,1,TakeOrders.copyData())
            
                      
                
    def newWindow(self,main,choice,copy):
          """"performs all the functions of the application"""
          global Win2
          
          Win2=tk.Toplevel(main)
          
          Win2.title("Warrior Cafe")
          Win2.geometry("800x600")
          Win2.configure(bg="#EEEEE8")
          Win1.destroy()
          
          #order button
          if choice==1:
              

              #listbox with scroll bar
              scroll=Scrollbar(Win2)
              
              scroll.pack(side="right",fill="y")
              global list1
              list1=Listbox(Win2,yscrollcommand=scroll.set,width=38,height=20,font=("Helvetica", 10))
              list1.place(relx=0.8,rely=0.4,anchor=CENTER)
              scroll.config(command=list1.yview)
        
              #labels
              label1=tk.Label(master=Win2,text='Menu Items',font=("Helvetica", 20),
                              background="#EEEEE8")
              label1.place(relx=0.3,rely=0.13,anchor=CENTER)
              
              label2=tk.Label(master=Win2,text='Total: ',font=("Helvetica", 20),
                              background="#EEEEE8")
              label2.place(relx=0.68,rely=0.73,anchor=CENTER)
              #checkout button
              button6 = tk.Button(master=Win2,text="checkout",font="Helvetica",width="15",
                                 height="2",fg="white",bg="SpringGreen3",command=lambda: self.checkOut(main))
              button6.place(relx=0.8,rely=0.85,anchor=CENTER)

              #creates image buttons
              self.image1=ImageTk.PhotoImage(Image.open("reg.jpg").resize((100,100)))
              button1=Button(master=Win2,image=self.image1,command=lambda:self.addItems(1))
              button1.place(relx=0.2,rely=0.31,anchor=CENTER)
              self.image2=ImageTk.PhotoImage(Image.open("expresso.jpg").resize((100,100)))
              button2=Button(master=Win2,image=self.image2,command=lambda:self.addItems(2))
              button2.place(relx=0.4,rely=0.31,anchor=CENTER)
              self.image3=ImageTk.PhotoImage(Image.open("latte.jpg").resize((100,100)))
              button3=Button(master=Win2,image=self.image3,command=lambda:self.addItems(3))
              button3.place(relx=0.2,rely=0.56,anchor=CENTER)
              self.image4=ImageTk.PhotoImage(Image.open("cappa.jpg").resize((100,100)))
              button4=Button(master=Win2,image=self.image4,command=lambda:self.addItems(4))
              button4.place(relx=0.4,rely=0.56,anchor=CENTER)
              self.image5=ImageTk.PhotoImage(Image.open("cocoa.jpg").resize((100,100)))
              button5=Button(master=Win2,image=self.image5,command=lambda:self.addItems(5))
              button5.place(relx=0.3,rely=0.81,anchor=CENTER)
              
              print("order button was pressed")
          #re-stock and set PRices function
          elif choice==2 or choice==3:
               #array used for  labels
               if choice==2:
                    namesList=['Current Inventory:','Choose Items to re-stock:','regular coffee beans(oz):'
                          ,'expresso coffee beans(oz)','1% milk(gal):','suger(packet):','non dairy creamer(packet):'
                          ,'cocoa power(oz):']  
               else:
                           namesList=['Current Prices:','Set Prices:','Regular:','Expresso:        '
                          ,'Latte:','Cappuccino:','Cocoa Latte:']      
               #all listbox and lables           
               global list2
               list2=Listbox(Win2,width=28,height=6,font=("Helvetica", 12))
               list2.place(relx=0.8,rely=0.158,anchor=CENTER)
               label1=ttk.Label(master=Win2,text=namesList[0],font=("Themed Label", 20),
                              background="#EEEEE8")
               label1.place(relx=.77,rely=0.03,anchor=CENTER)
               label2=ttk.Label(master=Win2,text=namesList[1],font=("Themed Label", 20),
                              background="#EEEEE8")
               label2.grid(row=1,column=0,sticky=W,pady=4)
               label0=ttk.Label(master=Win2,text=namesList[2],font=("Themed Label", 12),
                              background="#EEEEE8")
               label0.grid(row=2,column=0,sticky=W,pady=4)
               label5=ttk.Label(master=Win2,text=namesList[3],font=("Themed Label", 12),
                              background="#EEEEE8")
               label5.grid(row=3,column=0,sticky=W,pady=4)
               label6=ttk.Label(master=Win2,text=namesList[4],font=("Themed Label", 12),
                              background="#EEEEE8")
               label6.grid(row=4,column=0,sticky=W,pady=4)
               label7=ttk.Label(master=Win2,text=namesList[5],font=("Themed Label", 12),
                              background="#EEEEE8")
               label7.grid(row=5,column=0,sticky=W,pady=4)
               label8=ttk.Label(master=Win2,text=namesList[6],font=("Themed Label", 12),
                              background="#EEEEE8")
               label8.grid(row=6,column=0,sticky=W,pady=4)
               #if statment that performs tasks based the pressed is re-stock or re-price
               if choice==2:
                   label9=ttk.Label(master=Win2,text='cocoa power(oz):',font=("Themed Label", 12),
                              background="#EEEEE8")
                   label9.grid(row=7,column=0,sticky=W,pady=4)
                   cocoaEntry=tk.Entry(master=Win2, width=10)
                   cocoaEntry.grid(row=7,column=1,sticky=W,pady=4)
                   addButton = tk.Button(master=Win2,text="ADD",font="Helvetica",width="10",
                                  height="1",fg="white",bg="SpringGreen3",command=lambda: self.addToInventory(main,regEntry.get(),expressoEntry.get(),
                                     milkEntry.get(),sugarEntry.get(),creamEntry.get(),cocoaEntry.get()))
                   addButton.grid(row=8,column=0,sticky=W,pady=4)
                   for i in range(6):
                    list2.insert(END,inventory.ViewInventory(i))
               else:
                   PriceButton = tk.Button(master=Win2,text="SET",font="Helvetica",width="10",
                                  height="1",fg="white",bg="SpringGreen3",command=lambda: self.setPrice(main,regEntry.get(),expressoEntry.get(),
                                     milkEntry.get(),sugarEntry.get(),creamEntry.get()))
                   PriceButton.grid(row=8,column=0,sticky=W,pady=4)
                   for i in range(5):
                    list2.insert(END,inventory.ViewPrices(i))
                   
                    
               
               #entries
               regEntry=tk.Entry(master=Win2, width=10)
               regEntry.grid(row=2,column=1,sticky=W,pady=4)
               expressoEntry=tk.Entry(master=Win2, width=10)
               expressoEntry.grid(row=3,column=1,sticky=W,pady=4)
               milkEntry=tk.Entry(master=Win2, width=10)
               milkEntry.grid(row=4,column=1,sticky=W,pady=4)
               sugarEntry=tk.Entry(master=Win2, width=10)
               sugarEntry.grid(row=5,column=1,sticky=W,pady=4)
               creamEntry=tk.Entry(master=Win2, width=10)
               creamEntry.grid(row=6,column=1,sticky=W,pady=4)
               
               print("re-stock button was pressed")
          elif choice==4:
              global list3
              #log and Statistics button
              frame=tk.Frame(Win2)
              frame.place(relx=0.5,rely=0.23,anchor=CENTER)
              label1=tk.Label(master=Win2,text="LOGS:\n(An empty search returns all logs)",font=("Helvetica", 12),
                              background="#EEEEE8")
              label1.place(relx=.5,rely=0.035,anchor=CENTER)
              list3=Listbox(frame,width=100,
                            height=10,font=("Helvetica", 10))
              list3.pack(side="left",fill="y")
              scroll2=Scrollbar(frame,orient='vertical') 
              scroll2.pack(side="right",fill="y")
              list3.config(yscrollcommand=scroll2.set)
              label2=tk.Label(master=Win2,text="STATISTICS:",font=("Helvetica", 12),
                              background="#EEEEE8")
              label2.place(relx=.5,rely=0.61,anchor=CENTER)
              list4=Listbox(Win2,width=35,
                            height=5,font=("Helvetica", 10))
              list4.place(relx=.5,rely=0.7,anchor=CENTER)
              searchEntry=tk.Entry(master=Win2, width=35,font=("Helvetica", 9))
              searchEntry.place(relx=0.5,rely=0.39,anchor=CENTER)
              searchButton = tk.Button(master=Win2,text="Search Logs",font="Helvetica",width="10"
                    ,fg="white",bg="SpringGreen3",command=lambda: self.logSearch(searchEntry.get()))
              searchButton.place(relx=0.5,rely=0.45,anchor=CENTER)
              #add logs to list box
              with open('AppData.json','r') as openfile:
                 Database=json.load(openfile)
              for i in Database['logs']:
                    list3.insert(END,Database['logs'][i])
              for i in range(5):
                    list4.insert(END,inventory.viewStats(i))


          

          #goes back to previous screen
          button1 = tk.Button(master=Win2,text="BACK",font="Helvetica",
                                 width="10",height="1",fg="white",bg="SpringGreen3",
                                 command=lambda: self.close(2,main))
          button1.place(relx=0.5,rely=0.95,anchor=CENTER)
    def logSearch(self,search):
        """displays search results"""
        x=False
        list3.delete(0,END)
        with open('AppData.json','r') as openfile:
                 Database=json.load(openfile)
        for i in Database['logs']:
                
                if search.lower() in Database['logs'][i].lower():
                    x=True
                    list3.insert(END,Database['logs'][i])
        if x==False:
            messagebox.showwarning(parent=Win2,message="Search failed.\nCould not find a match for: "+str(search))





    def addToInventory(self,main,reg,expr,milk,sugar,cream,cocoa):
        """Add button: ingredients to inventory and displays the updated inventory """
        ch=messagebox.askquestion("Inventory","Are your sure you want to add these items\n to the inventory",parent=Win2)
        
        if ch=='yes':
            cost=inventory.reStock(reg,expr,milk,
                                     sugar,cream,cocoa,username1)
            
            cost="{:.2f}".format(float(cost))
            messagebox.showinfo(parent=Win2,message="Transaction complete. Total= "+ cost+"$")
            self.close(2,main)
            self.newWindow(main,2,0)
    def setPrice(self,main,reg,expr,latte,capa,cocoa):
        """Set menu prices after add button is pressed"""
        ch=messagebox.askquestion("Inventory","Are you sure you want to add these items\n to the inventory",parent=Win2)
        
        if ch=='yes':
            inventory.setPrice(reg,expr,latte,capa,cocoa,username1)
            messagebox.showinfo(parent=Win2,message="Transaction complete")
            self.close(2,main)
            self.newWindow(main,3,0)

    def close(self,choice,main):
        """Closes certain windows"""
        if(choice==1):
          Win1.destroy()

        else:
            Win2.destroy()
            self.loginOrHub(1,main,2) 
       
    
    def loginOrHub(self, choice,MainWin,log):
       """choice==2 logs the user in the program or signs them up and
          choice==1 a is menu for the functionally of the App """
       #sizes window depending on the button pressed
       
       global Win1
       
       global dataBase
       #opens dataBase
       with open('AppData.json','r') as openfile:
                read=json.load(openfile)
       dataBase=read
       if(choice==2):
          #creates window
          Win1=tk.Toplevel(MainWin)
          Win1.title("Warrior Cafe")
          Win1.geometry("400x600")
          Win1.configure(bg="#EEEEE8")
          label1=tk.Label(master=Win1,text='Sign Up',font=("Helvetica", 20),
                            background="#EEEEE8")
          #opens new window when sign up button is pressed
         
          label0=tk.Label(master=Win1,text='Passwords most be greater than six characters,\n and first and last names must only have alphabet characters.',
                          font=("Helvetica", 9),background="#EEEEE8")
          userEntry=tk.Entry(master=Win1, width=34)
          firstEntry=tk.Entry(master=Win1, width=34)
          lastEntry=tk.Entry(master=Win1, width=34)
          passEntry=tk.Entry(master=Win1, width=34,show="*")
          label2=ttk.Label(master=Win1,text='User Name',font=("Themed Label", 9),
                              background="#EEEEE8")
          label3=ttk.Label(master=Win1,text='First Name',font=("Themed Label", 9),
                              background="#EEEEE8")
          label4=ttk.Label(master=Win1,text='Last Name',font=("Themed Label", 9),
                              background="#EEEEE8")
          label5=ttk.Label(master=Win1,text='Password',font=("Themed Label", 9),
                              background="#EEEEE8")
          button1 = tk.Button(master=Win1,text="Register",font="Helvetica",width="10",
                                 height="2",fg="white",bg="SpringGreen3",command=lambda: self.register(userEntry.get(),
                                 firstEntry.get(),lastEntry.get(),passEntry.get()))
          
          firstEntry.get()
          #place entries and label to screen
          label0.place(relx=0.5,rely=0.17,anchor=CENTER)
          label1.place(relx=0.5,rely=0.1,anchor=CENTER)
          label2.place(relx=0.5,rely=0.265,anchor=CENTER)
          label3.place(relx=0.5,rely=0.365,anchor=CENTER)
          label4.place(relx=0.5,rely=0.465,anchor=CENTER)
          label5.place(relx=0.5,rely=0.565,anchor=CENTER)
          userEntry.place(relx=0.5,rely=0.3,anchor=CENTER)
          firstEntry.place(relx=0.5,rely=0.4,anchor=CENTER)
          lastEntry.place(relx=0.5,rely=0.5,anchor=CENTER)
          passEntry.place(relx=0.5,rely=0.6,anchor=CENTER)
          button1.place(relx=0.5,rely=0.7,anchor=CENTER)
          
       elif choice==1:
           #logs ins in user
           global username1
           username1=entry1.get()
           
           password=entry2.get()
           #menu after login  
           if(loginChecks.checkLogin(username1,password,log)):
            Win1=tk.Toplevel(MainWin)
            Win1.title("Warrior Cafe")
            Win1.geometry("800x600")
            Win1.configure(bg="#EEEEE8")
            self.logo1=ImageTk.PhotoImage(Image.open("logo1.png").resize((500,180)))
            label6=Label(master=Win1,image=self.logo1,background="#EEEEE8")
            label6.place(relx=0.5,rely=0.1,anchor=CENTER)
            #prints the users name 
            label7=tk.Label(master=Win1,text='WELCOME BACK '+(dataBase['usernames'][username1.lower()][0]).upper(),font=("Helvetica", 14),
                        background="#EEEEE8")
            
            #Sub menu
            button2 = tk.Button(master=Win1,text="Order",font="Helvetica",
                                 width="15",height="2",fg="white",bg="SpringGreen3",command=lambda: self.newWindow(MainWin,1,TakeOrders.copyData()))
            button3= tk.Button(master=Win1,text="Re-stock",font="Helvetica",
                                 width="15",height="2",fg="white",bg="SpringGreen3",command=lambda: self.newWindow(MainWin,2,0))
            button4 = tk.Button(master=Win1,text="Logs &\n Statistics",font="Helvetica",
                                 width="15",height="2",fg="white",bg="SpringGreen3",command=lambda: self.newWindow(MainWin,4,0))
            button5 = tk.Button(master=Win1,text="Set Prices",font="Helvetica",
                                 width="15",height="2",fg="white",bg="SpringGreen3",command=lambda: self.newWindow(MainWin,3,0))
            button6 = tk.Button(master=Win1,text="Log out",font="Helvetica",
                                 width="10",height="1",fg="white",bg="SpringGreen3",command=lambda: self.close(1,MainWin))
            button2.place(relx=0.35,rely=0.5,anchor=CENTER)
            button3.place(relx=0.65,rely=0.5,anchor=CENTER)
            button4.place(relx=0.35,rely=0.7,anchor=CENTER)
            button5.place(relx=0.65,rely=0.7,anchor=CENTER)
            button6.place(relx=0.5,rely=0.96,anchor=CENTER)
            label7.place(relx=0.5,rely=0.3,anchor=CENTER)
           
              
           else:
               messagebox.showerror(message="invalid username or Password")
               
    def register(self,user,first,last,password):
        """Register button: registers user or prints error message"""
        message=["This username is already taken",
                 "First name Error. Must be alphabets only",
                 "Last name Error. Must be alphabets only","password must be alleast six characters"]
        x=loginChecks.sign(user,first,last,password)
        if(x==0):
            messagebox.showinfo(parent=Win1,message=user+" is registered")
            Win1.destroy()
        else:
            messagebox.showerror(parent=Win1,message=message[x-1])

if __name__ == "__main__":
    app = App()
    app.mainloop()
    
    