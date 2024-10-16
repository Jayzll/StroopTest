from tkinter import *
from customtkinter import *
from PIL import Image
from tkinter import messagebox
from hashlib import sha1

import sqlite3 as s
from StroopTestFunc import StroopStartScreen
import importlib as w
import re
#Create database
def set_database():
    #Create connection to db
    db = s.connect(r"login.db")
    #Create cursor to interact with db
    cursor = db.cursor()
    #Create the user table in the db
    table = '''CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    email TEXT NOT NULL
    )
    '''
    #Execute the table 
    cursor.execute(table)
    #Insert values into the coloumns 
    sql = """INSERT INTO users (username, password, email) VALUES (?, ?, ?)"""
    #Exception Handling - Try inserting 0
    try:
        cursor.execute(sql, (0, 0, 0,))
    except s.IntegrityError:
        #If data does not have a uniqueness constraint then print the statement below
        print("data is stored")
    #Commit to changes in db
    db.commit()
set_database()

class Create_Page:
    def __init__(self, root, func):
        #To export username to other files
        self.username = ""
        self.root = root
        if not func.__module__ == "StroopTestFunc":
            self.create_page()
        

    def create_page(self):
        #Create page window configuration  
        self.root.title("Create Page")
        self.root.configure(fg_color=('#ddddff', '#F6F4EB'))
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        set_appearance_mode("system") 
        #colors
        self.color_1 = "#461959"
        self.color_2 = "white"
        self.color_3 = "black"
        #images
        self.img2 = CTkImage(Image.open('image/doodle_login.png'),size=(700,489))
        self.img3 = CTkImage(Image.open('image/Cross.png'), size=(30,30))   
        #Shape
        self.rectangle = CTkFrame(master=self.root,width=600,height=700, corner_radius=100, fg_color=(self.color_1, '#4682A9'))
        self.rectangle.place(relx = 0.7, rely = 0.5, anchor ='center')

        #globalised widgets
        self.username_entry = CTkEntry(self.root, font=('Cooper Black', 30), width = 400, height = 25, bg_color=(self.color_1))
        self.username_entry.place(relx = 0.7, rely = 0.35, anchor ='center')

        self.email_entry = CTkEntry(self.root, font=('Cooper Black', 30), text_color= "grey", width = 400, height = 25, bg_color=(self.color_1))
        self.email_entry.insert(0, "name@email.com")
        self.email_entry.place(relx = 0.7, rely = 0.45, anchor ='center')
        self.email_entry.bind("<FocusIn>", self.temp_text)

        self.password_entry = CTkEntry(self.root, font=('Cooper Black', 30), show="*", width = 400, height = 25, bg_color=(self.color_1))
        self.password_entry.place(relx = 0.7, rely = 0.55, anchor ='center')

        self.widgets()

    #Function to create the temp text
    def temp_text(self, e):
        self.email_entry.delete(0,"end")

        
    def widgets(self):
        #UI
        pic1 = CTkLabel(self.root,text= "", image=self.img2)
        pic1.place(relx = 0.25, rely = 0.4, anchor ='center')

        label_l = CTkLabel(self.root, text='WELCOME TO STROOP TEST', font=('Cooper Black', 40), text_color=self.color_3)
        label_l.place(relx = 0.25, rely = 0.1, anchor ='center')

        label_i = CTkLabel(self.root, text='Create An Account', font=('Cooper Black', 50, 'bold'), text_color= self.color_2, fg_color=(self.color_1, '#4682A9'))
        label_i.place(relx = 0.7, rely = 0.25, anchor ='center')

        warning_label = CTkLabel(self.root, text='Password must be 8 characters long', font=('Cooper Black', 30, 'bold'), text_color=self.color_3)
        warning_label.place(relx = 0.25, rely = 0.7, anchor ='center')

        warning_label = CTkLabel(self.root, text='Password must contain at least one uppercase and lowercase, numbers and symbols', font=('Cooper Black', 30, 'bold'), wraplength=600, text_color= self.color_3)
        warning_label.place(relx = 0.25, rely = 0.8, anchor ='center')

        username_label = CTkLabel(self.root, text="Username", font=('Cooper Black', 30), text_color=(self.color_2), bg_color=(self.color_1, '#4682A9'))
        username_label.place(relx = 0.64, rely = 0.3, anchor ='center')

        email_label = CTkLabel(self.root, text="Email", font=('Cooper Black', 30), text_color=(self.color_2), fg_color=(self.color_1, '#4682A9'))
        email_label.place(relx = 0.625, rely = 0.4, anchor ='center')

        password_label = CTkLabel(self.root, text="Password", font=('Cooper Black', 30), text_color=(self.color_2), fg_color=(self.color_1, '#4682A9'))
        password_label.place(relx = 0.64, rely = 0.5, anchor ='center')

        create_button = CTkButton(self.root, text="Create Account", font=('Cooper Black', 30), text_color = 'black', hover_color = "red", fg_color=('#ddddff', '#F6F4EB'), bg_color=(self.color_1), command=self.create_ac)
        create_button.place(relx = 0.7, rely = 0.65, anchor ='center')

        self.root.bind('<Return>',self.key_press)

        back_button = CTkButton(self.root, text="Back", font=('Cooper Black', 30), text_color = 'black', fg_color=('#ddddff', '#F6F4EB'), bg_color=(self.color_1), command=self.back)
        back_button.place(relx = 0.7, rely = 0.75, anchor ='center')

        exitButton = CTkButton(self.root, text= "",width=1, height=1, fg_color=('#F6F4EB', '#383842'), hover_color = "red", command= self.clickExitButton)
        exitButton.configure(self.root, image=self.img3)
        exitButton.place(relx = 1, x =-1, y = 1, anchor = N)

    def key_press(self, e):
                if e.keysym == "Return":
                    self.create_ac()
                  

    def create_ac(self):
        #Create Account Function
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()
        self.email = self.email_entry.get()
        self.db = s.connect(r"login.db")
        self.cursor = self.db.cursor()
        email_pattern = r"^(?=.*[@])$"

        # Password Validation 
        pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&+=!])(?=\S+$).{8,}$"

        if not re.match(pattern, self.password):
            requirements = []
            if len(self.password) < 8:
                requirements.append("- Password must be at least 8 characters long")
            if not any(c.isupper() for c in self.password):
                requirements.append("- Password must contain at least one uppercase letter")
            if not any(c.islower() for c in self.password):
                requirements.append("- Password must contain at least one lowercase letter")
            if not any(c.isdigit() for c in self.password):
                requirements.append("- Password must contain at least one digit")
            if not any(c in "!@#$%^&+=" for c in self.password):
                requirements.append("- Password must contain at least one special character (@#$%^&+=)")

            requirements_text = "\n".join(requirements)
            messagebox.showwarning("Password Security", f"The password you entered is not secure. Please make sure your password meets the following requirements:\n\n{requirements_text}")
        else:
            self.sql1 = "SELECT id FROM users"
            self.cursor.execute(self.sql1)
            self.userid = self.cursor.fetchone()
            #Username Validation 
            self.sql1 = """UPDATE users SET username = ? WHERE id = ?"""
            BOOT = True
            try:
                self.cursor.execute(self.sql1, (self.username, self.userid[0],))
            except s.IntegrityError:
                BOOT = False
                messagebox.showwarning("error","USERNAME IS ALREADY USED")
            COOT = True
            if not re.match(email_pattern, self.email):
                if not any(c in "@" for c in self.email):
                    COOT = False
                    messagebox.showwarning("Email", "It is not an email")

            if BOOT and COOT == True:
                #Database update
                self.sql2 = """UPDATE users SET password = ? WHERE id = ?"""
                hash = sha1(self.password.encode("utf-8")).hexdigest()
                self.cursor.execute(self.sql2, (hash, self.userid[0],))
                if self.password != hash:
                    print("hash complete")
                
                self.sql3 = """UPDATE users SET email = ? WHERE id = ?"""
                self.cursor.execute(self.sql3, (self.email, self.userid[0],))
                print("Email :", self.email)

                print(self.cursor.rowcount, "record inserted.")
                print("This is UserID", self.userid)
                self.db.commit()
                self.root.withdraw()
                self.open_game()
            else:
                self.db.rollback()
                messagebox.showwarning("error","Account Not Created")

    def open_game(self):
        #Function to 
        stroop_root = CTkToplevel()
        app = StroopStartScreen(stroop_root, self.username)
        print("Create Page Username = ", self.username)
        stroop_root.mainloop()

    def back(self):
        self.root.withdraw()
        try:
             go_back = getattr(w.import_module('Welcome'), 'Welcome').go_main(self)
             return go_back()
        except AttributeError:
             return "Function not found in the module."
    
    
    def clickExitButton(self):
            exit()


