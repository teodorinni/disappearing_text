import tkinter as tk
from tkinter import filedialog

countdowns = 0
countdown_ended = False


# countdown mechanism
def start_countdown(*args):
    global countdowns
    if not countdown_ended:
        countdowns += 1
        countdown(10, countdowns)


def countdown(seconds_left, countdown_number):
    global countdowns, countdown_ended
    if countdown_number < countdowns:
        pass
    elif seconds_left != 0:
        app.after(1000, countdown, seconds_left - 1, countdown_number)
        timer_text.set(f"Seconds left: {seconds_left}")
    else:
        countdown_ended = True
        timer_text.set(f"Seconds left: {seconds_left}")
        text_box.config(state="disabled")
        download_btn.config(state="normal")
        reset_btn.config(state="normal")


# reset timer and text window
def reset():
    global countdowns, countdown_ended
    countdowns = 0
    countdown_ended = False
    text_box.config(state="normal")
    download_btn.config(state="disabled")
    reset_btn.config(state="disabled")
    timer_text.set(f"Seconds left: 10")
    text_box.delete(1.0, tk.END)


# save file as .txt
def save():
    file = filedialog.asksaveasfile(mode="w", defaultextension=".txt", filetypes=[("txt", "*.txt")])
    if file is None:
        return
    file.write(text_box.get(1.0, tk.END))


# app window initialization
app = tk.Tk()
app.minsize(width=795, height=600)
app.title("Disappearing Text App")
app.config(padx=25, pady=25)

# text box
text_box = tk.Text(app, width=82, height=25, wrap="word", font=("arial", 12))
text_box.grid(row=0, column=0, columnspan=3, pady=20)
text_box.bind("<KeyRelease>", start_countdown)

# countdown label
timer_text = tk.StringVar(app, value="Seconds left: 10")
timer = tk.Label(app, textvariable=timer_text, width=17, anchor="w")
timer.grid(row=1, column=0)

# download button
download_btn = tk.Button(app, text="Download Text (as .txt)", state="disabled", width=21, command=save)
download_btn.grid(row=1, column=1, ipady=5)

# reset button
reset_btn = tk.Button(app, text="Reset", state="disabled", width=7, command=reset)
reset_btn.grid(row=1, column=2, ipady=5)

app.mainloop()
