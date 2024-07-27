
import tkinter as tk
from tkinter import filedialog
import pyscreenshot as ImageGrab

def capture_screenshot():
    try:
        # Capture the selected region
        screenshot = ImageGrab.grab(bbox=(x1.get(), y1.get(), x2.get(), y2.get()))

        # Ask user for the save location
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])

        if save_path:
            screenshot.save(save_path)
            status_label.config(text=f"Screenshot saved as {save_path}")
        else:
            status_label.config(text="Screenshot not saved (canceled).")
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}")

# Create the GUI
root = tk.Tk()
root.title("Screenshot App")
root.geometry("200x200")

x1 = tk.IntVar()
y1 = tk.IntVar()
x2 = tk.IntVar()
y2 = tk.IntVar()

label = tk.Label(root, text="Select a region (x1, y1, x2, y2):")
label.pack()

entry_frame = tk.Frame(root)
entry_frame.pack()

for var in [x1, y1, x2, y2]:
    entry = tk.Entry(entry_frame, textvariable=var, width=5)
    entry.pack(side="left")

capture_button = tk.Button(root, text="Capture Screenshot", command=capture_screenshot)
capture_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
