from tkinter import *
from customtkinter import *
from PIL import Image
import importlib as w

class instruction:
    def __init__(self, root):
        self.root = root

        self.root.title("Stroop Test Instructions")
        self.root.configure(fg_color=('#ddddff', '#383842'))
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        set_appearance_mode("system")

        self.img = CTkImage(Image.open('image/Cross.png'), size=(30, 30))

        self.widgets()

    def widgets(self):

        label_t = CTkLabel(self.root, text='INSTRUCTIONS', font=('Cooper Black', 60))
        label_t.place(relx=0.5, rely=0.1, anchor='center')

        label_i1 = CTkLabel(self.root, text='You are required to click the color of the word, not what the word shows',
                            wraplength=600, font=('Cooper Black', 30, 'bold'), text_color="#e83c67")
        label_i1.place(relx=0.5, rely=0.25, anchor='center')

        label_i2 = CTkLabel(self.root, text="For example, for the word", font=('Cooper Black', 30))
        label_i2.place(relx=0.5, rely=0.35, anchor='center')

        label_i3 = CTkLabel(self.root, text="RED", font=('Cooper Black', 60, "bold"), text_color="blue")
        label_i3.place(relx=0.5, rely=0.45, anchor='center')

        label_i4 = CTkLabel(self.root, text="you should say Blue.", font=('Cooper Black', 30))
        label_i4.place(relx=0.5, rely=0.55, anchor='center')

        label_i5 = CTkLabel(self.root, text="As soon as the words appear on your screen, click on the corresponding colour",
                            wraplength=600, font=('Cooper Black', 30))
        label_i5.place(relx=0.5, rely=0.7, anchor='center')

        b1 = CTkButton(self.root, text="Back", font=('Cooper Black', 30), fg_color=('#ddddff', '#383842'), text_color = "black", hover_color = "red", command=self.back)
        b1.place(relx = 0.5, rely = 0.85, anchor ='center')

        exitButton = CTkButton(self.root, text= "",width=1, height=1, fg_color=('#ddddff', '#383842'), hover_color = "red", command= self.clickExitButton)
        exitButton.configure(self.root, image=self.img)
        exitButton.place(relx = 1, x =-1, y = 1, anchor = NE)


    
    def clickExitButton(self):
            exit()

    def back(self):
        self.root.withdraw()
        try:
             go_back = getattr(w.import_module('Splash_Screen'), 'Splash_Screen').open_window(self)
             return go_back()
        except AttributeError:
             return "Function not found in the module."


