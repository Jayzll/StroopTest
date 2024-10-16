from tkinter import *
from customtkinter import *
from PIL import Image
from Create_Page import Create_Page
from Login_Page import Login_Page
import importlib as w

#Define a class
class Main_Title:
    #Create an instance in a class with 2 parameters self and root
    def __init__(self, root):
        #Window Configuration
        self.root = root
        self.root.title('Stroop Test')
        self.root.configure(fg_color=('#ddddff', '#383842'))
        self.root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
        set_appearance_mode("system") 

        #Images
        self.__img3 = CTkImage(Image.open('image/Cross.png'), size=(30,30))  
        self.__img2 = CTkImage(Image.open('image/Splash_Color.png'), size=(2000,2000))  

        self.widget()

    def widget(self):
        #UI
        bg = CTkLabel(self.root,text= "", image=self.__img2)
        bg.place(relx = 0.5, rely = 0.5, anchor ='center')

        rectangle = CTkFrame(master=self.root,width=600,height=700,corner_radius=100, fg_color=('#ddddff', '#383842'))
        rectangle.place(relx = 0.5, rely = 0.5, anchor ='center')

        label_t = CTkLabel(self.root, text='STROOP TEST', font=('Hogfish DEMO', 60))
        label_t.place(relx = 0.5, rely = 0.3, anchor ='center')

        c1 = CTkButton(self.root, text="Create", font=('Hogfish DEMO', 60),  text_color=("black", "white"),fg_color=('#ddddff', '#383842'), hover_color = "red", command=self.go_create)
        c1.place(relx = 0.5, rely = 0.45, anchor ='center')

        l1_button = CTkButton(self.root, text="Login", font=('Hogfish DEMO', 60), text_color=("black", "white"),fg_color=('#ddddff', '#383842'), hover_color = "blue", command=self.go_login)
        l1_button.place(relx = 0.5, rely = 0.6, anchor ='center')
                  

        b1 = CTkButton(self.root, text="Back", font=('Hogfish DEMO', 60), text_color=("black", "white"), fg_color=('#ddddff', '#383842'), hover_color = "yellow", command=self.back)
        b1.place(relx = 0.5, rely = 0.75, anchor ='center')

        exitButton = CTkButton(self.root, text= "",width=1, height=1, fg_color=('#ddddff', '#383842'), hover_color = "red", command= self.clickExitButton)
        exitButton.configure(self.root, image=self.__img3)
        exitButton.place(relx = 1, x =-1, y = 1, anchor = NE)

#Buttons 
    def clickExitButton(self):
            exit()
    
    def go_create(self):
        self.root.withdraw()
        create_page = CTkToplevel()
        app = Create_Page(create_page, self.go_create)
        create_page.mainloop()

    def go_login(self):
        self.root.withdraw()
        login_page = CTkToplevel()
        app = Login_Page(login_page, self.go_login)
        login_page.mainloop()

    def back(self):
        self.root.withdraw()
        try:
             go_back = getattr(w.import_module('Splash_Screen'), 'Splash_Screen').open_window(self)
             return go_back()
        except AttributeError:
             return "Function not found in the module."
    