import tkinter as tk
from tkinter import messagebox
import random

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play(choice):
    computer_choice = get_computer_choice()
    result = determine_winner(choice, computer_choice)
    messagebox.showinfo("Result", f"Computer chose: {computer_choice}\n{result}")


root = tk.Tk()
root.title("Rock, Paper, Scissors")


button_rock = tk.Button(root, text="Rock", width=20, command=lambda: play("Rock"))
button_rock.pack(pady=10)

button_paper = tk.Button(root, text="Paper", width=20, command=lambda: play("Paper"))
button_paper.pack(pady=10)

button_scissors = tk.Button(root, text="Scissors", width=20, command=lambda: play("Scissors"))
button_scissors.pack(pady=10)


root.mainloop()
