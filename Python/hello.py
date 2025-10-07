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
snake_body = []
velocity_x = 0
velocity_y = 0 
die = False
money = 0

def change_direcion(e): #e for event
    #print(e.keysym)
    global velocity_x, velocity_y, die
    if (die):
        return

    if(e.keysym == "Up" and velocity_y != 1): #it makes sure that you cannot go up then down straight away or right and left etc.
        velocity_x = 0
        velocity_y = -1
    elif(e.keysym == "Down" and velocity_y != -1):
        velocity_x = 0
        velocity_y = 1 
    elif(e.keysym == "Left" and velocity_x != 1):
        velocity_x = -1
        velocity_y = 0
    elif(e.keysym == "Right" and velocity_x != -1):
        velocity_x = 1
        velocity_y = 0
    elif(e.keysym == "w" and velocity_y != 1):
        velocity_x = 0
        velocity_y = -1
    elif(e.keysym == "s" and velocity_y != -1):
        velocity_x = 0
        velocity_y = 1
    elif(e.keysym == "a" and velocity_x != 1):
        velocity_x = -1
        velocity_y = 0
    elif(e.keysym == "d" and velocity_x != -1):
        velocity_x = 1
        velocity_y = 0

def move():
    global snake, coin, snake_body, die
    if (die):
        return
    if (snake.x < 0 or snake.x >= window_wide or snake.y < 0 or snake.y >= window_tall):
        die = True
        return
    for i in snake_body:
        if (snake.x == i.x and snake.y == i.y):
            die = True
            return  
    #checking for collison with coin
    if (snake.x == coin.x and snake.y == coin.y):
        snake_body.append(Tile(coin.x, coin.y))
        coin.x = random.randint(0, colum - 1) * sqrsize
        coin.y = random.randint(0, row - 1) * sqrsize
        
        #updating snake body making it follow the train of squares
    for x in range(len(snake_body)-1, -1, -1):
        tile = snake_body[x]
        if (x == 0):
            tile.x = snake.x
            tile.y = snake.y
        else:
            prev_tile = snake_body[x - 1]
            tile.x = prev_tile.x
            tile.y = prev_tile.y
    

    snake.x +=  velocity_x * sqrsize #if i dont multiply by sqrsize it will move 1 pixel instead of a square
    snake.y +=  velocity_y * sqrsize
def draw():
    global snake, coin, snake_body, die


    move()
    canvas.delete("all")
    #drawing the coin
    canvas.create_oval(coin.x, coin.y, coin.x + sqrsize, coin.y + sqrsize, fill = "yellow")
    #actually drawing the snake (character):
    canvas.create_rectangle(snake.x, snake.y, snake.x +sqrsize, snake.y + sqrsize, fill = "salmon")
    #adding to the body evertyime a colision happens
    for i in snake_body:
        canvas.create_rectangle(i.x, i.y, i.x + sqrsize, i.y + sqrsize, fill = "salmon")

    if (die):
        canvas.create_text(window_wide/2, window_tall/2, text = "You Died!", fill = "white", font = ("comic sans", 50))
    else:
        canvas.create_text(30, 10, text = f"Score: {len(snake_body)}", fill = "white", font = ("comic sans", 20))
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