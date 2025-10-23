from tkinter import *
import random
root = Tk()
root.title("guessing")
root.geometry("250x250")
root.resizable(False, False)
randnum = "none"
score = 0

#the functons
def start():
    global randnum
    for button in butlist:
        button.config(text=str(random.randint(0,100)))
    randbut = random.choice(butlist)
    randnum = randbut.cget("text") #https://www.tutorialspoint.com/get-the-text-of-a-button-widget-in-tkinter
    print("the numeber is: ", randnum) 
def click(event):
    global score
    btn = event.widget
    butttext = btn.cget("text")
    if randnum == butttext:
        score +=1
        ahh.config(text= f"score = " + str(score))
        ans_labl.config(text="It was " + randnum)
        start()
    

title_label = Label(root, text="guess number", font=("Arial, 12"), pady = 8, justify="center") #gui stuff
ahh = Label(root, text="score = 0", font=("Arial 12"), pady=5)
but1 = Button(root, text="00", font=("Arial 12"), width=6, pady=15, bg="Green")
but2 = Button(root, text="00", font=("Arial 12"), width=6, pady=15, bg="Blue")
but3 = Button(root, text="00", font=("Arial 12"), width=6, pady=15, bg="Red")
butlist = [but1, but2, but3]
ans_labl = Label(root, text="Answer:", font=("Arial 15"), pady=9, fg="purple", justify="center")
title_label.grid(row=0, column=0, columnspan=3)
but1.grid(row=1, column=0)
but2.grid(row=1, column=1)
but3.grid(row=1, column=2)
ans_labl.grid(row=2, column=0, columnspan=3)
ahh.grid(row=3, column=0, columnspan=3)

but1.bind("<Button-1>", click)
but2.bind("<Button-1>", click)
but3.bind("<Button-1>", click)
start()
root.mainloop()

