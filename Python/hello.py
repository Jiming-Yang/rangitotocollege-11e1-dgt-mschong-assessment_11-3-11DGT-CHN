import tkinter
import random

row = 25
colum = 25
sqrsize = 25
#laying out the window
window_wide = sqrsize * colum #(it is 625)
window_tall = sqrsize * row #(its 625)

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#window settings
window = tkinter.Tk()
window.title("snake")
window.resizable(False, False)
#making the canvas (gamemap)
canvas = tkinter.Canvas(window, bg = "black", height = window_tall, width = window_wide, borderwidth = 0, highlightthickness = 0)
canvas.pack()
window.update()
#centering window so it looks better
window_wide = window.winfo_width()
window_tall = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

#the game
snake = Tile(5*sqrsize, 5*sqrsize) #one tile for the characters head
coin = Tile(10*sqrsize, 10*sqrsize) #one tile for the coin
velocity_x = 0
velocity_y = 0 
def change_direcion(e): #e for event
    #print(e.keysym)
    global velocity_x, velocity_y

    if(e.keysym == "Up"):
        velocity_x = 0
        velocity_y = -1
def draw():
    global snake
    #actually drawing the snake (character):
    canvas.create_rectangle(snake.x, snake.y, snake.x +sqrsize, snake.y + sqrsize, fill = "salmon")
#drawing the coin
    canvas.create_oval(coin.x, coin.y, coin.x + sqrsize, coin.y + sqrsize, fill = "yellow")

    window.after(100, draw) #draws again every 0.1 sec (10 frames per sec)
draw()


window_x = float((screen_width/2) - (window_wide/2))
window_y = float((screen_height/2) - (window_tall/2))

window.geometry(f"{window_wide}x{window_tall}+{int(window_x)}+{int(window_y)}")

window.bind("<KeyRelease>", change_direcion)
window.mainloop()



"""from tkinter import *
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
# please note that i am not done this is only the python
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
#game 3 i havent decided yet
while True:
    guess = str(input("Guess a number between 1 and 5 (or type 'stop' to end): "))
    number = random.randint(1, 5)
    if guess == "stop":
        print("Game ended.")
        break
    if int(guess) == int(number):
        print("You guessed right!")
        score = score + 1
    else:
        print(f"Wrong! the number was {number}") 

print(f"{score} points")
print("the end")"""