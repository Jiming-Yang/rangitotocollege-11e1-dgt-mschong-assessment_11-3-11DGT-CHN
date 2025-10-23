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
poop = []

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

        #TIME FOR POOP
        if len(snake_body)>1:
            poop_location = snake_body[-2]
            poop.append(Tile(poop_location.x, poop_location.y))
        coin.x = random.randint(0, colum - 1) * sqrsize
        coin.y = random.randint(0, row - 1) * sqrsize
    for p in poop:
        if snake.x == p.x and snake.y == p.y:
            die = True
            return


        
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
    for x in poop:
        canvas.create_rectangle(x.x, x.y, x.x + sqrsize, x.y + sqrsize, fill = "brown")
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
