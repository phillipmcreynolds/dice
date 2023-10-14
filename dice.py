from tkinter import *
import random

def roll_die(sides):
    roll = random.randint(1, sides)
    rollLabel.set(str(roll))

def createButton(n, x, y):
    Button(root, font=('futura', 15, 'bold'),
           padx=16, pady=16, text = 'D' + str(n),
           command = lambda: roll_die(n),
           height = 2, width=9).grid(row = x, column = y, sticky=E)

root = Tk()  # create parent window
root.title('Dice App')
rollLabel = StringVar()
Label(root, font=('futura', 25, 'bold'), textvariable = rollLabel,
      justify=LEFT, height=2, width=7).grid(columnspan=4, ipadx=120)
buttons = [2, 4, 6, 8, 10, 12, 20, 100]
btn_counter = 0
for i in range(2, 4):
    for j in range(0, 4):
        createButton(buttons[btn_counter], i, j)
        btn_counter += 1

root.mainloop()