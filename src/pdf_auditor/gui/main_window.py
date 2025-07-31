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

# Label for Website URL
url_label = tk.Label(top_frame, text="Website URL:")
url_label.pack(side=tk.LEFT)

# Entry field for Website URL
url_entry = tk.Entry(top_frame, width=50)
url_entry.pack(side=tk.LEFT, padx=(10, 0))

#Start Tkinter event loop
root.mainloop()