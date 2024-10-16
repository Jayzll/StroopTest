import tkinter as tk
from customtkinter import *
from PIL import Image
from tkinter import messagebox
from hashlib import sha1
from StroopTestFunc import StroopStartScreen
from Password_Reset_Email import Password_Reset_Email

import sqlite3 as s
import importlib as w
import os.path

class Login_Page:
    def __init__(self, root, func):
        self.root = root
        #To export username to other files
        self.username = ""
        if not func.__module__ == "StroopTestFunc":
            self.login_page()

        if not func.__module__ == "StroopStartScreen":
            self.login_page()
    #Login page window configuration  
    def login_page(self):
        self.root.title('Login In')
        self.root.configure(fg_color=('#ddddff', '#383842'))
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry("{0}x{1}+0+0".format(screen_width, screen_height))
        set_appearance_mode("system") 
        #color palette
        self.color_c = "#8db8a5"
        self.color_dc = "#16916e"
        self.color_w = "white"
        self.color_b = "black"
        # Resize the image relative to the screen size
        image_width = int(screen_width * 0.3)  # 30% of screen width
        image_height = int(screen_height * 0.3)  # 40% of screen height
        #images
        self.__img2 = CTkImage(Image.open('image/doodle_login.png'), size=(image_width, image_height))
        self.__img3 = CTkImage(Image.open('image/Cross.png'), size=(30,30))

        #Shape
        self.__rectangle = CTkFrame(master=self.root,width=600,height=700, corner_radius=100, fg_color=(self.color_c, '#4682A9'))
        self.__rectangle.place(relx = 0.7, rely = 0.5, anchor ='center')
        
        #Globalised entry boxes
        self.username_entry = CTkEntry(self.root, font=('Cooper Black', 30), width = 400, height = 25)
        self.username_entry.place(relx = 0.7, rely = 0.45, anchor ='center')

        self.password_entry = CTkEntry(self.root, font=('Cooper Black', 30), show="*", width = 400, height = 25)
        self.password_entry.place(relx = 0.7, rely = 0.55, anchor ='center')

        self.widgets()

    def widgets(self):

        pic1 = CTkLabel(self.root,text= "", image=self.__img2)
        pic1.place(relx = 0.2, rely = 0.5, anchor ='center')

        label_l = CTkLabel(self.root, text='WELCOME BACK', font=('Cooper Black', 50), text_color=self.color_b)
        label_l.place(relx = 0.2, rely = 0.25, anchor ='center')

        label_i = CTkLabel(self.root, text='Log in and beat your high score', font=('Cooper Black', 40, 'bold'), wraplength=400, fg_color=(self.color_c))
        label_i.place(relx = 0.7, rely = 0.3, anchor ='center')

        username_label = CTkLabel(self.root, text="Username:", font=('Cooper Black', 30), fg_color=(self.color_c))
        username_label.place(relx = 0.64, rely = 0.4, anchor ='center')

        password_label = CTkLabel(self.root, text="Password:", font=('Cooper Black', 30), fg_color=(self.color_c))
        password_label.place(relx = 0.64, rely = 0.5, anchor ='center')

        reset_password = CTkButton(self.root, text="Reset Password", font=('Cooper Black', 30), hover_color = "red", fg_color=(self.color_dc), bg_color=(self.color_c), command=self.open_password_reset)
        reset_password.place(relx = 0.7, rely=0.65, anchor = 'center')

        login_button = CTkButton(self.root, text="Login", font=('Cooper Black', 30), hover_color = "orange", fg_color=(self.color_dc), bg_color=(self.color_c), command=self.login)
        login_button.place(relx = 0.7, rely = 0.7, anchor ='center')
        self.root.bind('<Return>',self.key_press)

        back_button = CTkButton(self.root, text="Back", font=('Cooper Black', 30), fg_color=(self.color_dc), bg_color =(self.color_c), command=self.back)
        back_button.place(relx = 0.7, rely = 0.75, anchor ='center')

        exitButton = CTkButton(self.root, text= "",width=1, height=1, fg_color=('#ddddff', '#383842'), hover_color = "red", command= self.clickExitButton)
        exitButton.configure(self.root, image=self.__img3)
        exitButton.place(relx = 1, x =-1, y = 1, anchor = NE)

    def key_press(self, e):
                if e.keysym == "Return":
                    self.login()
                  

    def login(self):
        #Login function
        username = self.username_entry.get()
        password = self.password_entry.get()
        password = sha1(password.encode("utf-8")).hexdigest()

        if not os.path.isfile("login.db"):
            messagebox.showerror("Stroop Test", "Database not found")
            return
        
        self.db = s.connect(r"login.db")
        self.cursor = self.db.cursor()
        self.sql = "SELECT username FROM users WHERE username = ? AND password = ?"
        self.cursor.execute(self.sql, (username, password,))
        self.username = self.cursor.fetchone()
        self.db.close()
        #Check if username and password matches
        if self.username:
            self.root.withdraw()
            self.open_game()
        else:
            messagebox.showwarning("Stroop Test", "Login Fail")
    
    def open_game(self):
        self.root.withdraw()
        stroop_start_root = CTkToplevel()
        app = StroopStartScreen(stroop_start_root, self.username[0])
        print("Login Page Username = ", self.username[0])
        stroop_start_root.mainloop()

    def open_password_reset(self):
        self.root.withdraw()
        password_reset_root = CTkToplevel()
        app = Password_Reset_Email(password_reset_root, self.open_password_reset)
        password_reset_root.mainloop()

    def back(self):
        self.root.withdraw()
        try:
             go_back = getattr(w.import_module('Welcome'), 'Welcome').go_main(self)
             return go_back()
        except AttributeError:
             return "Function not found in the module."
    
    
    def clickExitButton(self):
            exit()



        
