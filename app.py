import tkinter as tk
Server = 2
Team1 = 0
Team2 = 0

def Team1button():
    global Server, Team1
    if Server == 1 or Server == 2:
        Team1=Team1+1
    if Server == 3 :
        Server = 4
    else:
        if Server == 4  :
           Server = 1
    print(Team1, "-", Team2, "-", Server)
    if Team1 >= 11 and Team1 - Team2 >= 2:	
	    print("Team1 wins", Team1, "-", Team2)
        
def Team2button():
    global Server, Team2
    if Server == 3 or Server == 4:
        Team2=Team2+1
    if Server == 1 :
        Server = 2
    else: 
        if Server == 2 :  
           Server = 3
    print(Team1, "-", Team2, "-", Server)
    if Team2 >= 11 and Team2 - Team1 >= 2:	
	    print("Team2 wins", Team2, "-", Team1)
    
    
    
# Create main window


window = tk.Tk()
window.title("My First GUI")

# Add a label
label = tk.Label(window, text="Score")
label.pack()


# Add a button
button = tk.Button(window, text="Team1", command=Team1button)
button.pack()
button = tk.Button(window, text="Team2", command=Team2button)
button.pack()
# Start the event loop
window.mainloop()


