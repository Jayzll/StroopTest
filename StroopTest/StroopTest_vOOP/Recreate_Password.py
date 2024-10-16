from tkinter import *
from customtkinter import *
from PIL import  Image
from hashlib import sha1
import re
import importlib as w
import sqlite3 as s
from tkinter import messagebox

#Define a class
class Recreate_Password:
    #Create an instance in a class with 3 parameters self, root and username
    def __init__(self, root, username):
        #Window Configuration
        self.root = root
        self.username = username
        self.root.title("Password Reset")
        self.root.configure(fg_color=('#ddddff', '#383842'))
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        set_appearance_mode("system")

        #Images
        self.img = CTkImage(Image.open('image/Cross.png'), size=(30, 30))

        #Color palette
        self.color = "#ec4174"
        self.color_d = "#a83154"

        #Shape
        self.rectangle = CTkFrame(master=self.root,width=700,height=800,corner_radius=100, fg_color=self.color)
        self.rectangle.place(relx = 0.5, rely = 0.5, anchor ='center')

        self.widgets()
        self.get_username()
    #Function import username from Password Reset Email file
    def get_username(self):
        from Password_Reset_Email import Password_Reset_Email
        lpg = Password_Reset_Email(self.root, self.get_username)
        print("Username = ", self.username)

    def widgets(self):

        label_t = CTkLabel(self.root, text='Reset Password', font=('Cooper Black', 60), fg_color=(self.color))
        label_t.place(relx=0.5, rely=0.3, anchor='center')

        password_label = CTkLabel(self.root, text="Enter your new password", font=('Cooper Black', 30), text_color=("black"), fg_color=(self.color))
        password_label.place(relx = 0.5, rely = 0.45, anchor ='center')

        self.password_entry = CTkEntry(self.root, font=('Cooper Black', 30), show="*", width = 500, height = 25)
        self.password_entry.place(relx = 0.5, rely = 0.5, anchor ='center')

        reset_b = CTkButton(self.root, text="Reset", font=('Cooper Black', 30), fg_color=(self.color_d), bg_color=(self.color), text_color = "black", hover_color = "red", command=self.update_password)
        reset_b.place(relx = 0.5, rely = 0.65, anchor ='center')

        back_b = CTkButton(self.root, text="Back", font=('Cooper Black', 30), fg_color=(self.color_d), bg_color=(self.color), text_color = "black", hover_color = "red", command=self.back)
        back_b.place(relx = 0.5, rely = 0.7, anchor ='center')

        exitButton = CTkButton(self.root, text= "",width=1, height=1, fg_color=('#ddddff', '#383842'), hover_color = "red", command= self.clickExitButton)
        exitButton.configure(self.root, image=self.img)
        exitButton.place(relx = 1, x =-1, y = 1, anchor = NE)

    def update_password(self):
        self.password = self.password_entry.get()

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

            # Show the password requirements to the user
            requirements_text = "\n".join(requirements)
            messagebox.showwarning("Password Security", f"The password you entered is not secure. Please make sure your password meets the following requirements:\n\n{requirements_text}")
        else:
            self.db = s.connect(r"login.db")
            self.cursor = self.db.cursor()
            self.sql1 = "SELECT id FROM users WHERE username = ?"
            self.cursor.execute(self.sql1, (self.username,))
            self.userid = self.cursor.fetchone()
            print(self.userid[0])
            BOOT = True
            try:
                self.sql = """UPDATE users SET password = ? WHERE id = ?"""
                hash = sha1(self.password.encode("utf-8")).hexdigest()
                self.cursor.execute(self.sql, (hash, self.userid[0],))
                print(hash)
                self.db.commit()
                self.cursor.close()
                self.db.close()
                if self.password != hash:
                    print("hash complete")
                print("New Password Reset")
            except s.IntegrityError:
                BOOT = False
                messagebox.showwarning("error","PASSWORD IS ALREADY USED")

            if BOOT:
                    self.root.withdraw()
                    self.go_login()
            else:
                    messagebox.showwarning("error","Password not reset")#
            


    def go_login(self):
        self.root.withdraw()
        login_page = CTkToplevel()
        app = getattr(w.import_module('MainTitle'), 'Main_Title').go_login(self)
        login_page.mainloop()
    
    
    def clickExitButton(self):
            exit()

    def back(self):
        self.root.withdraw()
        try:
             go_back = getattr(w.import_module('Splash_Screen'), 'Splash_Screen').open_window(self)
             return go_back()
        except AttributeError:
             return "Function not found in the module."
        

