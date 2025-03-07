import tkinter as tk
from tkinter import ttk, messagebox
from utils.url_analyzer import analyze_url
from utils.email_analyzer import analyze_email

# Function to analyze URL
def analyze_url_gui():
    url = url_entry.get()
    if url:
        result = analyze_url(url)
        result_label.config(text=f"Result: {result}", fg="#00FF00" if "safe" in result.lower() else "#FF0000")
    else:
        messagebox.showwarning("Input Error", "Please enter a URL.")

# Function to analyze email
def analyze_email_gui():
    email = email_entry.get("1.0", tk.END).strip()
    if email:
        result = analyze_email(email)
        result_label.config(text=f"Result: {result}", fg="#00FF00" if "safe" in result.lower() else "#FF0000")
    else:
        messagebox.showwarning("Input Error", "Please enter email content.")

# Create the main window
root = tk.Tk()
root.title("PhishNet Detector")
root.geometry("500x400")
root.configure(bg="#000000")

# Make the window a bit transparent
root.attributes("-alpha", 0.95)

# Load a robotic font (ensure the font is installed on your system)
robotic_font = ("Roboto", 12)

# Header
header = tk.Label(root, text="PhishNet Detector", font=("Roboto", 20, "bold"), bg="#000000", fg="#00FF00")
header.pack(pady=10)

# URL Section
url_frame = tk.Frame(root, bg="#000000")
url_frame.pack(pady=10)

url_label = tk.Label(url_frame, text="Enter URL to Analyze:", font=robotic_font, bg="#000000", fg="#00FF00")
url_label.pack()

url_entry = tk.Entry(url_frame, width=50, font=robotic_font, bg="#111111", fg="#00FF00", insertbackground="#00FF00")
url_entry.pack(pady=5)

url_button = tk.Button(url_frame, text="Analyze URL", command=analyze_url_gui, font=robotic_font, bg="#111111", fg="#00FF00", relief="flat")
url_button.pack(pady=5)

# Email Section
email_frame = tk.Frame(root, bg="#000000")
email_frame.pack(pady=10)

email_label = tk.Label(email_frame, text="Enter Email Content to Analyze:", font=robotic_font, bg="#000000", fg="#00FF00")
email_label.pack()

email_entry = tk.Text(email_frame, width=50, height=5, font=robotic_font, bg="#111111", fg="#00FF00", insertbackground="#00FF00")
email_entry.pack(pady=5)

email_button = tk.Button(email_frame, text="Analyze Email", command=analyze_email_gui, font=robotic_font, bg="#111111", fg="#00FF00", relief="flat")
email_button.pack(pady=5)

# Result Section
result_label = tk.Label(root, text="Result: ", font=robotic_font, bg="#000000", fg="#00FF00")
result_label.pack(pady=20)

# Run the application
root.mainloop()