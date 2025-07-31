import tkinter as tk
from tkinter import *
from tkinter import ttk

# Create main application
root = tk.Tk()
root.title("PDF Auditor")
root.geometry("800x600")


# Create a frame at the top for the URL input
top_frame = tk.Frame(root)
top_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

# Use grid for dynamic resizing
top_frame.columnconfigure(1, weight=1)

# Label for Website URL
url_label = tk.Label(top_frame, text="Website URL:")
url_label.grid(row=0, column=0, sticky="w")

# Entry field for Website URL
url_entry = tk.Entry(top_frame)
url_entry.grid(row=0, column=1, sticky="ew", padx=(10, 0))

#Start Tkinter event loop
root.mainloop()