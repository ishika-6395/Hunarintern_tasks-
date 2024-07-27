import tkinter as tk
from tkinter import messagebox
from plyer import notification
import time

class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")
        self.root.geometry("300x150")

        self.hours = tk.StringVar()
        self.minutes = tk.StringVar()
        self.seconds = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Set Timer (HH:MM:SS)").pack()

        tk.Entry(self.root, textvariable=self.hours, width=10).pack()
        tk.Label(self.root, text=":").pack()
        tk.Entry(self.root, textvariable=self.minutes, width=10).pack()
        tk.Label(self.root, text=":").pack()
        tk.Entry(self.root, textvariable=self.seconds, width=10).pack()

        tk.Button(self.root, text="Start", command=self.start_timer).pack()
        tk.Button(self.root, text="Stop", command=self.stop_timer).pack()
        tk.Button(self.root, text="Reset", command=self.reset_timer).pack()

        self.remaining_time = 0
        self.timer_running = False

    def start_timer(self):
        if not self.timer_running:
            total_seconds = int(self.hours.get()) * 3600 + int(self.minutes.get()) * 60 + int(self.seconds.get())
            self.remaining_time = total_seconds
            self.timer_running = True
            self.update_timer()

    def update_timer(self):
        if self.remaining_time > 0:
            self.remaining_time -= 1
            hours, remainder = divmod(self.remaining_time, 3600)
            minutes, seconds = divmod(remainder, 60)
            self.root.title(f"Time Remaining: {hours:02}:{minutes:02}:{seconds:02}")
            self.root.after(1000, self.update_timer)
        else:
            self.timer_running = False
            self.alert_user()

    def stop_timer(self):
        self.timer_running = False

    def reset_timer(self):
        self.timer_running = False
        self.root.title("Countdown Timer")

    def alert_user(self):
        notification.notify(
            title="Timer Alert",
            message="Time's up!",
            app_name="Countdown Timer",
        )
        messagebox.showinfo("Timer Alert", "Time's up!")

if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownTimer(root)
    root.mainloop()
