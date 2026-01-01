import tkinter as tk
import enum as Enum 

# Global variables
team = 1
server = 2
team1 = 0
team2 = 0

def update_label():
    label.config(text=f"{team1} - {team2}  |  Team: {team} Server: {server}")

def team1_button():
    global server, team1, team2, team
    if team == 1:
        team1 += 1
    if team == 2 and server == 1:
        server = 2
    else:
        if team == 2 and server == 2:
            server = 1
            team = 1
    update_label()
    if team1 >= 11 and team1 - team2 >= 2:	
        label.config(text=f"Team1 wins! {team1} - {team2}")
        #Reset_game()

def team2_button():
    global server, team1, team2, team
    if team ==  2:
        team2 += 1
    if team == 1 and server == 1:
        server = 2
    else:
        if team == 1 and server == 2:
            server = 1
            team = 2
    update_label()
    if team2 >= 11 and team2 - team1 >= 2:	
        label.config(text=f"Team2 wins! {team2} - {team1}")
        #Reset_game()

def reset_game():
    global server, team1, team2, team
    team = 1
    server = 2
    team1 = 0
    team2 = 0
    update_label() 

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


