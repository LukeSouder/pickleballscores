import tkinter as tk
from team_states import *

# Global variables
current_state = Team1Server2(0,0)

def update_label(label):
    if current_state.winner() == 1:
        label.config(text=f"Team {current_state.team} wins! {current_state.team1} - {current_state.team2}")
    if current_state.winner() == 2:
        label.config(text=f"Team {current_state.team} wins! {current_state.team2} - {current_state.team1}")
    if current_state.winner() == 0:
        label.config(text=f"{current_state.team1} - {current_state.team2}  |  Team: {current_state.team} Server: {current_state.server}")

def team1_button():
    global  current_state
    
    current_state = current_state.team1_scored()
    update_label(label)
        #Reset_game()

def team2_button():
    global current_state
    current_state = current_state.team2_scored()
    update_label(label)
        #Reset_game()

def reset_game():
    global current_state
    current_state = Team1Server2(0,0)
    update_label(label) 

# Create main window
window = tk.Tk()
window.title("Score Tracker")

# Add a label
label = tk.Label(window, text="0 - 0 | Team: 1 Server: 2", font=("Helvetica", 16))
label.pack(pady=10)

# Add buttons
button1 = tk.Button(window, text="Team1", command=team1_button, width=20)
button1.pack(pady=5)

button2 = tk.Button(window, text="Team2", command=team2_button, width=20)
button2.pack(pady=5)

#reset game button
reset_button = tk.Button(window, text = "Reset Game", command=reset_game, width=20)
reset_button.pack(pady=10)

# Start the GUI event loop
window.mainloop()


