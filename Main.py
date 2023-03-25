import tkinter as tk
import json
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from logCheckSign import loginChecks

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        #window creation
        self.title("Warrior Cafe")
        self.geometry("800x600")
        self.configure(bg="#EEEEE8")
        #logo
        self.logo=ImageTk.PhotoImage(Image.open("logo1.png").resize((500,180)))
        self.label0=Label(image=self.logo,background="#EEEEE8")
        self.label0.place(relx=0.5,rely=0.1,anchor=CENTER)

        #labels and buttons
        self.label2=ttk.Label(master=self,text='Copyright Datatree, 2023',font=("Themed Label", 10),
                              background="#EEEEE8")
        self.label3=ttk.Label(master=self,text='username',font=("Themed Label", 9),
                              background="#EEEEE8")
        self.label4=ttk.Label(master=self,text='password',font=("Themed Label", 9),
                              background="#EEEEE8")
        self.button1 = tk.Button(master=self,text="Log in", font="Helvetica",width="18",
                                 height="3",fg="white",bg="SpringGreen3",command=lambda: self.loginOrHub(1,self))
        self.button2 = tk.Button(master=self,text="Sign up", font="Helvetica",width="15",height="3",
                                 fg="white",bg="SpringGreen3",command= lambda:self.loginOrHub(2,self))
        self.button3 = tk.Button(master=self,text="Simulation mode",font="Helvetica",
                                 width="15",height="3",fg="white",bg="SpringGreen3")
        self.button4 = tk.Button(master=self,text="Exit",font="Helvetica",width="15",
                                 height="3",fg="white",bg="SpringGreen3",command=self.destroy)
        global entry1
        global entry2
        
        
        entry1=tk.Entry(master=self, width=34)
        entry2=tk.Entry(master=self, width=34,show="*")
        #display to screen
        self.label2.place(relx=0,rely=.98,anchor="w")
        self.label3.place(relx=0.5,rely=0.26,anchor=CENTER)
        self.label4.place(relx=0.5,rely=0.36,anchor=CENTER)
        self.button1.place(relx=0.5,rely=0.52,anchor=CENTER)
        self.button2.place(relx=0.2,rely=0.8,anchor=CENTER)
        self.button3.place(relx=0.5,rely=0.8,anchor=CENTER)
        self.button4.place(relx=0.8,rely=0.8,anchor=CENTER)
        entry1.place(relx=0.5,rely=0.3,anchor=CENTER)
        entry2.place(relx=0.5,rely=0.4,anchor=CENTER)
    def newWindow(self,main,choice):
          """"performs all the functions of the application"""
          global Win2
          Win2=tk.Toplevel(main)
          Win2.title("Warrior Cafe")
          Win2.geometry("800x600")
          Win2.configure(bg="#EEEEE8")
          Win1.destroy()
          if choice==1:
              print("order button was pressed")
          elif choice==2:
              print("re-stock button was pressed")
          elif choice==3:
              print("logs button was pressed")
          elif choice==4:
              print("Pricing button was pressed")
              
          
          
          
          
          
          
          button1 = tk.Button(master=Win2,text="BACK",font="Helvetica",
                                 width="10",height="1",fg="white",bg="SpringGreen3",
                                 command=lambda: self.close(2,main))
          button1.place(relx=0.5,rely=0.95,anchor=CENTER)
         
    def close(self,choice,main):
        if(choice==1):
          Win1.destroy()
        else:
            Win2.destroy()
            self.loginOrHub(1,main) 
       
    
    def loginOrHub(self, choice,MainWin):
       """choice==2 logs the user in the program or signs them up and
          choice==3 a is menu for the functionally of the App """
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
           username=entry1.get()
           password=entry2.get()
           #menu after login  
           if(loginChecks.checkLogin(username,password)):
            Win1=tk.Toplevel(MainWin)
            Win1.title("Warrior Cafe")
            Win1.geometry("800x600")
            Win1.configure(bg="#EEEEE8")
            self.logo1=ImageTk.PhotoImage(Image.open("logo1.png").resize((500,180)))
            label6=Label(master=Win1,image=self.logo1,background="#EEEEE8")
            label6.place(relx=0.5,rely=0.1,anchor=CENTER)
            #prints the users name 
            label7=tk.Label(master=Win1,text='WELCOME BACK '+(dataBase['usernames'][username][0]).upper(),font=("Helvetica", 14),
                        background="#EEEEE8")
            
            
            button2 = tk.Button(master=Win1,text="Order",font="Helvetica",
                                 width="15",height="2",fg="white",bg="SpringGreen3",command=lambda: self.newWindow(MainWin,1))
            button3= tk.Button(master=Win1,text="Re-stock",font="Helvetica",
                                 width="15",height="2",fg="white",bg="SpringGreen3",command=lambda: self.newWindow(MainWin,2))
            button4 = tk.Button(master=Win1,text="Logs &\n statistics",font="Helvetica",
                                 width="15",height="2",fg="white",bg="SpringGreen3",command=lambda: self.newWindow(MainWin,3))
            button5 = tk.Button(master=Win1,text="Set pries",font="Helvetica",
                                 width="15",height="2",fg="white",bg="SpringGreen3",command=lambda: self.newWindow(MainWin,4))
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
    
    