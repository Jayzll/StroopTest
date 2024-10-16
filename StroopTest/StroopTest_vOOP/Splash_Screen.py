from tkinter.ttk import Progressbar
from customtkinter import *
from PIL import Image
import time 
from Welcome import Welcome
import pyglet as p

class Splash_Screen:
    def __init__(self, root):   
        #Window Configuration
        self.root = root
        self.root.title("Loading")
        self.root.geometry('427x250')
        self.root.configure(fg_color=('#272727'))
        self.root.resizable(False, False)

        self.bg = CTkImage(Image.open('image/rainbow.jpg'), size=(427,250)) 

        self.widgets()
        p.font.add_file('fonts/HOGFISH DEMO.OTF')
        p.font.add_file('fonts/Cooper Black.TTF')


    def key_press(self, e):
                if e.keysym == "Return":
                    self.bar()   
    #Function that contains all widgets for Splash Screen
    def widgets(self):

        bg_img = CTkLabel(self.root,text= "", image=self.bg)
        bg_img.pack()

        rectangle = CTkFrame(master=self.root,width=350,height=160, fg_color=('white'))
        rectangle.place(relx = 0.5, rely = 0.5, anchor ='center')
        
        b1 = CTkButton(self.root, text='START', font=('Hogfish DEMO', 20), text_color='black', fg_color="#e3e5e6", corner_radius=1, hover_color="red", command=self.bar)
        b1.place(relx = 0.5, rely = 0.535, anchor ='center')
        self.root.bind('<Return>',self.key_press)

        t1 = CTkLabel(self.root, text='STROOP TEST', font=('Hogfish DEMO', 40), text_color="black", corner_radius= 1, fg_color="white")
        t1.place(relx = 0.5, rely=0.35, anchor = 'center')

        crd = CTkLabel(self.root, text= '© 2023 Jupiter All Rights Reserved', font=('Cooper Black', 10), text_color="black", corner_radius= 1, fg_color="white")
        crd.place(relx = 0.5, rely=0.7, anchor = 'center')
        
    #Function for the bar
    def bar(self):
        Loading_Label = CTkLabel(self.root, text='LOADING', font=('Cooper Black', 20), text_color="black", corner_radius= 2, fg_color="white")
        Loading_Label.place(relx = 0.5, rely = 0.9, anchor ='center')   
        progressbar = Progressbar(self.root, orient=HORIZONTAL, length=300, mode='determinate')
        progressbar.place(relx = 0.5, rely = 0.8, anchor ='center')

        final = 100
        value = 0 
        # A while loop to make the loading animation in the bar 
        while(value<final):
                time.sleep(0.03)
                progressbar['value'] += 2
                value+=1
                self.root.update_idletasks()  
                value = value + 1
        self.root.withdraw()
        
        self.open_window()
    #This function open a new page called Welcome
    def open_window(self):
        welcome_root = CTkToplevel()
        app = Welcome(welcome_root)
        welcome_root.mainloop()

# The function to load up the Splash Screen
def main():
    root = CTk()
    app = Splash_Screen(root)
    root.mainloop()

if __name__ == "__main__":
    main()