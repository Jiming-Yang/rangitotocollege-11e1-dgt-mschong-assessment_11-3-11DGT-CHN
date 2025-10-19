from tkinter import *
import random

def next_turn(row, column):
    global player
    if buttons[row][column]["text"] == "" and check_winner() is False:
        if player == players[0]: #if it is player 1's turn

            buttons[row][column]["text"] = player
            
            if check_winner() is False: #so if there is no winner
                player = players[1] #i am swapping the player's turn
                label.config(text= (players[1] + " turn"))
            elif check_winner() is True:
                label.config(text= (players[0] + " wins")) #if there is a winner
            elif check_winner() == "Tie":
                label.config(text= "tie")
        else: # if it is not player ones turn (player 2 turn)
            buttons[row][column]["text"] = player
            
            if check_winner() is False: #so if there is no winner
                player = players[0] #i am swapping the player's turn
                label.config(text= (players[0] + " turn"))
            elif check_winner() is True:
                label.config(text= (players[1] + " wins")) #if there is a winner
            elif check_winner() == "Tie":
                label.config(text= "tie")

        

def check_winner():
#im basically checking if all the cooordnates are filled or not
    #horizontal win condition
    for row in range(3): # if there is 3 in row
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            buttons[row][0].config(bg="blue")  #this is to make it visually better and more clear that somone won
            buttons[row][1].config(bg="blue")
            buttons[row][2].config(bg="blue")
            return True
 #vertical
    for column in range(3):
        if buttons[0][column]["text"] == buttons[1][column]["text"] == buttons[2][column]["text"] != "":
            buttons[0][column].config(bg="blue")
            buttons[1][column].config(bg="blue")
            buttons[2][column].config(bg="blue")
            return True
    
  #diagonal both ways dont need loop bc only 2 way digaanol can go
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        buttons[0][0].config(bg="blue")
        buttons[1][1].config(bg="blue")
        buttons[2][2].config(bg="blue")
        return True
    elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        buttons[0][2].config(bg="blue")
        buttons[1][1].config(bg="blue")
        buttons[2][0].config(bg="blue")
        return True
    elif empty_spaces() is False: #if there is no empty spaces and no winner then it is a tie
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="purple") #to make it clear its tie and also look cool
        return "Tie"
    else:
        return False
def empty_spaces():
    spaces = 9 #when this is 0 the game end and tie
    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"] != "":
                spaces -=1 #note to self -= is just spaces = spaces -1

    #check if there no spaces left
    if spaces ==0:
        return False
    else:
        return True
    
def new_game():
    global player
    player = random.choice(players) #random new player
    label.config(text= player + " turn:")
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="white") #reset buttons and colour

window = Tk()
window.title("Tic Tac Toe")
players = ["x", "o"]
player = random.choice(players) #randomising who go first
buttons = [[0,0,0],  #i put them in this format so i can visualise what it kinda look like i basically use this as coordinates
           [0,0,0],
           [0,0,0]]
label = Label(text= player + " turn", font= ("Arial", 40)) #to see who go first
label.pack(side="top") 

again = Button(text="try again", font =("Comic Sans MC", 20), command=new_game) #this will call upon the function new_game
again.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3): #3 because there are 3 rows the i in the loop represents row
    for column in range(3):#3 because 3 collumns the c represents column
        buttons[row][column] = Button(frame, text="", font=("Arial", 40), width=5, height=2, command= lambda row=row, column=column: next_turn(row,column)) #note to self, lambda is just a short function that too lazy to define
        buttons[row][column].grid(row=row, column=column)

window.mainloop()
