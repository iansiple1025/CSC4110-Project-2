import tkinter as tk
import json, customtkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from logCheckSign import loginChecks
from TakeOrder import TakeOrders
from StockAndPrices import inventory

class App(customtkinter.CTk):
    WIDTH = 1000
    HEIGHT = 700
    DARK_COLOR = '#90ee90'
    LIGHT_COLOR = '#233923'
    BG_COLOR = '#EEEEE8'
    def __init__(self):
        """Main window"""
        super().__init__()
        
        totalLabel=Label(self)
        #window creation
        self.title("Warrior Cafe")
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.resizable(1,1)


        '''
        ============= LOAD IMAGES =============
        '''
        self.logo_image = customtkinter.CTkImage(Image.open("logo1.png"), size=(500,150))
        self.home_image = customtkinter.CTkImage(light_image=Image.open("home_light.png"),
                                                 dark_image=Image.open("home_dark.png"),
                                                 size=(40, 40))
        self.simulation_image = customtkinter.CTkImage(light_image=Image.open("simulation_light.png"),
                                                 dark_image=Image.open("simulation_dark.png"),
                                                 size=(40, 40))
        self.setting_image = customtkinter.CTkImage(light_image=Image.open("setting_light.png"),
                                                 dark_image=Image.open("setting_dark.png"),
                                                 size=(40, 40))
        self.bg_image = customtkinter.CTkImage(light_image=Image.open("setting_light.png"),
                                                 dark_image=Image.open("setting_dark.png"),
                                                 size=(40, 40))
        
        
        '''
        ============= CREATE MAIN FRAMES =============
        '''

        # create login frame
        self.login_frame = customtkinter.CTkFrame(self, 
                                                  corner_radius=0)
        self.login_frame.grid(row = 0, column = 0, sticky='news')
        
        # create logo frame
        self.logo_frame = customtkinter.CTkFrame(self.login_frame,
                                                 corner_radius=0,
                                                 height=180,
                                                 fg_color='#858585')
        self.logo_frame.grid(row = 0, column = 0, columnspan=2, sticky='news')

        # create nav frame
        self.nav_frame = customtkinter.CTkFrame(self.login_frame,  
                                                corner_radius=0,
                                                fg_color=("#c9c9c9","#212121"),
                                                width=200)
        self.nav_frame.grid(row=1, column=0, sticky='news')
        self.nav_frame.grid_propagate(0)
        
        # create dashboard frame
        self.dashboard_frame = customtkinter.CTkFrame(self.login_frame, 
                                                      corner_radius=0,
                                                      fg_color='transparent')        
        self.dashboard_frame.grid(row=1, column=1, sticky='news')
        
        # create simulation frame
        self.simulation_frame = customtkinter.CTkFrame(self.login_frame, 
                                                      corner_radius=0,
                                                      fg_color='transparent')        
        self.simulation_frame.grid(row=1, column=1, sticky='news')

        # create setting frame
        self.setting_frame = customtkinter.CTkFrame(self.login_frame, 
                                                      corner_radius=0,
                                                      fg_color='transparent')        
        self.setting_frame.grid(row=1, column=1, sticky='news')


        '''
        ============= ADD WIDGETS TO FRAMES =============
        '''
        # add image to logo frame
        self.logo_label = customtkinter.CTkLabel(self.logo_frame, 
                                                 text='', 
                                                 image=self.logo_image)
        self.logo_label.pack()

        # add frame buttons
        self.dashboard_button = customtkinter.CTkButton(self.nav_frame, 
                                                   corner_radius=0, 
                                                   height=80,                         
                                                   text="Dashboard",
                                                   font=("Arial", 18),
                                                   fg_color="transparent", 
                                                   text_color=("gray10", "gray90"), 
                                                   hover_color=("gray70", "gray30"),
                                                   image=self.home_image,
                                                   command=self.dashboard_button_event,
                                                   anchor='w')        
        self.dashboard_button.grid(row=0, column=0, sticky='news')
        self.simulation_button = customtkinter.CTkButton(self.nav_frame, 
                                                   corner_radius=0, 
                                                   height=80,                         
                                                   text="Simulation Mode",
                                                   font=("Arial", 18),
                                                   fg_color="transparent", 
                                                   text_color=("gray10", "gray90"), 
                                                   hover_color=("gray70", "gray30"),
                                                   image=self.simulation_image,
                                                   command=self.simulation_button_event,
                                                   anchor='w')        
        self.simulation_button.grid(row=1, column=0, sticky='news')
        self.setting_button = customtkinter.CTkButton(self.nav_frame, 
                                                   corner_radius=0, 
                                                   height=80,                         
                                                   text="Setting",
                                                   font=("Arial", 18),
                                                   fg_color="transparent", 
                                                   text_color=("gray10", "gray90"), 
                                                   hover_color=("gray70", "gray30"),
                                                   image=self.setting_image,
                                                   command=self.setting_button_event,
                                                   anchor='w')        
        self.setting_button.grid(row=2, column=0, sticky='news')
        
        # add version label
        self.version_label = customtkinter.CTkLabel(self.nav_frame, 
                                                 text='Copyright\nDataTree\nv1.1.1',
                                                 anchor="s")
        self.version_label.grid(row=3, column=0, sticky='news', pady=20)
        
        
        '''
        ============= LOGIN PAGE =============
        '''

        # create login frame
        self.account_frame = customtkinter.CTkFrame(self.dashboard_frame, 
                                                    corner_radius=0,
                                                    fg_color="transparent")
        self.account_frame.grid(row=0, column=0, sticky='ns')       
        self.account_label = customtkinter.CTkLabel(self.account_frame, 
                                                    text="Login Page",
                                                    font=customtkinter.CTkFont(size=20, weight="bold"))
        self.account_label.grid(row=0, column=0, padx=30, pady=(150, 15))
        self.username_entry = customtkinter.CTkEntry(self.account_frame, width=250, placeholder_text="username")
        self.username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.password_entry = customtkinter.CTkEntry(self.account_frame, width=250, show="*", placeholder_text="password")
        self.password_entry.grid(row=2, column=0, padx=30, pady=(0, 15))
        self.login_button = customtkinter.CTkButton(self.account_frame, text="Login", command=lambda:self.loginOrHub(1,self,1), width=120)
        self.login_button.grid(row=3, column=0, padx=30, pady=(15, 15))
        self.signup_button = customtkinter.CTkButton(self.account_frame, text="Signup", command=lambda:self.loginOrHub(2,self,1), width=120)
        self.signup_button.grid(row=4, column=0, padx=30, pady=(0, 15))
        
        '''
        ============= SETTING PAGE =============
        '''
        # language
        self.language_label = customtkinter.CTkLabel(self.setting_frame, 
                                                     text = "Language:", 
                                                     font=("Arial", 18))
        self.language_label.grid(row=0, column=0, pady=(150, 20), sticky='e')
        self.language_optionmenu = customtkinter.CTkOptionMenu(self.setting_frame, 
                                                               values=["English", "Spanish", "French"],
                                                               anchor='center',
                                                               font=("Arial", 18))
        self.language_optionmenu.grid(row=0, column=1, padx=20, pady=(150, 20), sticky='w')

        # theme
        self.theme_label = customtkinter.CTkLabel(self.setting_frame, 
                                                  text="Theme:", 
                                                  font=("Arial", 18))
        self.theme_label.grid(row=1, column=0, pady=(0, 20), sticky='e')
        self.theme_optionemenu = customtkinter.CTkOptionMenu(self.setting_frame, 
                                                             values=["Light", "Dark"],
                                                             font=("Arial", 18),
                                                             anchor='center',
                                                             command=self.change_theme_event)
        self.theme_optionemenu.grid(row=1, column=1, padx=20, pady=(0, 20), sticky='w')

        # scaling
        self.scaling_label = customtkinter.CTkLabel(self.setting_frame, 
                                                    text="UI Scaling:", 
                                                    font=("Arial", 18))
        self.scaling_label.grid(row=2, column=0, pady=(0, 20), sticky='e')
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.setting_frame, 
                                                               values=["80%", "90%", "100%", "110%", "120%"],
                                                               font=("Arial", 18),
                                                               anchor='center',
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=2, column=1, padx=20, pady=(0, 20), sticky='w')


        '''
        ============= GRID CONFIGURE =============
        '''
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.nav_frame.columnconfigure(0, weight=1)
        self.login_frame.rowconfigure(1, weight=1)        
        self.login_frame.columnconfigure(1, weight=1)
        self.nav_frame.rowconfigure(3, weight=1)
        self.dashboard_frame.rowconfigure(0, weight=1)
        self.dashboard_frame.grid_columnconfigure(0, weight=1)
        self.setting_frame.columnconfigure((0,1), weight=1)
        self.setting_frame.grid_columnconfigure((0,1), weight=1)
        '''
        ============= SET DEFAULT VALUES =============
        '''
        self.select_frame_by_name("dashboard")
        self.scaling_optionemenu.set("100%")
        self.theme_optionemenu.set("Dark")
        

        
    '''
    ============= METHODS =============
    '''
    def select_frame_by_name(self, name):
        # set button color for selected button
        self.dashboard_button.configure(fg_color=("gray75", "gray25") if name == "dashboard" else "transparent")
        self.simulation_button.configure(fg_color=("gray75", "gray25") if name == "simulation" else  "transparent")
        self.setting_button.configure(fg_color=("gray75", "gray25") if name == "setting" else "transparent")
        # show selected frame
        if name == "dashboard":
            self.dashboard_frame.grid(row=1, column=1, sticky="nsew")
        else:
            self.dashboard_frame.grid_forget()
        if name == "simulation":
            self.simulation_frame.grid(row=1, column=1, sticky="nsew")
        else:
            self.simulation_frame.grid_forget()
        if name == "setting":
            self.setting_frame.grid(row=1, column=1, sticky="nsew")
        else:
            self.setting_frame.grid_forget()
    def dashboard_button_event(self):
        self.select_frame_by_name("dashboard")
    def simulation_button_event(self):
        self.select_frame_by_name("simulation")
    def setting_button_event(self):
        self.select_frame_by_name("setting")
    def change_theme_event(self, new_theme):
        customtkinter.set_appearance_mode(new_theme)
    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def addItems(self,choice):
            
            str=""
            total=""
            drinks=["Regular","Espresso","Latte","Cappuccino","Cocoa latte"]
            x=TakeOrders.order(choice)
            
            if x==False:
                messagebox.showwarning(parent=Win2,message="Not enough ingredients to make "+drinks[choice-1])
            else:
                str="{:.2f}".format(x[0])
                total="{:.2f}".format(x[1])
                global totalLabel
                
                totalLabel=customtkinter.CTkLabel(master= checkout_frame,
                                                  text=total+"$",
                                                  font=("Helvetica", 20))
                totalLabel.grid(row = 1, column = 1)
                list1.insert(END,drinks[choice-1]+": "+str)
            

                
    def checkOut(self,main):
        """Checks out users asks the if they are sure and processes if they click yes"""
        ch=messagebox.askquestion("Checkout","Are your sure you want to checkout",parent=Win2)
        if ch=='yes':
            id=TakeOrders.checkOut(username1)
            messagebox.showinfo(parent=Win2,message="Transaction complete oderID: "+str(id))
            list1.delete(0,END)
            TakeOrders.copyData()
            totalLabel.grid_forget()
            totalLabel1=customtkinter.CTkLabel(master= checkout_frame,
                                                  text="                          ",
                                                font=("Helvetica", 20))
            totalLabel1.grid(row = 1, column = 1)
            
            
                      
                
    def newWindow(self,main,choice,copy):
            """"performs all the functions of the application"""
            global Win2
            
            Win2=customtkinter.CTkToplevel(main)
            Win2.title("Warrior Cafe")
            Win2.geometry("800x600")
            
            Win1.destroy()
          
            #order button
            if choice==1:
                # load images
                
                self.image1=customtkinter.CTkImage(Image.open("reg.jpg"), size=(100,100))
                self.image2=customtkinter.CTkImage(Image.open("expresso.jpg"), size=(100,100))
                self.image3=customtkinter.CTkImage(Image.open("latte.jpg"), size=(100,100))
                self.image4=customtkinter.CTkImage(Image.open("cappa.jpg"), size=(100,100))
                self.image5=customtkinter.CTkImage(Image.open("cocoa.jpg"), size=(100,100))

                # create main frame
                order_frame = customtkinter.CTkFrame(Win2, fg_color="transparent")
                order_frame.grid(row = 0, column = 0, columnspan=2, sticky='news')
                order_frame.rowconfigure(0, weight=1)
                order_frame.columnconfigure((0,1), weight=1)
                
                # menu
                menu_frame = customtkinter.CTkFrame(order_frame, fg_color="transparent")
                menu_frame.grid(row = 0, column = 0, sticky='news')
                label1=customtkinter.CTkLabel(menu_frame,
                                              text='Menu Items',
                                              font=("Helvetica", 20))
                label1.grid(row = 0, column = 0, columnspan =2, pady =20)
                menu_frame.rowconfigure((0,1,2,3), weight= 1)
                menu_frame.columnconfigure((0,1), weight= 1)
                #creates image buttons
                button1=customtkinter.CTkButton(master=menu_frame,
                                                text="Regular",
                                                fg_color="transparent",
                                                image=self.image1,
                                                compound="top",
                                                command=lambda:self.addItems(1))
                button1.grid(row = 1, column = 0)
                
                button2=customtkinter.CTkButton(master=menu_frame,
                                                text="Espresso",
                                                fg_color="transparent",
                                                image=self.image2,
                                                compound="top",
                                                command=lambda:self.addItems(2))
                button2.grid(row = 1, column = 1)
                
                button3=customtkinter.CTkButton(master=menu_frame,
                                                text="Latte",
                                                fg_color="transparent",
                                                image=self.image3,
                                                compound="top",
                                                command=lambda:self.addItems(3))
                button3.grid(row = 2, column = 0)
                
                button4=customtkinter.CTkButton(master=menu_frame,
                                                image=self.image4,
                                                text="Cappa",
                                                fg_color="transparent",
                                                compound="top",
                                                command=lambda:self.addItems(4))
                button4.grid(row = 2, column = 1)
                
                button5=customtkinter.CTkButton(master=menu_frame,
                                                image=self.image5,
                                                fg_color="transparent",
                                                text="Cocoa",
                                                compound="top",
                                                command=lambda:self.addItems(5))
                button5.grid(row = 3, column = 0, columnspan=2)

                
                
                #listbox with scroll bar
                global checkout_frame
                checkout_frame = customtkinter.CTkFrame(order_frame, fg_color="transparent")
                checkout_frame.grid(row = 0, column=1)
                listbox1_frame = customtkinter.CTkFrame(checkout_frame)
                listbox1_frame.grid(row = 0, column=0, columnspan=2, pady=(0,20))
                scroll=Scrollbar(listbox1_frame)
                scroll.pack(side="right",fill="y")
                global list1
                list1=Listbox(listbox1_frame,yscrollcommand=scroll.set,width=38,height=20,font=("Helvetica", 10))
                list1.pack()
                scroll.config(command=list1.yview)

                total_label=customtkinter.CTkLabel(master=checkout_frame,
                                                   text='Total: ',
                                                   font=("Helvetica", 20))
                total_label.grid(row = 1, column=0)

                #checkout button
                checkout_button = customtkinter.CTkButton(master=checkout_frame,
                                    text="CHECKOUT",
                                    command=lambda: self.checkOut(main))
                checkout_button.grid(row = 2, column = 0, columnspan=2, pady=20)

                

                print("order button was pressed")
            #re-stock and set PRices function
            elif choice==2 or choice==3:
                #array used for  labels
                if choice==2:
                     namesList=['Current Inventory:',
                                'Choose Items to re-stock:',
                                'regular coffee beans(oz):',
                                'espresso coffee beans(oz)',
                                '1% milk(gal):',
                                'suger(packet):',
                                'non dairy creamer(packet):',
                                'cocoa power(oz):']  
                else:
                     namesList=['Current Prices:',
                                'Set Prices:',
                                'Regular:',
                                'Espresso:',
                                'Latte:',
                                'Cappuccino:',
                                'Cocoa Latte:']      
                
    
                # create frames
                Win2.set_frame = customtkinter.CTkFrame(Win2, corner_radius=0, border_width=0, fg_color="transparent")
                Win2.set_frame.grid(row=0, column=0,sticky='news')
                Win2.show_frame = customtkinter.CTkFrame(Win2, corner_radius=0, border_width=0,fg_color="transparent")
                Win2.show_frame.grid(row=0, column=1,sticky='news')
                Win2.rowconfigure(0, weight=1)
                Win2.columnconfigure((0,1), weight=1)
    
                # add widgets to set frame
                set_label_1=customtkinter.CTkLabel(master=Win2.set_frame,text=namesList[1], font=customtkinter.CTkFont(size=20, weight="bold"))
                set_label_1.grid(row=0, column=0, columnspan=2, pady=(50,20))
    
                set_label_2=customtkinter.CTkLabel(master=Win2.set_frame,text=namesList[2])
                set_label_2.grid(row=1,column=0, pady=(0,20))
    
                set_label_3=customtkinter.CTkLabel(master=Win2.set_frame,text=namesList[3])
                set_label_3.grid(row=2,column=0, pady=(0,20))
    
                set_label_4=customtkinter.CTkLabel(master=Win2.set_frame,text=namesList[4])
                set_label_4.grid(row=3,column=0, pady=(0,20))
    
                set_label_5=customtkinter.CTkLabel(master=Win2.set_frame,text=namesList[5])
                set_label_5.grid(row=4,column=0, pady=(0,20))
    
                set_label_6=customtkinter.CTkLabel(master=Win2.set_frame,text=namesList[6])
                set_label_6.grid(row=5,column=0, pady=(0,20))

                #entries
                regEntry=customtkinter.CTkEntry(master=Win2.set_frame, width=100)
                regEntry.grid(row=1,column=1, pady=(0,20))
                expressoEntry=customtkinter.CTkEntry(master=Win2.set_frame, width=100)
                expressoEntry.grid(row=2,column=1, pady=(0,20))
                milkEntry=customtkinter.CTkEntry(master=Win2.set_frame, width=100)
                milkEntry.grid(row=3,column=1, pady=(0,20))
                sugarEntry=customtkinter.CTkEntry(master=Win2.set_frame, width=100)
                sugarEntry.grid(row=4,column=1, pady=(0,20))
                creamEntry=customtkinter.CTkEntry(master=Win2.set_frame, width=100)
                creamEntry.grid(row=5,column=1, pady=(0,20))
                Win2.set_frame.columnconfigure((0,1), weight=1)

                # add widget to show frames
                label1=customtkinter.CTkLabel(master=Win2.show_frame,text=namesList[0],font=customtkinter.CTkFont(size=20, weight="bold"))
                label1.grid(row=0, column=0, sticky='news', pady=(50,20))
                Win2.list_frame=customtkinter.CTkFrame(Win2.show_frame, fg_color="transparent", corner_radius=0, border_width=0)
                Win2.list_frame.grid(row=1, column=0, sticky='news')
                global list2
                list2= Listbox(Win2.list_frame,
                                                width=28, 
                                                height=6,
                                                font=("Helvetica", 12))
                list2.pack()
                Win2.show_frame.columnconfigure(0, weight=1)
               
               
                #if statment that performs tasks based the pressed is re-stock or re-price
                if choice==2:
                    label9=customtkinter.CTkLabel(master=Win2.set_frame,
                                                  text='cocoa power(oz):')
                    label9.grid(row=6,column=0, pady=(0,20))
                    cocoaEntry=customtkinter.CTkEntry(master=Win2.set_frame, width=100)
                    cocoaEntry.grid(row=6,column=1, pady=(0,20))
                    addButton = customtkinter.CTkButton(master=Win2.set_frame,
                                                        text="ADD",
                                                        command=lambda: self. addToInventory(main,
                                                                                             regEntry.get(),
                                                                                             expressoEntry.get(),
                                                                                             milkEntry.get(),
                                                                                             sugarEntry.get(),
                                                                                             creamEntry.get(),
                                                                                             cocoaEntry.get()))
                    addButton.grid(row=8,column=0,columnspan=2, pady=(10,20))
                    for i in range(6):
                        list2.insert(END,inventory.ViewInventory(i))
                else:
                    PriceButton = customtkinter.CTkButton(master=Win2.set_frame,
                                                           text="SET",
                                                           command=lambda: self.setPrice (main,
                                                                                          regEntry.get(),
                                                                                          expressoEntry.get(),
                                                                                          milkEntry.get(),
                                                                                          sugarEntry.get(),
                                                                                          creamEntry.get()))
                    PriceButton.grid(row=8,column=0,columnspan=2, pady=(10,20))
                    for i in range(5):
                        list2.insert(END,inventory.ViewPrices(i))
                print("re-stock button was pressed")
            elif choice==4:
                global list3
                
                # create main frame 
                log_stat_frame = customtkinter.CTkFrame(Win2, fg_color="transparent")
                log_stat_frame.grid(row = 0, column = 0, columnspan=2, sticky='news')
                log_stat_frame.rowconfigure(0, weight=1)
                log_stat_frame.columnconfigure(0, weight=1)

                # create log frame
                log_frame=customtkinter.CTkFrame(log_stat_frame, fg_color="transparent")
                log_frame.grid(row = 0, column = 0, sticky='news')
                log_frame.rowconfigure(0, weight=1)
                log_frame.columnconfigure(0, weight=1)
                log_label=customtkinter.CTkLabel(log_frame,
                                                 text="LOGS:\n(An empty search returns all logs)",
                                                 font = customtkinter.CTkFont(family="Helvetica",
                                                                               size=16, 
                                                                               weight="bold"))
                log_label.grid(row = 0, column = 0)
                
                listbox3_frame = customtkinter.CTkFrame(log_frame)
                listbox3_frame.grid(row=1, column=0)
                list3=Listbox(listbox3_frame,width=100,
                              height=10,font=("Helvetica", 10))
                list3.pack(side="left",fill="y")
                scroll2=Scrollbar(listbox3_frame,orient='vertical') 
                scroll2.pack(side="right",fill="y")
                list3.config(yscrollcommand=scroll2.set)
                searchEntry=customtkinter.CTkEntry(log_frame, 
                                                   width=400,
                                                   font=("Helvetica", 9))
                searchEntry.grid(row = 2, column = 0, pady=25)
                searchButton = customtkinter.CTkButton(log_frame,
                                                       text="Search Logs",
                                                       command=lambda: self.logSearch(searchEntry.get()))
                searchButton.grid(row = 3, column = 0, pady=(0,25))
                
                # create statistic frame
                stat_frame=customtkinter.CTkFrame(log_stat_frame, fg_color="transparent")
                stat_frame.grid(row = 1, column = 0, sticky='news')
                stat_frame.rowconfigure(0, weight=1)
                stat_frame.columnconfigure(0, weight=1)
                
                label2=customtkinter.CTkLabel(master=stat_frame,
                                              text="STATISTICS:",
                                              font = customtkinter.CTkFont(family="Helvetica",
                                                                               size=16, 
                                                                               weight="bold"))
                label2.grid(row=0, column=0)
                listbox4_frame = customtkinter.CTkFrame(stat_frame)
                listbox4_frame.grid(row=1, column=0, pady=10)
                list4=Listbox(listbox4_frame,width=35,
                              height=5,font=("Helvetica", 10))
                list4.pack()
                
                # add logs to list box
                with open('AppData.json','r') as openfile:
                   Database=json.load(openfile)
                for i in Database['logs']:
                      list3.insert(END,Database['logs'][i])
                for i in range(5):
                      list4.insert(END,inventory.viewStats(i))


          

            #goes back to previous screen
            Win2.back_button_frame = customtkinter.CTkFrame(Win2, corner_radius=0, border_width=0, fg_color="transparent")
            Win2.back_button_frame.grid(row=1, column=0, columnspan=2, sticky='news')
            Win2.back_button = customtkinter.CTkButton(master=Win2.back_button_frame,
                                                text="BACK",
                                                command=lambda: self.close(2,main))
            Win2.back_button.grid(row=0, column=0)
            Win2.back_button_frame.rowconfigure(0, weight=1)
            Win2.back_button_frame.columnconfigure(0, weight=1)

            Win2.rowconfigure((0,1), weight=1)
            Win2.columnconfigure((0,1), weight=1)

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
            list2.delete(0,END)
            for i in range(6):
                        list2.insert(END,inventory.ViewInventory(i))
            
    def setPrice(self,main,reg,expr,latte,capa,cocoa):
        """Set menu prices after add button is pressed"""
        ch=messagebox.askquestion("Inventory","Are you sure you want to add these items\n to the inventory",parent=Win2)
        
        if ch=='yes':
            inventory.setPrice(reg,expr,latte,capa,cocoa,username1)
            messagebox.showinfo(parent=Win2,message="Transaction complete")
            list2.delete(0,END)
            for i in range(5):
                        list2.insert(END,inventory.ViewPrices(i))

    def close(self,choice,main):
        """Closes certain windows"""
        if(choice==1):
          Win1.destroy()
          self.deiconify()

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
          #Win1=tk.Toplevel(MainWin)
          Win1= customtkinter.CTkToplevel(MainWin)
          Win1.attributes("-topmost", True)
          Win1.title("Warrior Cafe")
          Win1.geometry("400x600")
          
          label0=customtkinter.CTkLabel(master=Win1,
                                        text='Sign Up',
                                        font=("Helvetica", 20))
          #opens new window when sign up button is pressed
         
          label1=customtkinter.CTkLabel(master=Win1,
                                        text='Passwords most be greater than six characters,\n and first and last names must only have alphabet characters.',
                                        font=("Helvetica", 14))
          userEntry=customtkinter.CTkEntry(master=Win1, width=200)
          firstEntry=customtkinter.CTkEntry(master=Win1, width=200)
          lastEntry=customtkinter.CTkEntry(master=Win1, width=200)
          passEntry=customtkinter.CTkEntry(master=Win1, width=200,show="*")
          label2=customtkinter.CTkLabel(master=Win1,text='Username')
          label3=customtkinter.CTkLabel(master=Win1,text='First Name')
          label4=customtkinter.CTkLabel(master=Win1,text='Last Name')
          label5=customtkinter.CTkLabel(master=Win1,text='Password')
          button1 = customtkinter.CTkButton(master=Win1,
                                            text="Register",
                                            command=lambda: self.register(userEntry.get(),
                                 firstEntry.get(),lastEntry.get(),passEntry.get()))
          
          firstEntry.get()
          #place entries and label to screen
          label0.place(relx=0.5,rely=0.1,anchor="center")
          label1.place(relx=0.5,rely=0.17,anchor="center")
          label2.place(relx=0.5,rely=0.3,anchor="center")
          label3.place(relx=0.5,rely=0.4,anchor="center")
          label4.place(relx=0.5,rely=0.5,anchor="center")
          label5.place(relx=0.5,rely=0.6,anchor="center")
          userEntry.place(relx=0.5,rely=0.35,anchor="center")
          firstEntry.place(relx=0.5,rely=0.45,anchor="center")
          lastEntry.place(relx=0.5,rely=0.55,anchor="center")
          passEntry.place(relx=0.5,rely=0.65,anchor="center")
          button1.place(relx=0.5,rely=0.75,anchor="center")
          
       elif choice==1:
            #logs ins in user
            global username1
            username1=self.username_entry.get()
            password=self.password_entry.get()
            #menu after login  
            if(loginChecks.checkLogin(username1,password,log)):
                
                Win1=customtkinter.CTkToplevel(MainWin)
                Win1.title("Warrior Cafe")
                Win1.geometry("800x600")
                Win1.attributes("-topmost", True)
                # create main frame
                Win1.main_frame = customtkinter.CTkFrame(Win1, 
                                                  corner_radius=0)
                Win1.main_frame.grid(row = 0, column = 0, sticky='news')
                Win1.rowconfigure(0, weight=1)
                Win1.columnconfigure(0, weight=1)
                # create logo frame
                Win1.logo_frame = customtkinter.CTkFrame(Win1.main_frame,
                                                 corner_radius=0,
                                                 height=180,
                                                 fg_color='#858585')
                Win1.logo_frame.grid(row = 0, column = 0, columnspan=2, sticky='news')
                Win1.main_frame.columnconfigure((0,1), weight=1)
                Win1.main_frame.rowconfigure((1,2,3,4), weight=1)

                # add image to logo frame
                Win1.logo_label = customtkinter.CTkLabel(Win1.logo_frame, 
                                                 text='', 
                                                 image=self.logo_image)
                Win1.logo_label.pack()
                
                #prints the users name 
                label7= customtkinter.CTkLabel(master=Win1.main_frame,
                                               text='WELCOME BACK '+(dataBase['usernames'][username1.lower()][0]).upper(),
                                               font=customtkinter.CTkFont(size=20, weight="bold"))
                label7.grid(row = 1, column = 0, columnspan=2)

                #Sub menu
                button2 = customtkinter.CTkButton(master=Win1.main_frame,
                                                  text="Order",
                                                  height=50,
                                                  font=customtkinter.CTkFont(size=16, weight="bold"),
                                                  command=lambda: self.newWindow(MainWin,1,TakeOrders.copyData()))
                button3= customtkinter.CTkButton(master=Win1.main_frame,
                                                 text="Restock",
                                                 height=50,
                                                 font=customtkinter.CTkFont(size=16, weight="bold"),
                                                 command=lambda: self.newWindow(MainWin,2,0))
                button4 = customtkinter.CTkButton(master=Win1.main_frame,
                                                  text="Logs &\n Statistics",
                                                  height=50,
                                                  font=customtkinter.CTkFont(size=16, weight="bold"),
                                                  command=lambda: self.newWindow(MainWin,4,0))
                button5 = customtkinter.CTkButton(master=Win1.main_frame,
                                                  text="Set Prices",
                                                  height=50,
                                                  font=customtkinter.CTkFont(size=16, weight="bold"),
                                                  command=lambda: self.newWindow(MainWin,3,0))
                button6 = customtkinter.CTkButton(master=Win1.main_frame,
                                                  text="Log out",
                                                  font=customtkinter.CTkFont(size=16, weight="bold"),
                                                  command=lambda: self.close(1,MainWin))
                
                button2.grid(row=2, column=0, sticky='e', padx = 30)
                button3.grid(row=2, column=1, sticky='w', padx = 30)
                button4.grid(row=3, column=0, sticky='e', padx = 30)
                button5.grid(row=3, column=1, sticky='w', padx = 30)
                button6.grid(row=4, column=0, columnspan=2)
                
           
              
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
    customtkinter.set_default_color_theme("green")
    app = App()
    app.mainloop()
    
    