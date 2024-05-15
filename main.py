# https://github.com/CristiMCV91/
"""
🆃🆈🅿🅸🅽🅶 🆂🅿🅴🅴🅳 🆃🅴🆂🆃
"""
import tkinter
import customtkinter  # Custom module for GUI

def restartButtonEvent():
    pass




# System Settings
customtkinter.set_appearance_mode("system")
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

# Score label
max_score_var = 0
max_score_lbl = customtkinter.CTkLabel(first_frame, text="Max Score: "+str(max_score_var))
max_score_lbl.grid(row=2, column=0, padx=0, pady=10, sticky="w")

your_score_var = 0
your_score_lbl = customtkinter.CTkLabel(first_frame, text="Your Score: "+str(your_score_var))
your_score_lbl.grid(row=2, column=0, padx=0, pady=10, sticky="n")

# Corrected Case Per Minute (CPM)
cpm_lbl = customtkinter.CTkLabel(second_frame, text="Corrected CPM:")
cpm_lbl.grid(row=0, column=0, padx=10, pady=10, sticky="n")

cpm_var = tkinter.StringVar()
cpm_var_lbl = customtkinter.CTkEntry(second_frame,  textvariable=cpm_var, font=(("Arial"), 15, "bold"), width=40, state="disabled")
cpm_var_lbl.grid(row=0, column=1, padx=10, pady=10, sticky="n")

# Word Per Minute (WPM)
wpm_lbl = customtkinter.CTkLabel(second_frame, text="WPM:")
wpm_lbl.grid(row=0, column=2, padx=10, pady=10, sticky="n")

wpm_var = tkinter.StringVar()
wpm_var_lbl = customtkinter.CTkEntry(second_frame,  textvariable=wpm_var, font=(("Arial"), 15, "bold"), width=40, state="disabled")
wpm_var_lbl.grid(row=0, column=3, padx=10, pady=10, sticky="n")

# Time left
time_lbl = customtkinter.CTkLabel(second_frame, text="Time left:")
time_lbl.grid(row=0, column=4, padx=10, pady=10, sticky="n")

time_left_var = tkinter.StringVar()
time_left_lbl = customtkinter.CTkEntry(second_frame,  textvariable=time_left_var, font=(("Arial"), 15, "bold"), width=40, state="disabled")
time_left_lbl.grid(row=0, column=5, padx=10, pady=10, sticky="n")

# Restart button
restart_btn = customtkinter.CTkButton(second_frame, text="Restart", command=restartButtonEvent)
restart_btn.grid(row=0, column=6, padx=10, pady=10, sticky="n")

# Scrollable  frame words box
words_box_frame = customtkinter.CTkScrollableFrame(third_frame, width=500, height=200)
words_box_frame.grid(row=0, column=0, padx=10, pady=10, sticky="n")

# Text box for typing
typing_textbox = customtkinter.CTkEntry(third_frame, width=500, height=50, font=(("Arial"), 40), justify="center")
typing_textbox.grid(row=1, column=0, padx=10, pady=20, sticky="s")

# Corrected Case Per Minute (CPM)
final_score_lbl = customtkinter.CTkLabel(third_frame, text=f'Your score: {your_score_var} CPM (that is {your_score_var} WPM)', font=(("Arial"), 16))
final_score_lbl.grid(row=2, column=0, padx=0, pady=10, sticky="s")

# Run app
app.mainloop()

