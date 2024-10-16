from tkinter import *
from customtkinter import *
from tkinter import messagebox
from PIL import Image
import random as r
import sqlite3 as s
from Recreate_Password import Recreate_Password
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import importlib as w

class Password_Reset_Email:
    def __init__(self, root, func):

        self.username = ""
        self.root = root
        if not func.__module__ == "Recreate_Password":
            self.Password_Page()
        
    def Password_Page(self):
        self.root.title('Rest Password')
        self.root.configure(fg_color=('#ddddff', '#383842'))
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        set_appearance_mode("system") 

        self.img = CTkImage(Image.open('image/Cross.png'), size=(30, 30))

        self.color = "#F2C75B"
        self.color_d = "#f99800"

        self.rectangle = CTkFrame(master=self.root,width=700,height=800,corner_radius=100, fg_color=self.color)
        self.rectangle.place(relx = 0.5, rely = 0.5, anchor ='center')

        self.username_entry = CTkEntry(self.root, font=('Cooper Black', 30), width = 500, height = 25)
        self.username_entry.place(relx = 0.5, rely = 0.5, anchor ='center')

        self.widgets()

    def temp_text(self, e):
        self.email_entry.delete(0,"end")

    def widgets(self):

        label_t = CTkLabel(self.root, text='Password Reset', fg_color=(self.color), font=('Cooper Black', 60))
        label_t.place(relx=0.5, rely=0.3, anchor='center')

        username_label = CTkLabel(self.root, text='Enter your username', fg_color=(self.color), font=('Cooper Black', 20))
        username_label.place(relx=0.43, rely=0.46, anchor='center')

        psw_reset_button = CTkButton(self.root, text='Reset Password', font=('Cooper Black', 30), fg_color=(self.color_d), bg_color=(self.color), text_color = "black", hover_color = "red", command=self.send_mail)
        psw_reset_button.place(relx=0.5, rely=0.6, anchor='center')

        back = CTkButton(self.root, text="Back", font=('Cooper Black', 30), fg_color=(self.color_d), bg_color=(self.color), text_color = "black", hover_color = "red", command=self.back)
        back.place(relx = 0.5, rely = 0.85, anchor ='center')

        exitButton = CTkButton(self.root, text= "",width=1, height=1, fg_color=('#ddddff'), hover_color = "red", command= self.clickExitButton)
        exitButton.configure(self.root, image=self.img)
        exitButton.place(relx = 1, x =-1, y = 1, anchor = NE)

    def key_press(self, e):
                if e.keysym == "Return":
                    self.check_code()
                  

    def send_mail(self):
        db = s.connect(r"login.db")
        self.username = self.username_entry.get()
        if not os.path.isfile("login.db"):
            messagebox.showerror("Stroop Test", "Database not found")
            return
        cursor = db.cursor()
        cursor.execute("SELECT username FROM users")
        all_usernames = [row[0] for row in cursor.fetchall()]

        # Check if the provided username exists in the list of usernames
        if self.username in all_usernames:
            # User exists
            BOOT = True
            print("Username exists.")
        else:
            # User does not exist
            BOOT = False
            print("Username does not exist.")
            messagebox.showwarning("error","USERNAME NOT FOUND")

        if BOOT == TRUE:    
            cursor = db.cursor()
            id_fetch = "SELECT id FROM users WHERE username = ?"
            cursor.execute(id_fetch, (self.username,))
            userid_email = cursor.fetchone()
            print("This is UserID", userid_email)

            email_fetch = "SELECT email FROM users WHERE id = ?"
            cursor.execute(email_fetch, (userid_email[0],))
            self.email = cursor.fetchone()
            print("Email: ", self.email[0])

            code_label = CTkLabel(self.root, text='Enter the code', fg_color=(self.color), bg_color=(self.color), font=('Cooper Black', 20))
            code_label.place(relx=0.43, rely=0.65, anchor='center')

            self.code_enter_entry = CTkEntry(self.root, font=('Cooper Black', 20), width = 500, height = 40, bg_color=(self.color), text_color = "gray")
            self.code_enter_entry.place(relx=0.5, rely=0.7, anchor='center')
            
            code_enter_button = CTkButton(self.root, text='Confirm', font=('Cooper Black', 30), fg_color=(self.color_d), bg_color=(self.color), text_color = "black", hover_color = "red", command=self.check_code)
            code_enter_button.place(relx=0.5, rely=0.8, anchor='center')
            self.root.bind('<Return>',self.key_press)

            self.rand_num = str(r.randint(99999,999999))

            #SMTP Code 
            #Initalising the variables
            sender_email = 'jupiterstrooptest@hotmail.com'
            message = 'Hello! We got a request to change your password. This is a random generated number: ' + self.rand_num

            #Use MIMEMultipart to create the email message
            msg = MIMEMultipart()
            msg['From'] = sender_email

            #Set recipient to the email fetched from db
            msg['To'] = self.email[0]
            print("Email Delivery :", self.email[0])
            #Email Subject
            msg['Subject'] = 'Reset Password'
            #Select Plain style
            msg.attach(MIMEText(message, 'plain'))

            #Connect SMTP to Office 365
            server = smtplib.SMTP('smtp.office365.com', 587)
            #Secure the connection with TLS
            server.starttls()
            #Login to the sender email
            server.login(sender_email, 'CIS2022!')
            #Send the email
            server.send_message(msg)
            #Close the connection
            server.quit()

            print('Mail Sent')

    def check_code(self):
        #Check if the six digit code is correct
        self.sixdigitcode = self.code_enter_entry.get()
        if self.sixdigitcode == self.rand_num:
            print("Successful")
            self.root.withdraw()
            self.continue_password()
        else:
            retry_label = CTkLabel(self.root, text="Try Again", font=('Comic Sans MS', 18), text_color="black", fg_color=(self.color))
            retry_label.place(relx=0.5, rely=0.75, anchor='center')
            print("Try Again")

    def clickExitButton(self):
            exit()

    def continue_password(self):

        recreate_password_page = CTkToplevel()
        app = Recreate_Password(recreate_password_page, self.username)
        recreate_password_page.mainloop()


    def back(self):
        self.root.withdraw()
        try:
             go_back = go_back = getattr(w.import_module('Splash_Screen'), 'Splash_Screen').open_window(self)
             return go_back()
        except AttributeError:
             return "Function not found in the module."

