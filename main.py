import tkinter as tk
import customtkinter as ctk
import random
import time
import threading

# Function to read words from the file
def read_word_list():
    try:
        with open("words.txt", 'r') as file:
            word_list = file.readlines()
            word_list = [word.strip() for word in word_list]
            random.shuffle(word_list)  # Shuffle the list of words
            return word_list
    except FileNotFoundError:
        print("Error: The words.txt file was not found.")
        return []

# Function to start the timer
def start_timer(event, reset=0):
    typing_textbox.unbind("<Key>")  # Unbind the key event to avoid multiple bindings
    typing_textbox.configure(state="normal")

    def run(seconds=60):
        global running
        running = True
        while seconds > 0 and running:
            time.sleep(1)
            seconds -= 1
            time_left_var.set(seconds)  # Update the time left variable
        time_left_var.set(0)
        typing_textbox.configure(state="disabled")  # Disable the typing textbox when time is up
        cpm_var_lbl.configure(fg_color="#87ceeb")  # Change the color of CPM label
        wpm_var_lbl.configure(fg_color="#87ceeb")  # Change the color of WPM label
        time_left_lbl.configure(fg_color="#87ceeb")  # Change the color of time left label

    countdown_thread = threading.Thread(target=run)
    countdown_thread.start()

# Function to calculate statistics
def calculate_statistics(match_list):
    cpm_var.set(len(typing_textbox.get()))  # Set CPM variable to the length of the typed text
    correct_words = sum(1 for item in match_list if item[2])  # Count correct words
    wpm_var.set(correct_words)  # Set WPM variable to the count of correct words

# Function to restart the test
def restart_test():
    global shuffled_text, running
    shuffled_text = ' '.join(read_word_list())  # Read and shuffle the word list
    words_textbox.configure(state='normal')
    words_textbox.delete("0.0", tk.END)  # Clear the words textbox
    words_textbox.insert("0.0", shuffled_text)  # Insert the new shuffled text
    words_textbox.configure(state='disabled')
    typing_textbox.configure(state="normal")
    typing_textbox.delete(0, tk.END)  # Clear the typing textbox
    typing_textbox.bind("<Key>", start_timer)  # Bind the key event to start the timer
    running = False
    time_left_var.set(60)  # Reset the timer
    cpm_var.set(0)  # Reset CPM variable
    wpm_var.set(0)  # Reset WPM variable
    typing_textbox.configure(state="normal")
    cpm_var_lbl.configure(fg_color="#FFFFFF")  # Reset CPM label color
    wpm_var_lbl.configure(fg_color="#FFFFFF")  # Reset WPM label color
    time_left_lbl.configure(fg_color="#FFFFFF")  # Reset time left label color

# Function to update the colors of the words
def update_word_colors(match_list):
    word_text = shuffled_text
    words = word_text.split()

    words_textbox.configure(state='normal')
    words_textbox.tag_delete("color")  # Delete previous color tags

    for i in range(len(match_list), len(words)):
        words_textbox.tag_remove(words[i], "1.0", "end")  # Remove tags from unmatched words

    for i in range (0, len(match_list)-1):
        words_textbox.tag_config(words[i],background="")  # Reset background color

    words_textbox.tag_config(words[len(match_list)], background="yellow")  # Highlight current word

    current_word_index = len(match_list)

    for word in match_list:
        start_index = word_text.index(word[0])
        end_index = start_index + len(word[0])
        words_textbox.tag_add(word[0], f"1.{start_index}", f"1.{end_index}")

        if word[2]:
            words_textbox.tag_config(word[0], foreground="green")  # Correct words in green
        else:
            words_textbox.tag_config(word[0], foreground="red")  # Incorrect words in red

    # Auto-scroll to the current word
    if match_list:
        words_textbox.see(f"1.{word_text.index(words[current_word_index])}")

# Function to match typed words with displayed words
def match_lists(event):
    typed_text = typing_textbox.get()
    words = shuffled_text.split()
    typed_words = typed_text.split()
    match_list = []

    try:
        for i in range(len(typed_words)):
            match_list.append((words[i], typed_words[i], words[i] == typed_words[i]))  # Create match list
    except IndexError:
        pass

    update_word_colors(match_list)
    calculate_statistics(match_list)

# System Settings
ctk.set_appearance_mode("light")  # Set appearance mode to light
ctk.set_default_color_theme("blue")  # Set default color theme to blue

# App Typing Speed Test
app = ctk.CTk()
app.geometry("720x720")  # Set app window size
app.title("Typing Speed Test")  # Set app title

# Create frames
first_frame = ctk.CTkFrame(app, width=720, height=120, fg_color="transparent")
first_frame.grid(column=0, row=0, padx=10, pady=10, sticky="n")
second_frame = ctk.CTkFrame(app, width=720, height=300, fg_color="#bebebe")
second_frame.grid(column=0, row=1, padx=10, pady=10, sticky="n")
third_frame = ctk.CTkFrame(app, width=720, height=300, fg_color="transparent")
third_frame.grid(column=0, row=2, padx=10, pady=10, sticky="n")

# Logo
logo_lbl = ctk.CTkLabel(first_frame, text="🆃🆈🅿🅸🅽🅶 🆂🅿🅴🅴🅳 🆃🅴🆂🆃", font=("Arial", 56))
logo_lbl.grid(row=0, column=0, padx=10, pady=10, sticky="n")

# Intro text
intro_text = """
How fast are your fingers? Do the one-minute typing test to find out! 
Press the space bar after each word. At the end, you'll get your typing speed in CPM and WPM.
Good luck!
"""
intro_lbl = ctk.CTkLabel(first_frame, text=intro_text)
intro_lbl.grid(row=1, column=0, padx=10, pady=10, sticky="n")

# Corrected Characters Per Minute (CPM)
cpm_lbl = ctk.CTkLabel(second_frame, text="Total CPM:")
cpm_lbl.grid(row=0, column=0, padx=10, pady=10, sticky="n")
cpm_var = tk.StringVar()
cpm_var.set(0)
cpm_var_lbl = ctk.CTkEntry(second_frame, textvariable=cpm_var, font=("Arial", 15, "bold"), width=40, state="disabled")
cpm_var_lbl.grid(row=0, column=1, padx=10, pady=10, sticky="n")

# Words Per Minute (WPM)
wpm_lbl = ctk.CTkLabel(second_frame, text="Correct WPM:")
wpm_lbl.grid(row=0, column=2, padx=10, pady=10, sticky="n")
wpm_var = tk.StringVar()
wpm_var.set(0)
wpm_var_lbl = ctk.CTkEntry(second_frame, textvariable=wpm_var, font=("Arial", 15, "bold"), width=40, state="disabled")
wpm_var_lbl.grid(row=0, column=3, padx=10, pady=10, sticky="n")

# Time left
time_lbl = ctk.CTkLabel(second_frame, text="Time left:")
time_lbl.grid(row=0, column=4, padx=10, pady=10, sticky="n")
time_left_var = tk.StringVar()
time_left_var.set(60)
time_left_lbl = ctk.CTkEntry(second_frame, textvariable=time_left_var, font=("Arial", 15, "bold"), width=40, state="normal")
time_left_lbl.grid(row=0, column=5, padx=10, pady=10, sticky="n")

# Restart button
restart_btn = ctk.CTkButton(second_frame, text="Restart", command=restart_test)
restart_btn.grid(row=0, column=6, padx=10, pady=10, sticky="n")

# Words textbox
shuffled_text = ' '.join(read_word_list())  # Read and shuffle the word list
words_textbox = ctk.CTkTextbox(third_frame, width=500, height=200, font=("Arial", 40), wrap='word')
words_textbox.insert("0.0", shuffled_text)
words_textbox.configure(state='disabled')
words_textbox.grid(row=0, column=0, padx=10, pady=10, sticky="n")

# Typing textbox
typing_textbox = ctk.CTkEntry(third_frame, width=500, height=50, font=("Arial", 40), justify="center")
typing_textbox.grid(row=1, column=0, padx=10, pady=20, sticky="s")
typing_textbox.bind("<KeyRelease>", match_lists)  # Bind key release event to match lists function
typing_textbox.bind("<Key>", start_timer)  # Bind key event to start timer
typing_textbox.focus()

explanation_text = """
The countdown will start when you type the first letter.
Press RESTART button to reload a new typing session.
"""
explanation_text_lbl = ctk.CTkLabel(third_frame, text=explanation_text)
explanation_text_lbl.grid(row=2, column=0, padx=10, pady=10, sticky="n")

match_lists("start app")  # Initial call to match lists function

# Run the app
app.mainloop()