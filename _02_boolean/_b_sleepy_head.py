"""
Use boolean variables to control program logic between two different code
paths.
"""
import turtle
from tkinter import messagebox, Tk

if __name__ == '__main__':
    # TODO)
    #  1. Use a boolean variable to indicate if it is the weekend.
    #     Display a different message to the user depending on whether it is
    #     the weekend or not.
    window = Tk()
    window.withdraw()
    weekend = False
    if weekend:
        messagebox.showinfo(None, "Relax! Watch TV or read a book :)")
    else:
        messagebox.showinfo(None, "Do your homework and/or go to your job!")
    #  2. Use a boolean variable to indicate if a student passed an exam.
    #     Display a different message to the user depending on whether they
    #     passed or not.
    passed = True
    if passed:
        messagebox.showinfo(None, "Good job! You get ice cream!")
    else:
        messagebox.showinfo(None, "You don't get ice cream.")
    #  3. Use a boolean variable to indicate if a game is over. When the game
    #     is over, tell the user.
    gameOver = True
    if gameOver:
        messagebox.showinfo(None, "GAME OVER")
    #  4. Use two boolean variables, one to indicate if a shape should be red,
    #     the other to indicate if the shape is to be square. When both
    #     variables are true, use a turtle to draw a red square.
    shelly = turtle.Turtle()
    red = True
    square = True
    if red and square:
        shelly.pencolor("Red")
        for i in range(4):
            shelly.forward(100)
            shelly.right(90)

