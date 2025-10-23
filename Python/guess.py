from tkinter import *
import random
root = Tk()
root.title("guessing")
root.geometry("250x150")

randnum = "none"


title_label = Label(root,text="guess number", font=("Arial 12"), pady = 8, justify="center") #gui stuff
but1 = Button(root, text="00", font=("Arial 12"), width=6, pady=15, bg="Green")
but2 = Button(root, text="00", font=("Arial 12"), width=6, pady=15, bg="Blue")
but3 = Button(root, text="00", font=("Arial 12"), width=6, pady=15, bg="Red")
butlist = [but1, but2, but3]
ans_labl = Label(root, text="Answer:", font=("Arial 12"), pady=9, fg="purple", justify="center")
title_label.grid(row=0, column=0, columnspan=3)
but1.grid(row=1, column=0)
but2.grid(row=1, column=1)
but3.grid(row=1, column=2)

root.mainloop()