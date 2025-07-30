import tkinter as tk
from time import strftime

# Create the main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x250")
root.configure(bg="black")

# Define the label to display time
clock_label = tk.Label(
    root, 
    font=("Helvetica", 48), 
    background="black", 
    foreground="cyan"
)
clock_label.pack(anchor="center", pady=20)

# Function to update time every second
def update_time():
    current_time = strftime("%H:%M:%S \n %D")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)  # Call itself after 1 second

# Start the clock
update_time()

# Run the GUI loop
root.mainloop()
