import sqlite3
my_conn = sqlite3.connect('login.db')

import tkinter  as tk 
from tkinter import * 
from customtkinter import *
import importlib as w

class Scoreboard:
    def __init__(self, root):
        self.root = root
        
        self.display_score()

    def display_score(self):
        self.root.title("Leaderboard")
        self.root.configure(fg_color=('#ddddff', '#383842'))
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        set_appearance_mode("system")  
        leaderboard_label = CTkLabel(self.root, text="Leaderboard", font=('Cooper Black', 60), fg_color=('#ddddff', '#383842'))
        leaderboard_label.grid(row=0, column=0, columnspan=30)


        self.back_button = CTkButton(self.root, text="Back", font=('Cooper Black', 23), text_color=('#ddddff', '#383842'), fg_color = '#461959', command=self.back)
        self.back_button.place(relx = 0.5, rely = 0.8, anchor ='center')
        #Headings
        headings = ["Place", "Username", "Recent Time", "Lowest Time", "Recent Score", "Highest Score"]  # Add the desired headings
        
        for j, heading in enumerate(headings):
            title = CTkEntry(self.root, width=300, text_color=('#571c6b','#d147ff'), font=('Cooper Black', 30), fg_color=('#ddddff', '#383842'), corner_radius=(1)) 
            title.grid(row=1, column=j)  # Place headings at row 1
            title.insert(END, heading) 
            title.configure(state= "disabled")

        total_columns = len(headings)
        for j in range(total_columns):
            self.root.grid_columnconfigure(j, weight=1) 
        #Values from database
        r_set = my_conn.execute('''SELECT '', username, recent_timetaken, lowest_timetaken, recent_score, highest_score from scoreboard ORDER BY highest_score DESC, lowest_timetaken ASC LIMIT 0,10''')
        i=5 
        position = 1 # row value inside the loop 

        for score in r_set: 
            for j in range(len(score)):
                if j == 0:
                    score_row = CTkEntry(self.root, width=300, text_color=('black', 'white'), font=('Cooper Black', 30), fg_color=('#ddddff', '#383842'), corner_radius=(1))
                    score_row.grid(row=i, column=j)
                    # Create rows
                    score_row.insert(END, position)
                else:
                    score_row = CTkEntry(self.root, width=300, text_color=('black','white'), font=('Cooper Black', 30), fg_color=('#ddddff', '#383842'), corner_radius=(1)) 
                    score_row.grid(row=i, column=j)
                    # Create columns
                    score_row.insert(END, score[j])
                    score_row.configure(state= "disabled")
                #Make the placement color 
                if i == 5:
                    #1st Place = Gold
                    score_row.configure(fg_color=('#c2ab5f'))
                if i == 6:
                    #2nd Place = Silver
                    score_row.configure(fg_color=('silver'))
                if i == 7:
                    #3rd Place = Bronze
                    score_row.configure(fg_color=('#b08c57'))

            i=i+1
            position += 1
        self.root.mainloop()
    
        for i in range(1,10):
            r_set


    def back(self):
        self.root.withdraw()
        #quit()
        try:
             go_back = getattr(w.import_module('Splash_Screen'), 'Splash_Screen').open_window(self)
        except AttributeError:
             return "Function not found in the module."
