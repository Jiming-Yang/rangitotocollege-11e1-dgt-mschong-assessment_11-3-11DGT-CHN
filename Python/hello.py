import tkinter as tk
import random
from tkinter import *
r = tk.Tk()
r.title('Home Page')
button = tk.Button(r, text='Stop', width=25, command=r.destroy)
button.pack()
r.mainloop()

#gambling game
score = 0.0


gamble = float(input("How much would you like to gamble?"))
thing = random.choice(["1", "2"])
if thing == "1":
    score = score + gamble
    print(f"WINNER! you won! you have {score} dollars")
if thing == "2":
    score = score - gamble
    print(f"LOSER! you lost {score} dollars")
    
#game 2: maths quiz
stop = "stop"
while True:
    try:
        no1 = random.randint(1, 20)
        no2 = random.randint(1, 20)
        useranswer = (input(f"What is {no1} + {no2}? "))
        actual = (int(no1) + int(no2))
        if useranswer == "stop":
            break
        int(useranswer)
        if int(useranswer) == int(actual):
            print("Correct!")
            score = score + 1
        else: 
            print("Incorrect! try again")
    except ValueError:
        print("Please enter a number or 'stop' to end the game.")
print(f"you score is {score}")
#game 3
