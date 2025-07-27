import tkinter as tk

# Global variables
Server = 2
Team1 = 0
Team2 = 0

def update_label():
    label.config(text=f"{Team1} - {Team2}  |  Server: {Server}")

def Team1button():
    global Server, Team1, Team2
    if Server == 1 or Server == 2:
        Team1 += 1
    if Server == 3:
        Server = 4
    else:
        if Server == 4:
            Server = 1
    update_label()
    if Team1 >= 11 and Team1 - Team2 >= 2:	
        label.config(text=f"Team1 wins! {Team1} - {Team2}")
        #Reset_game()
def Team2button():
    global Server, Team1, Team2
    if Server == 3 or Server == 4:
        Team2 += 1
    if Server == 1:
        Server = 2
    else:
        if Server == 2:
            Server = 3
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
label = tk.Label(window, text="Score", font=("Helvetica", 16))
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