import random
import tkinter as tk

lowChars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
uppChars = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
            "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
specChars = ["!", "'", ",", ".", "£", "$", "€", "%", "^",
             "&", "*", "?", "/", ":", ";", "-", "+", "=", "~"]
nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

# Settings for the GUI
window = tk.Tk()
window.title("Password Generator")
window.geometry("300x200")

# Allows user to input a length
length = tk.Label(text="Enter Password Length: ")
length.grid(column=0, row=4)
lengthEntry = tk.Entry()
lengthEntry.grid(column=1, row=4)

# Check boxes for the different options
Lowercase = tk.IntVar()
Uppercase = tk.IntVar()
Special = tk.IntVar()
Numbers = tk.IntVar()

C1 = tk.Checkbutton(text="Lowercase", variable=Lowercase)
C1.grid(column=0, row=0, sticky="w")
C2 = tk.Checkbutton(text="Uppercase", variable=Uppercase)
C2.grid(column=0, row=1, sticky="w")
C3 = tk.Checkbutton(text="Special", variable=Special)
C3.grid(column=0, row=2, sticky="w")
C4 = tk.Checkbutton(text="Numbers", variable=Numbers)
C4.grid(column=0, row=3, sticky="w")

final = []


def getInput():
    i = 0

    password = ""
    length = lengthEntry.get()
    intLength = int(length)

    if (Lowercase.get() == True):  # Uses the check box options and adds the arrays to final
        final.extend(lowChars)
    if (Uppercase.get() == True):
        final.extend(uppChars)
    if (Special.get() == True):
        final.extend(specChars)
    if (Numbers.get() == True):
        final.extend(nums)

    while (i < intLength):  # Generates the password word from final[]
        password = password + random.choice(final)
        i += 1
    textArea = tk.Text(master=window, height=1,
                       width=intLength)
    textArea.grid(column=0, row=5)
    textArea.insert(tk.END, password)  # Where password is displayed


# Button with takes the input from lengthEntry and runs it in getInput()
button = tk.Button(window, text="Generate", command=getInput, bg="lightblue")
button.grid(column=1, row=5)
window.mainloop()
