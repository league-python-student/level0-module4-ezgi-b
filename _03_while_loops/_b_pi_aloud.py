"""
Use a while loop to recite the digits of pi
"""
from tkinter import messagebox, simpledialog, Tk
import math


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    # TODO) Place the first 20 digits of pi into a String variable.
    #  3.1415926535897932384
    pi_str = "31415926535897932384"

    # TODO) Print out the first 3 digits of pi. For example,
    #  pi_str[0]   # first digit
    #  pi_str[1]   # second digit

    # TODO) Use a while loop to keep asking for the next digit of pi

        # TODO) If they are correct, print "correct".
        #  If they are not, print "incorrect" and break out of the while loop
    index = 0
    while True:
        input = simpledialog.askstring(None, "What is digit #" + str(index + 1) + " of pi?")

        if pi_str[index] == input:
            print("correct")
            index += 1
        else:
            print("incorrect")
            break


    # TODO) Print out how many digits of pi the user was able to recite
    #  in a row
    print("You were able to recite " + str(index) + " digits of pi in a row")
