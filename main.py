# https://github.com/CristiMCV91/
"""
🆃🆈🅿🅸🅽🅶 🆂🅿🅴🅴🅳 🆃🅴🆂🆃
"""
import tkinter
import customtkinter  # Custom module for GUI
import random
from datetime import datetime
import time
import threading



# Funcție pentru începerea cronometrului
def start_timer(event, reset=0):

    typing_textbox.unbind("<Key>")
    typing_textbox.configure(state="normal")
    def run(seconds = 60):
        global your_score_var, running
        running = True
        while (seconds > 0) and (running == True):
            time.sleep(1)
            seconds -= 1
            time_left_var.set(seconds)
        time_left_var.set(0)
        typing_textbox.configure(state="disabled")

        your_score_var = wpm_var.get()

    countdown_thread = threading.Thread(target=run)
    countdown_thread.start()


def statistic(match_list):
    cpm_var.set(len(typing_textbox.get()))

    count_true = 0
    for item in match_list:
        if item[2] == True:
            count_true += 1
    wpm_var.set(count_true)

def readWordList():
    with open("words.txt", 'r') as file:
        word_list= file.readlines()
        word_list = [word.strip() for word in word_list]
        random.shuffle(word_list)
        print(word_list)
        return word_list


def restartButtonEvent():
    global shuffled_text, running
    shuffled_text = ' '.join(readWordList())
    words_textbox.configure(state='normal')
    words_textbox.delete("0.0", tkinter.END)
    words_textbox.insert("0.0", shuffled_text)
    words_textbox.configure(state='disabled')
    typing_textbox.delete(0, tkinter.END)
    typing_textbox.bind("<Key>", start_timer)
    running = False
    time_left_var.set(60)
    cpm_var.set(0)
    wpm_var.set(0)
    typing_textbox.configure(state="normal")


def coloredWords(match_list):
    word_text_var = shuffled_text

    list1 = word_text_var.split()

    words_textbox.configure(state='normal')
    words_textbox.tag_delete("color")

    for i in range (len(match_list), len(list1)):
        words_textbox.tag_remove(list1[i], "1.0", "end")

    for i in range (0, len(match_list)-1):
        words_textbox.tag_config(list1[i],background="")

    words_textbox.tag_config(list1[len(match_list)], background="yellow")
    print(len(match_list))
    print(list1[len(match_list)])

    for word in match_list:
        start_index = word_text_var.index(word[0])
        end_index = start_index + len(word[0])

        words_textbox.tag_add(word[0], f"1.{start_index}",f"1.{end_index}")

        for word in match_list[:-1]:
            start_index = word_text_var.index(word[0])
            end_index = start_index + len(word[0])

            words_textbox.tag_add(word[0], f"1.{start_index}", f"1.{end_index}")

            if word[2] == True:
                words_textbox.tag_config(word[0], foreground="green")
            elif (word[2] == False):
                words_textbox.tag_config(word[0], foreground="red")


def matchLists(event):
    typed_text_var = typing_textbox.get()
    word_text_var = shuffled_text


    list1 = word_text_var.split()
    list2 = typed_text_var.split()
    match_list = []

    try:
        for i in range(0,len(list2)):
            if list1[i] == list2[i]:
                match_list.append((list1[i], list2[i], True))
            elif not list1[i] == list2[i]:
                match_list.append((list1[i], list2[i], False))
    except:
        pass

    coloredWords(match_list)
    statistic(match_list)



# System Settings
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

# App Typing Speed Test
app = customtkinter.CTk()
app.geometry("720x720")
app.title("Typing Speed Test")

# Create 3 frames for the app content
first_frame = customtkinter.CTkFrame(app, width=720, height=120, fg_color="transparent", border_color="#FF0000", border_width=0)
first_frame.grid(column=0, row=0, padx=10, pady=10, sticky="n")
second_frame = customtkinter.CTkFrame(app, width=720, height=300, fg_color="#bebebe", border_color="#FF0000", border_width=0)
second_frame.grid(column=0, row=1, padx=10, pady=10, sticky="n")
third_frame = customtkinter.CTkFrame(app, width=720, height=300, fg_color="transparent", border_color="#FF0000", border_width=0)
third_frame.grid(column=0, row=2, padx=10, pady=10, sticky="n")

# Add UI Elements

# Logo Typing Speed Test
logo_lbl = customtkinter.CTkLabel(first_frame, text="🆃🆈🅿🅸🅽🅶 🆂🅿🅴🅴🅳 🆃🅴🆂🆃", font=("Arial", 56))
logo_lbl.grid(row=0, column=0, padx=10, pady=10, sticky="n")

# Add intro text
intro_text = """
How fast are your fingers? Do the one-minute typing test to find out! 
Press the space bar after each word. At the end, you'll get your typing speed in CPM and WPM.
Good luck!
"""
intro_lbl = customtkinter.CTkLabel(first_frame, text=intro_text)
intro_lbl.grid(row=1, column=0, padx=10, pady=10, sticky="n")

# # Score label
# max_score_var = 0
# max_score_lbl = customtkinter.CTkLabel(first_frame, text="Max Score: "+str(max_score_var))
# max_score_lbl.grid(row=2, column=0, padx=0, pady=10, sticky="w")
#
# your_score_var = 0
# your_score_lbl = customtkinter.CTkLabel(first_frame, text=f"Your Score: "+str(your_score_var))
# your_score_lbl.grid(row=2, column=0, padx=0, pady=10, sticky="n")

# Corrected Case Per Minute (CPM)
cpm_lbl = customtkinter.CTkLabel(second_frame, text="Total CPM:")
cpm_lbl.grid(row=0, column=0, padx=10, pady=10, sticky="n")

cpm_var = tkinter.StringVar()
cpm_var.set(0)
cpm_var_lbl = customtkinter.CTkEntry(second_frame,  textvariable=cpm_var, font=(("Arial"), 15, "bold"), width=40, state="disabled")
cpm_var_lbl.grid(row=0, column=1, padx=10, pady=10, sticky="n")

# Word Per Minute (WPM)
wpm_lbl = customtkinter.CTkLabel(second_frame, text="Correct WPM:")
wpm_lbl.grid(row=0, column=2, padx=10, pady=10, sticky="n")

wpm_var = tkinter.StringVar()
wpm_var.set(0)
wpm_var_lbl = customtkinter.CTkEntry(second_frame,  textvariable=wpm_var, font=(("Arial"), 15, "bold"), width=40, state="disabled")
wpm_var_lbl.grid(row=0, column=3, padx=10, pady=10, sticky="n")

# Time left
time_lbl = customtkinter.CTkLabel(second_frame, text="Time left:")
time_lbl.grid(row=0, column=4, padx=10, pady=10, sticky="n")

time_left_var = tkinter.StringVar()
time_left_var.set(60)
time_left_lbl = customtkinter.CTkEntry(second_frame,  textvariable=time_left_var, font=(("Arial"), 15, "bold"), width=40, state="normal")
time_left_lbl.grid(row=0, column=5, padx=10, pady=10, sticky="n")

# Restart button
restart_btn = customtkinter.CTkButton(second_frame, text="Restart", command=restartButtonEvent)
restart_btn.grid(row=0, column=6, padx=10, pady=10, sticky="n")

# Scrollable frame words box
shuffled_text = ' '.join(readWordList())
words_textbox = customtkinter.CTkTextbox(third_frame, width=500, height=200, font=(("Arial"), 40), wrap='word')
words_textbox.insert("0.0", shuffled_text)
words_textbox.configure(state='normal')
words_textbox.grid(row=0, column=0, padx=10, pady=10, sticky="n")

# Text box for typing
typing_textbox = customtkinter.CTkEntry(third_frame, width=500, height=50, font=(("Arial"), 40), justify="center")
typing_textbox.grid(row=1, column=0, padx=10, pady=20, sticky="s")
typing_textbox.bind("<KeyRelease>", matchLists)
typing_textbox.bind("<Key>", start_timer)

typing_textbox.focus()
matchLists("Start")


# Run app
app.mainloop()

