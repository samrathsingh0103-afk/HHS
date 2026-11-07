
import tkinter as tk
import random

# Main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("500x550")
root.config(bg="#172554")
root.resizable(False, False)

# Scores
user_score = 0
computer_score = 0

# Game function
def play(user_choice):
    global user_score, computer_score

    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    user_label.config(text=f"You chose: {user_choice}")
    computer_label.config(text=f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        result_label.config(text="IT'S A DRAW!", fg="yellow")

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        user_score += 1
        result_label.config(text="YOU WIN! 🎉", fg="#4ade80")

    else:
        computer_score += 1
        result_label.config(text="COMPUTER WINS!", fg="#fb7185")

    score_label.config(
        text=f"You: {user_score}     Computer: {computer_score}"
    )

# Reset function
def reset_game():
    global user_score, computer_score

    user_score = 0
    computer_score = 0

    user_label.config(text="You chose: -")
    computer_label.config(text="Computer chose: -")
    result_label.config(text="Choose your move!", fg="white")
    score_label.config(text="You: 0     Computer: 0")

# Heading
title = tk.Label(
    root,
    text="ROCK PAPER SCISSORS",
    font=("Arial", 23, "bold"),
    bg="#172554",
    fg="white"
)
title.pack(pady=30)

# Instructions
instruction = tk.Label(
    root,
    text="Choose your move!",
    font=("Arial", 16),
    bg="#172554",
    fg="#93c5fd"
)
instruction.pack(pady=10)

# Game buttons
button_frame = tk.Frame(root, bg="#172554")
button_frame.pack(pady=25)

rock_button = tk.Button(
    button_frame, text="🪨 ROCK",
    font=("Arial", 14, "bold"),
    bg="#facc15", fg="black",
    width=10, command=lambda: play("Rock")
)
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(
    button_frame, text="📄 PAPER",
    font=("Arial", 14, "bold"),
    bg="#4ade80", fg="black",
    width=10, command=lambda: play("Paper")
)
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(
    button_frame, text="✂️ SCISSORS",
    font=("Arial", 14, "bold"),
    bg="#38bdf8", fg="black",
    width=11, command=lambda: play("Scissors")
)
scissors_button.grid(row=1, column=0, columnspan=2, pady=15)

# Choice labels
user_label = tk.Label(
    root, text="You chose: -",
    font=("Arial", 15),
    bg="#172554", fg="white"
)
user_label.pack(pady=8)

computer_label = tk.Label(
    root, text="Computer chose: -",
    font=("Arial", 15),
    bg="#172554", fg="white"
)
computer_label.pack(pady=8)

# Result
result_label = tk.Label(
    root, text="Choose your move!",
    font=("Arial", 20, "bold"),
    bg="#172554", fg="white"
)
result_label.pack(pady=20)

# Scoreboard
score_label = tk.Label(
    root, text="You: 0     Computer: 0",
    font=("Arial", 17, "bold"),
    bg="#1e40af", fg="white",
    padx=20, pady=15
)
score_label.pack(pady=15)

# Reset button
reset_button = tk.Button(
    root, text="🔄 PLAY AGAIN",
    font=("Arial", 14, "bold"),
    bg="#f97316", fg="white",
    width=18, command=reset_game
)
reset_button.pack(pady=20)

# Run application
root.mainloop()
