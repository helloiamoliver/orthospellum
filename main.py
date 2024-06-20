import tkinter as tk
from tkinter import ttk, messagebox
import sv_ttk
import random
import webbrowser
from PIL import ImageTk, Image

vocab = []

def callback(url):
   webbrowser.open_new_tab(url)

def generate_vocab():
    global vocab
    vocab.clear()  # Clear the existing vocab list
    if stage1.get():
        stage1Vocab = [['Latin11', 'English11'], ['Latin12', 'English12'], ['Latin13', 'English13']]
        vocab.extend(stage1Vocab)
    if stage2.get():
        stage2Vocab = [['Latin21', 'English21'], ['Latin22', 'English22'], ['Latin23', 'English23']]
        vocab.extend(stage2Vocab)
    if stage3.get():
        stage3Vocab = [['Latin31', 'English31'], ['Latin32', 'English32'], ['Latin33', 'English33']]
        vocab.extend(stage3Vocab)
    if not vocab:
        messagebox.showwarning("Error", "You must choose at least one stage.")
    else:
        random.shuffle(vocab)
        open_new_window()

def getWord(latin_label, english_label, timer_label):
    if not timer_label.timer_started:
        start_timer(timer_label, 60)
        timer_label.timer_started = True

    if vocab and timer_label.timer_started:
        current_word = vocab.pop()
        latin_label.config(text=current_word[0])
        english_label.config(text=current_word[1])


def start_timer(label, remaining=None):
    if remaining is not None:
        label.remaining = remaining

    if label.remaining <= 0:
        label.config(text="Time's up!", foreground="red")
    else:
        minutes, seconds = divmod(label.remaining, 60)
        label.config(text="{:02}:{:02}".format(minutes, seconds))
        label.remaining -= 1
        label.after(1000, start_timer, label)

def open_new_window():
    bee_window = tk.Toplevel(root)
    bee_window.title("OrthoSpellum: Competition mode")
    bee_window.geometry('900x600')

    sv_ttk.use_light_theme()

    timer_label = ttk.Label(bee_window, text="01:00", font=("Segoe UI", 64))
    timer_label.pack(pady=20)
    timer_label.timer_started = False  # Add a flag to indicate the timer has not started

    latin_label = ttk.Label(bee_window, text="Click go to start", font=("Segoe UI", 64))  # Initially empty
    latin_label.pack(pady=(20, 0))

    english_label = ttk.Label(bee_window, text="", font=("Segoe UI", 36))  # Initially empty
    english_label.pack(pady=(2, 20))

    start_button = ttk.Button(bee_window, text="Go", command=lambda: getWord(latin_label, english_label, timer_label), width=10)
    start_button.pack(side=tk.LEFT, padx=10, pady=10)

    stop_button = ttk.Button(bee_window, text="Quit", command=bee_window.destroy, width=10)
    stop_button.pack(side=tk.LEFT, padx=10, pady=10)

    bee_window.bind('<space>', lambda event: getWord(latin_label, english_label, timer_label))

# Create the main window
root = tk.Tk()
root.geometry('500x400')
root.title("OrthoSpellum")

# Apply sv_ttk theme
sv_ttk.use_light_theme()

# Define Tkinter variables for the checkboxes
stage1 = tk.BooleanVar()
stage2 = tk.BooleanVar()
stage3 = tk.BooleanVar()

# Create the checkboxes
checkbox1 = ttk.Checkbutton(root, text="Stage 1", variable=stage1)
checkbox2 = ttk.Checkbutton(root, text="Stage 2", variable=stage2)
checkbox3 = ttk.Checkbutton(root, text="Stage 3", variable=stage3)

header = tk.Label(root, text="OrthoSpellum", font=("Segoe UI", 24, 'bold'))
header.pack(pady=(10, 0))

subhead = tk.Label(root, text="A Latin Spelling Bee", font=("Segoe UI", 12))
subhead.pack(pady=(2, 10))

# Pack the checkboxes into the window
checkbox1.pack(pady=5)
checkbox2.pack(pady=5)
checkbox3.pack(pady=5)

# Create the submit button
submit_button = ttk.Button(root, text="Submit", command=generate_vocab)
submit_button.pack(pady=10)

# Create and position the copyright label at the bottom left
def position_copyright_label():
    # Calculate the position relative to the root window size
    x_position = 10
    y_position = root.winfo_height() - 5  # Adjusted vertical position to create space between labels
    copyright_label.place(x=x_position, y=y_position, anchor='sw')

# Initialize the root window

# Create the copyright label and link widgets
copyright_label = ttk.Label(root, text="Supplied by Kingswood School\n\n© Oliver Hewitt, 2024\noliverhewitt.co.uk")

# Configure the link label to respond to mouse clicks

# Call the function to position the copyright label initially
position_copyright_label()

# Bind the function to adjust the label positions when the window size changes
root.bind('<Configure>', lambda e: position_copyright_label())

# Start the main event loop
root.mainloop()

