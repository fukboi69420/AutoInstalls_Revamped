import tkinter as tk

def create_ui():
    """
    This function creates a simple UI using the Tkinter framework.
    """
    # Create a new window
    window = tk.Tk()

    # Set the window title
    window.title("My UI")

    # Create a label
    label = tk.Label(window, text="Hello, World!")
    label.pack()

    # Run the UI
    window.mainloop()
