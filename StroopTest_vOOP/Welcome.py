from tkinter import *
from customtkinter import *
from PIL import ImageTk, Image
from MainTitle import Main_Title
from Instruction_Page import instruction
from scoreboard import Scoreboard
from time import sleep 

class Welcome:
    def __init__(self, root):
        frame = CTkFrame(root, width = 400, height = 300, fg_color=('#ddddff', '#383842'))
        frame.place(relx=0.5, rely=0.6, anchor="center")
        #These are variables initiated for the animation of the word Stroop Test
        self.count = 0
        self.text = ''
        self.title = 'STROOP TEST'
        #Window Configuration
        self.root = root
        self.root.title('Stroop Test')
        self.root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
        self.root.configure(fg_color=('#ddddff', '#383842')) 
        set_appearance_mode("system")  

        self.img3 = CTkImage(Image.open('image/Cross.png'), size=(30,30))  

        self.label_t = CTkLabel(self.root, text=self.title, font=('Cooper Black', 100))
        self.label_t.place(relx=0.5, rely=0.3, anchor="center")       
    
        #Widgets

        # Buttons placed inside the frame with explicit positions
        self.t1_button = CTkButton(frame, text="PLAY", font=('Hogfish DEMO', 40), text_color=("black", "white"), fg_color=('#ddddff', '#383842'), hover_color="red", command=self.go_main)
        self.t1_button.place(relx=0.5, rely=0.2, anchor="center")  # Adjusted position for the PLAY button

        self.i1_button = CTkButton(frame, text="Instructions", font=('Hogfish DEMO', 40), text_color=("black", "white"), fg_color=('#ddddff', '#383842'), hover_color="blue", command=self.instruction)
        self.i1_button.place(relx=0.5, rely=0.5, anchor="center")  # Adjusted position for the Instructions button

        self.l1_button = CTkButton(frame, text="Leaderboard", font=('Hogfish DEMO', 40), text_color=("black", "white"), fg_color=('#ddddff', '#383842'), hover_color="yellow", command=self.open_leaderboard)
        self.l1_button.place(relx=0.5, rely=0.8, anchor="center")

        self.exitButton = CTkButton(self.root, text= "",width=1, height=1, fg_color=('#ddddff', '#383842'), hover_color = "red", command= self.clickExitButton)
        self.exitButton.configure(self.root, image=self.img3)
        self.exitButton.place(relx = 1, x =-1, y = 1, anchor = NE)

        self.animation()


    def clickExitButton(self):
            exit()
    
    def go_main(self):

        self.root.withdraw()
        main_page = CTkToplevel()
        app = Main_Title(main_page)
        text = ""
        main_page.mainloop()

    def instruction(self):

        self.root.withdraw()
        instruction_page = CTkToplevel()
        app = instruction(instruction_page)
        text = ""
        instruction_page.mainloop()

    def open_leaderboard(self):
        self.root.withdraw()
        Leaderboard = CTkToplevel()
        app = Scoreboard(Leaderboard)
        Leaderboard.mainloop()

    #Function for animation
    def animation(self):
        #Loop if there are more characters to display
        if self.count < len(self.title):
            #Add the next character to the displayed text
            self.text = self.text + self.title[self.count]
            #Update the text of the label with new text
            self.label_t.configure(text=self.text)
            print(self.text)
            #Move to the next character by incrementing counter
            self.count += 1
        else: 
            #Reset the counter 
            self.count = -1
            #Update the label's text with the final text
            self.widget.label_t.configure(text=self.text)
            #Stop the recursion
            self.widget.label_t.after_cancel(self.slider)
        #Time each iteration of the animation after 50 milliseconds
        self.slider = self.root.after(50, self.animation)
