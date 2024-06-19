import tkinter as tk
from tkinter import ttk
import sv_ttk
import random


def generate_vocab():
    vocab = []
    if stage1.get():
        stage1Vocab = ['1', '2', '3']
        vocab.extend(stage1Vocab)
        vocab.append("Stage 1")
    if stage2.get():
        vocab.append("Stage 2")
    if stage3.get():
        vocab.append("Stage 3")
    if stage4.get():
        vocab.append("Stage 4")

    random.shuffle(vocab)
    # You can replace the above line with the function you want to call
    # For example:
    # your_function(selections)
    open_new_window(vocab)


def open_new_window(selections):
    # Create a new window
    bee_window = tk.Toplevel(root)
    bee_window.title("OrthoSpellum: Competition mode")
    bee_window.geometry('900x600')

    sv_ttk.use_light_theme()

    # Display the selected options in the new window
    ttk.Label(bee_window, text="You selected:").pack(pady=10)
    for selection in selections:
        ttk.Label(bee_window, text=selection).pack()

# Create the main window
root = tk.Tk()
root.geometry('400x400')
root.title("OrthoSpellum")

# Apply sv_ttk theme
sv_ttk.use_light_theme()

# Define Tkinter variables for the checkboxes
stage1 = tk.BooleanVar()
stage2 = tk.BooleanVar()
stage3 = tk.BooleanVar()
stage4 = tk.BooleanVar()


# Create the checkboxes
checkbox1 = ttk.Checkbutton(root, text="Stage 1", variable=stage1)
checkbox2 = ttk.Checkbutton(root, text="Stage 2", variable=stage2)
checkbox3 = ttk.Checkbutton(root, text="Stage 3", variable=stage3)
checkbox4 = ttk.Checkbutton(root, text="Stage 4", variable=stage4)


# Pack the checkboxes into the window
checkbox1.pack(pady=5)
checkbox2.pack(pady=5)
checkbox3.pack(pady=5)

# Create the submit button
submit_button = ttk.Button(root, text="Submit", command=generate_vocab)
submit_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
