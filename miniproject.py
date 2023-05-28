import tkinter as tk
from tkinter import messagebox
import time

class ClockTimerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Clock and Timer")

        # Clock label
        self.clock_label = tk.Label(root, text="", font=("Arial", 32), fg="blue")
        self.clock_label.pack(pady=20)

        # Timer label
        self.timer_label = tk.Label(root, text="", font=("Arial", 24), fg="red")
        self.timer_label.pack(pady=10)

        # Timer input
        self.timer_input = tk.Entry(root, font=("Arial", 16))
        self.timer_input.pack(pady=10)

        # Timer start button
        self.start_button = tk.Button(root, text="Start Timer", command=self.start_timer, font=("Arial", 14), bg="green", fg="white")
        self.start_button.pack(pady=10)

    def update_clock(self):
        current_time = time.strftime("%I:%M:%S %p")  # %I for 12-hour format, %p for AM/PM
        self.clock_label.config(text=current_time)
        self.root.after(1000, self.update_clock)

    def start_timer(self):
        timer_input = self.timer_input.get()
        timer_parts = timer_input.split(':')

        if len(timer_parts) != 3:
            # Invalid input format
            self.timer_label.config(text="Invalid input format!", fg="red")
            return

        try:
            hours = int(timer_parts[0])
            minutes = int(timer_parts[1])
            seconds = int(timer_parts[2])
        except ValueError:
            # Invalid input format
            self.timer_label.config(text="Invalid input format!", fg="red")
            return

        total_seconds = hours * 3600 + minutes * 60 + seconds
        self.timer_label.config(text=f"Timer: {timer_input}", fg="black")

        while total_seconds > 0:
            hours = total_seconds // 3600
            minutes = (total_seconds % 3600) // 60
            seconds = (total_seconds % 3600) % 60
            timer_text = f"Timer: {hours:02d}:{minutes:02d}:{seconds:02d}"
            self.timer_label.config(text=timer_text, fg="black")
            self.root.update()
            time.sleep(1)
            total_seconds -= 1

        self.timer_label.config(text="Timer: Complete", fg="green")
        messagebox.showinfo("Timer Complete", "The timer has finished!")


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("400x300")  # Set window size
    root.resizable(False, False)  # Disable window resizing
    root.configure(bg="white")  # Set window background color

    gui = ClockTimerGUI(root)
    gui.update_clock()  # Start the clock update

    root.mainloop()
