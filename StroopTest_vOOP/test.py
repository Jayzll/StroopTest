from tkinter import *
from customtkinter import *
import random as r

rand_num = str(r.randint(99999,999999))


def check_code(self):
        #Check if the six digit code is correct
        count = 0
        if self.sixdigitcode == self.code_enter_entry.get():
            Flag = True
        while Flag == False:
            if count == 5:
                locked_label = CTkLabel(self.root, text="Sorry Your Account is locked", font=('Comic Sans MS', 18))
                locked_label.place(relx=0.5, rely=0.65, anchor='center')
                print("Sorry Your Account is locked")
                
            elif Flag:
                successful_label = CTkLabel(self.root, text="Successful", font=('Comic Sans MS', 18))
                successful_label.place(relx=0.5, rely=0.65, anchor='center')
                print("Successful")
                self.root.withdraw()
                self.continue_password()
                count = 0
            else:
                retry_label = CTkLabel(self.root, text="Try Again", font=('Comic Sans MS', 18))
                retry_label.place(relx=0.5, rely=0.65, anchor='center')
                print("Try Again", )
                count = count + 1 