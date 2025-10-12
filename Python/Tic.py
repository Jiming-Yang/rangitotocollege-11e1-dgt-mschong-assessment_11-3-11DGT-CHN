from tkinter import *
import random

def next_turn():
    pass
def check_winner():
    pass
def empty_spaces():
    pass
def new_game():
    pass

window = Tk()
window.title("Tic Tac Toe")
players = ["x", "o"]
player = random.choice(players) #randomising who go first
buttons = [[0,0,0],  #i put them in this format so i can visualise what it kinda look like
           [0,0,0],
           [0,0,0]]
label = Label(text= player + " turn", font= ("Arial", 40)) #to see who go first
label.pack(side="top") 

again = Button(text="try again", font =("Comic Sans MC", 20), command=new_game) #this will call upon the function new_game
again.pack(side="top")

frame = Frame(window)
frame.pack()

for i in range(3): #3 because there are 3 rows the i in the loop represents row
    for c in range(3):#3 because 3 collumns the c represents column
        buttons[i][c] = Button(frame, text="", font=("Arial", 40), width=5, height=2, command= lambda row=i, column=c: next_turn(i.c)) #note to self, lambda is just a short function that too lazy to define
        buttons[i][c].grid(row=i, column=c)

window.mainloop()
