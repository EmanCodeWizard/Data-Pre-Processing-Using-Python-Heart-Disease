import tkinter as tk
from tkinter import Text, Scrollbar, filedialog, messagebox
import pandas as pd

# Create the main window
window = tk.Tk()
window.title("Data Preprocessing Project")
window.geometry("1000x600")
window.config(bg="#f7f1e3")

# Global dataframe to hold the data
df = None

# Title Label
title_label = tk.Label(
    window,
    text="Heart Disease Data Preprocessing Tool",
    font=("Helvetica", 24, "bold"),
    bg="#2c3e50",
    fg="white",
    pady=10,
)
title_label.pack(fill=tk.X)

# Frame for buttons
button_frame = tk.Frame(window, bg="#f7f1e3")
button_frame.pack(pady=20)

# Scrollable Text Widget
text_widget = Text(window, wrap=tk.NONE, height=20, width=100, font=("Courier", 10))
text_widget.pack(pady=10, padx=10)

# Scrollbars for Text Widget
vertical_scrollbar = Scrollbar(window, command=text_widget.yview, orient=tk.VERTICAL)
text_widget.config(yscrollcommand=vertical_scrollbar.set)
vertical_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

horizontal_scrollbar = Scrollbar(window, command=text_widget.xview, orient=tk.HORIZONTAL)
text_widget.config(xscrollcommand=horizontal_scrollbar.set)
horizontal_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

# Load Data Button
def load_data():
    global df
    file_path = filedialog.askopenfilename(
        filetypes=[("CSV Files", "*.csv"), ("Excel Files", "*.xlsx"), ("All Files", "*.*")]
    )
    if file_path:
        try:
            if file_path.endswith(".csv"):
                df = pd.read_csv(file_path)
            elif file_path.endswith(".xlsx"):
                df = pd.read_excel(file_path)
            else:
                messagebox.showerror("Error", "Unsupported file format!")
                return

            text_widget.delete("1.0", tk.END)  # Clear text widget
            text_widget.insert(tk.END, "Data Loaded Successfully!\n\n")
            text_widget.insert(tk.END, df.head().to_string())  # Display first few rows
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load data: {e}")

load_button = tk.Button(
    button_frame,
    text="Load Data",
    command=load_data,
    font=("Helvetica", 14),
    bg="#6c5ce7",
    fg="white",
    padx=20,
    pady=5,
)
load_button.grid(row=0, column=0, padx=20)

# Preprocess Data Button
def preprocess_data():
    global df
    if df is None:
        messagebox.showerror("Error", "No data loaded! Please load data first.")
        return

    try:
        # Handle missing values
        df.fillna(0, inplace=True)

        # Normalize numeric columns
        numeric_cols = df.select_dtypes(include=["number"]).columns
        df[numeric_cols] = (df[numeric_cols] - df[numeric_cols].mean()) / df[numeric_cols].std()

        text_widget.delete("1.0", tk.END)  # Clear text widget
        text_widget.insert(tk.END, "Data Preprocessed Successfully!\n\n")
        text_widget.insert(tk.END, df.head().to_string())  # Display first few rows of preprocessed data
    except Exception as e:
        messagebox.showerror("Error", f"Failed to preprocess data: {e}")

preprocess_button = tk.Button(
    button_frame,
    text="Preprocess Data",
    command=preprocess_data,
    font=("Helvetica", 14),
    bg="#0984e3",
    fg="white",
    padx=20,
    pady=5,
)
preprocess_button.grid(row=0, column=1, padx=20)

# Save Processed Data Button
def save_data():
    global df
    if df is None:
        messagebox.showerror("Error", "No data to save! Please preprocess data first.")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV Files", "*.csv"), ("Excel Files", "*.xlsx")],
    )
    if file_path:
        try:
            if file_path.endswith(".csv"):
                df.to_csv(file_path, index=False)
            elif file_path.endswith(".xlsx"):
                df.to_excel(file_path, index=False)
            else:
                messagebox.showerror("Error", "Unsupported file format!")
                return

            messagebox.showinfo("Success", "Data saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save data: {e}")

save_button = tk.Button(
    button_frame,
    text="Save Data",
    command=save_data,
    font=("Helvetica", 14),
    bg="#fdcb6e",
    fg="white",
    padx=20,
    pady=5,
)
save_button.grid(row=0, column=2, padx=20)

# Display Full Data Button
def display_data():
    global df
    if df is None:
        messagebox.showerror("Error", "No data loaded! Please load data first.")
        return

    try:
        text_widget.delete("1.0", tk.END)  # Clear text widget
        text_widget.insert(tk.END, "Full Data Display:\n\n")
        text_widget.insert(tk.END, df.to_string())  # Display full dataset
    except Exception as e:
        messagebox.showerror("Error", f"Failed to display data: {e}")

display_button = tk.Button(
    button_frame,
    text="Display Data",
    command=display_data,
    font=("Helvetica", 14),
    bg="#74b9ff",
    fg="white",
    padx=20,
    pady=5,
)
display_button.grid(row=0, column=3, padx=20)

# Start the GUI loop
window.mainloop()
