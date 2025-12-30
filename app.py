import tkinter as tk

# Global variables
Team = 1
Server = 2
Team1 = 0
Team2 = 0


def update_label():
    label.config(text=f"{Team1} - {Team2}  |  Team: {Team} Server: {Server}")

def Team1button():
    global Server, Team1, Team2, Team
    if Team == 1:
        Team1 += 1
    if Team == 2 and Server == 1:
        Server = 2
    else:
        if Team == 2 and Server == 2:
            Server = 1
            Team = 1
    update_label()
    if Team1 >= 11 and Team1 - Team2 >= 2:	
        label.config(text=f"Team1 wins! {Team1} - {Team2}")
        #Reset_game()
def Team2button():
    global Server, Team1, Team2, Team
    if Team ==  2:
        Team2 += 1
    if Team == 1 and Server == 1:
        Server = 2
    else:
        if Team == 1 and Server == 2:
            Server = 1
            Team = 2
    update_label()
    if Team2 >= 11 and Team2 - Team1 >= 2:	
        label.config(text=f"Team2 wins! {Team2} - {Team1}")
        #Reset_game()

def Reset_game():
    global Server, Team1, Team2
    Server = 2
    Team1 = 0
    Team2 = 0
    update_label() 

# Create main window
window = tk.Tk()
window.title("Score Tracker")

# Add a label
label = tk.Label(window, text="0 - 0 | Team: 1 Server: 2", font=("Helvetica", 16))
label.pack(pady=10)

# Add buttons
button1 = tk.Button(window, text="Team1", command=Team1button, width=20)
button1.pack(pady=5)

button2 = tk.Button(window, text="Team2", command=Team2button, width=20)
button2.pack(pady=5)

#reset game button
Reset_button = tk.Button(window, text = "Reset Game", command=Reset_game, width=20)
Reset_button.pack(pady=10)
# Start the GUI event loop
window.mainloop()


