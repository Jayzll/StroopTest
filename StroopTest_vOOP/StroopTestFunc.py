from tkinter import *
from customtkinter import *
import random
import time
import sqlite3 as s
from scoreboard import Scoreboard

#Define a class
class StroopStartScreen:
    #Create an instance in a class with 3 parameters self, root and username
    def __init__(self, root, username):
        # Store the username as an attribute of the instance
        self.username = username 
        print("Stroop Start Screen Username = ", self.username)
        self.stroop_start_root = root
        self.stroop_start_root.title("Are you ready?")
        self.stroop_start_root.configure(fg_color=('#ddddff', '#383842'))
        self.stroop_start_root.geometry("{0}x{1}+0+0".format(self.stroop_start_root.winfo_screenwidth(), self.stroop_start_root.winfo_screenheight()))
        set_appearance_mode("system") 
        self.stroop_start_root.resizable(False, False)
        #Objects that can only be accessed in this class
        t1 = CTkLabel(self.stroop_start_root, text='"Click on the color of the word, not the word itself as quickly as possible in a series of colored words.', 
                      font=('Cooper Black', 40), wraplength=700, text_color="black", corner_radius= 1, fg_color="#ddddff")
        t1.place(relx = 0.5, rely=0.4, anchor = 'center')
        b1 = CTkButton(self.stroop_start_root, text='ARE YOU READY!', font=('Cooper Black', 40), text_color='black', fg_color="white", 
                       hover_color="red", command=self.open_strooptestfunc)
        b1.place(relx = 0.5, rely = 0.7, anchor ='center')

    def open_strooptestfunc(self):
        self.stroop_start_root.withdraw()
        stroop_root = CTkToplevel()
        app = StroopTestFunc(stroop_root, self.username)
        stroop_root.mainloop()
        

class StroopTestFunc:
    def __init__(self, root, username):
        self.count = 0
        self.correct_answers = 0
        self.choices = []
        self.username = username


        self.root = root
        self.root.title("Stroop Test")
        self.root.configure(fg_color=('#ddddff', '#383842'))
        self.root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
        set_appearance_mode("system") 

        self.set_database()

        self.Stroop_Test_Game_Display()

        self.widgets()


        self.store_username()

    def store_username(self):
        from Create_Page import Create_Page
        print("D1")
        cpg = Create_Page(self.root, self.store_username)
        print("D2")
        print("Create Store Username = ", self.username)

    def get_username(self):
        from Login_Page import Login_Page
        print("L1")
        lpg = Login_Page(self.root, self.get_username)
        print("L2")
        print("Login Get Username = ", self.username)

    def set_database(self):
        #Create connection to db
        db = s.connect(r"login.db")
        #Create cursor to interact with db
        cursor = db.cursor()
        #Create scoreboard table in the db
        table = '''CREATE TABLE IF NOT EXISTS scoreboard(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            recent_timetaken INT NOT NULL,
            lowest_timetaken INT NOT NULL,
            recent_score INT NOT NULL,
            highest_score INT NOT NULL
            )
            '''
        #Execute the table 
        cursor.execute(table)
        #Insert values into the coloumns 
        sql = """INSERT INTO scoreboard (username, recent_timetaken, lowest_timetaken, recent_score, highest_score) VALUES (?, ?, ?, ?, ?)"""
        #Exception Handling - Try inserting placeholder values
        try:
            cursor.execute(sql, (0, 0, 99, 0, 0,))
        except s.IntegrityError:
            #If data does not have a uniqueness constraint then print the statement below
            print("data is stored")
        #Commit to changes in db
        db.commit()

        self.time_algorithm = False
    #Update results 
    def store_result(self):
        #Connect to db
        self.db = s.connect(r"login.db")
        try:
            #Attempt to set it as empty string
            self.username == ""
            print("Creation success. go through")
        except:
            self.username
        cursor = self.db.cursor()
        print("This is the username ", self.username)
        
        #Select the user ID from the users table based on the current username
        sql4 = "SELECT id FROM users WHERE username = ?"
        cursor.execute(sql4, (self.username,))
        userid = cursor.fetchone()
        print("This is UserID", userid[0])
        print("This is the username ", self.username)

        #Update the username from the users table based on the current username
        username_fetch = """UPDATE scoreboard SET username = ? WHERE id = ?"""
        cursor.execute(username_fetch, (self.username, userid[0],))
        username_id = cursor.fetchone()
        print("Username = ", username_id)

        #Fetch the highest score from the scoreboard table based on the user ID
        highest_score_fetch = '''SELECT highest_score FROM scoreboard WHERE id = ?'''
        cursor.execute(highest_score_fetch, (userid[0],))
        highest_score = cursor.fetchone()
        print("High Score", highest_score)
        print("Result", self.correct_answers,"/10")
        #Update the 'scoreboard' table with the recent and highest scores
        sql = "UPDATE scoreboard SET recent_score = ?, highest_score = ? WHERE id = ?"
        cursor.execute(sql, (self.correct_answers, self.correct_answers, userid[0],))
        #Check if there is a highest score and update accordingly
        if highest_score is not None:
            if self.correct_answers >= highest_score[0]:
                self.time_algorithm = True
                cursor.execute(sql, (self.correct_answers, self.correct_answers, userid[0],))
                print("New highest score recorded")
            else: 
                cursor.execute(sql, (self.correct_answers, highest_score[0], userid[0],))
        else:
            print("No High score")
        self.db.commit()
 
        print(userid)

        cursor.close()
        self.db.close()


    def store_time(self):
        db = s.connect(r"login.db")

        cursor = db.cursor()
        sql2 = "SELECT id FROM users WHERE username = ?"
        cursor.execute(sql2, (self.username,))
        userid_time = cursor.fetchone()
        print("This is UserID", userid_time)
        
        lowest_time_fetch = '''SELECT lowest_timetaken FROM scoreboard WHERE id = ?'''
        cursor.execute(lowest_time_fetch, (userid_time[0],))
        lowest_time = cursor.fetchone()
        print("Lowest Time", lowest_time)
        print("Time Taken", self.total_time) 

        sql = "UPDATE scoreboard SET recent_timetaken = ?, lowest_timetaken = ? WHERE id = ?"
        cursor.execute(sql, (self.total_time, self.total_time, userid_time[0],))
        
        if lowest_time is not None:
            if self.total_time < lowest_time[0] and self.time_algorithm:
                cursor.execute(sql, (self.total_time, self.total_time, userid_time[0],))
                print("New shortest time recorded")
            else:
                cursor.execute(sql, (self.total_time, lowest_time[0], userid_time[0],))
        else:
            print("No Lowest Time")
        db.commit() 
        cursor.close()
        db.close()
    #Stroop Test Algorithm
    def Stroop_Test(self):
        current_word = random.choice(self.words)
        self.label.config(text=current_word[0], fg=random.choice(self.colors))
        for choice in self.choices:
            choice.configure(text_color='black')
        self.count += 1
        self.count_label.configure(text="Question: " + str(self.count) + "/10")
        if self.count == 10:
            self.end_time = time.time()
            self.total_time = round(self.end_time - self.start_time, 2)
            self.result_label.configure(text="You scored " + str(self.correct_answers) + " out of 10.")
            self.store_result()
            self.time_label.configure(text="Time taken: " + str(self.total_time) + "seconds.")
            self.store_time()
            self.next_button.configure(state='disabled')
            self.reset_button.configure(state='normal')
            for choice in self.choices:
                choice.unbind('<Button-1>')

    def check_answer(self, event):
        self.event = event
        if self.event.widget.cget("text") == self.label.cget("fg"):
            self.correct_answers += 1
            print("This is Correct", self.correct_answers)
            self.event.widget.configure(fg='green')
        else:
            self.event.widget.configure(fg='red')
            self.result_label.configure(text="Incorrect! Correct answer was " + self.label.cget("fg"))
        self.Stroop_Test()

    def reset(self):
        self.root.destroy()
        stroop_root = CTkToplevel()
        app = StroopTestFunc(stroop_root, self.username)
        stroop_root.mainloop()

    def Stroop_Test_Game_Display(self):

            self.words = [("red", "red"), ("blue", "blue"), ("green", "green"), ("yellow", "yellow")]
            self.colors = ["red", "blue", "green", "yellow"]
            self.current_word = random.choice(self.words)

            self.label = Label(self.root, text=self.current_word[0], font=('Comic Sans MS', 60), fg=random.choice(self.colors), bg="#ddddff",
                  width=20, height=2)
            self.label.pack()

            for color in self.colors:
                choice = CTkButton(self.root, text=color, font=('Comic Sans MS', 40), text_color=("black", "white"), fg_color=('#ddddff', '#383842'), hover_color="#9b9bb0")
                self.start_time = time.time()
                choice.pack()
                choice.bind('<Button-1>', self.check_answer)
                self.choices.append(choice)

    def widgets(self):
    
        self.next_button = CTkButton(self.root, text="", fg_color=('#ddddff', '#383842'), hover_color=('#ddddff', '#383842'), command=self.Stroop_Test)
        self.next_button.pack()

        self.count_label = CTkLabel(self.root, text="", font=('Comic Sans MS', 24), fg_color=('#ddddff', '#383842'))
        self.count_label.place(relx = 0.9, rely = 0.2, anchor ='center')

        self.timer_label = CTkLabel(self.root, text="", font=('Comic Sans MS', 18), fg_color=('#ddddff', '#383842'))
        self.timer_label.place(relx = 0.9, rely = 0.3, anchor ='center')

        self.reset_button = CTkButton(self.root, text="Reset",  font=('Cooper Black', 60), text_color=("black", "white"), fg_color=('#ddddff', '#383842'), command=self.reset)
        self.reset_button.place(relx = 0.3, rely = 0.8, anchor ='center')

        self.result_label = CTkLabel(self.root, text="", font=('Comic Sans MS', 18), fg_color=('#ddddff', '#383842'))
        self.result_label.place(relx = 0.5, rely = 0.65, anchor ='center')

        self.time_label = CTkLabel(self.root, text="", font=('Comic Sans MS', 18), fg_color=('#ddddff', '#383842'))
        self.time_label.place(relx = 0.5, rely = 0.7, anchor ='center')

        score_button = CTkButton(self.root, text="Scoreboard", font=('Cooper Black', 60), text_color=("black", "white"), fg_color=('#ddddff', '#383842'), command=self.open_leaderboard)
        score_button.place(relx = 0.7, rely = 0.8, anchor ='center')

    def clickExitButton(self):
            exit()

    def open_leaderboard(self):
        self.root.withdraw()
        Leaderboard = CTkToplevel()
        app = Scoreboard(Leaderboard)
        Leaderboard.mainloop()
         
    


