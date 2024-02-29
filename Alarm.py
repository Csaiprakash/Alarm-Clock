import tkinter as tk
import time
from pygame import mixer
from tkinter import messagebox

window = tk.Tk()
window.title("Alarm Clock")
window.geometry("730x630")
alarmtime = tk.StringVar()
msgi = tk.StringVar()
head = tk.Label(window, text="Alarm Clock", font=('comic sans', 20))
head.grid(row=0, columnspan=3, pady=10)

mixer.init()

def ala():
    alarm_time = alarmtime.get()
    current_time = time.strftime("%H:%M")

    if alarm_time == current_time:
        mixer.music.load("Sanchari.mp3")
        mixer.music.play()

        response = messagebox.showinfo('Info', f'{msgi.get()}')

        if response == 'ok':
            mixer.music.stop()

    else:
        window.after(1000, ala)

clockImg = tk.PhotoImage(file="Clock.png")
img = tk.Label(window, image=clockImg)
img.grid(row=1, rowspan=4, column=0, pady=10)

input_time = tk.Label(window, text="Time", font=('comic sans', 18))
input_time.grid(row=1, column=1, pady=5)

field1 = tk.Entry(window, textvariable=alarmtime, font=('comic sans', 18), width=6)
field1.grid(row=1, column=2, pady=5)

msg = tk.Label(window, text="Message", font=('comic sans', 18))
msg.grid(row=2, column=1, columnspan=2, sticky='nsew')

field2 = tk.Entry(window, textvariable=msgi, font=('comic sans', 18))
field2.grid(row=3, column=1, columnspan=2, sticky='nsew')

submit = tk.Button(window, text="SUBMIT", bg="#4CAF50", fg="white", font=('comic sans', 14), padx=10, pady=5, command=ala)
submit.grid(row=4, column=1, columnspan=2, pady=10)

window.mainloop()
