import json
import tkinter as tk
from tkinter import ttk
import keyboard
import clipboard

# Load the JSON file
try:
    with open('mappings.json') as f:
        try:
            KEY_MAPPINGS = json.load(f)
        except json.decoder.JSONDecodeError:
            print("Error: mappings.json file is not defined correctly!")
            input()
except FileNotFoundError:
    print("ERROR: mappings.json file not found!")
    input()
    
# Function to insert a special character
def insert_char(key):
    if key in KEY_MAPPINGS:
        keyboard.write(KEY_MAPPINGS[key])
    else:
        keyboard.write(key)

# Function to register a hotkey
hotkey_ids = {}
def register_hotkey(key):
    hotkey_id = keyboard.add_hotkey(
        key, insert_char, args=[key], suppress=True)
    hotkey_ids[key] = hotkey_id

# Function to unregister a hotkey
def unregister_hotkey(key):
    hotkey_id = hotkey_ids[key]
    keyboard.remove_hotkey(hotkey_id)
    del hotkey_ids[key]

# Function to toggle the hotkeys on and off
def toggle_hotkeys():
    global hotkeys_enabled
    hotkeys_enabled = not hotkeys_enabled
    if hotkeys_enabled:
        on_off_button.config(text="Hotkeys: ON")
        for key in KEY_MAPPINGS.keys():
            register_hotkey(key)
    else:
        on_off_button.config(text="Hotkeys: OFF")
        for key in KEY_MAPPINGS.keys():
            unregister_hotkey(key)

# Define a function to toggle the hotkeys on and off when Caps Lock key is pressed
def on_off_toggle_hotkeys():
    toggle_hotkeys()

# Create GUI
root = tk.Tk()
root.title("Key-mapper")

# Create button to toggle hotkeys on and off
hotkeys_enabled = True
on_off_button = tk.Button(root, text="Hotkeys: ON", command=toggle_hotkeys,
                          padx=10, pady=10, font=("Helvetica", 16))
on_off_button.pack()

# Create a helper label, to show the Caps lock is the hotkey to toggle the hotkeys on and off
label = tk.Label(root, text="Use caps lock to toggle hotkeys on/off\n(Note: Please turn off caps lock before starting this app)",
                 font=("Helvetica", 8))
label.pack()

# Create the table of keys and special characters
table = ttk.Treeview(root, columns=("hotkey", "char"),
                     show="headings", height="20")
table.heading("hotkey", text="Hotkey")
table.heading("char", text="Mapped to")
table.column("hotkey", width=100)
table.column("char", width=110)

# Add data to the table
for key, special_char in KEY_MAPPINGS.items():
    table.insert("", tk.END, values=(key, special_char))

# Create a vertical scrollbar for the table
scrollbar = ttk.Scrollbar(root, orient="vertical", command=table.yview)
table.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")
table.pack()

# Create a frame for each row of buttons
buttons_frame = tk.Frame(root)
# Maximum number of buttons per row
MAX_BUTTONS_PER_ROW = 17
button_count = 0
current_row_frame = tk.Frame(buttons_frame)
# Loop through the key mappings
for key, special_char in KEY_MAPPINGS.items():
    # If the maximum number of buttons per row has been reached, create a new row frame
    if button_count == MAX_BUTTONS_PER_ROW:
        current_row_frame.pack()
        current_row_frame = tk.Frame(buttons_frame)
        button_count = 0
    # Create the button and add it to the current row frame
    button = tk.Button(current_row_frame, text=special_char,
                       command=lambda k=key: insert_char(k),
                       padx=2, pady=2, font=("Helvetica", 13))
    button.pack(side=tk.LEFT)
    button_count += 1
# Pack the final row frame
current_row_frame.pack()
buttons_frame.pack()

# Create text field to enter text
text = tk.Text(root, height=10, width=50, font=("Helvetica", 12))
text.pack()

# Create a button to clip the text field to the clipboard
def clip_text():
    clipboard.copy(text.get("1.0", "end-1c"))
clip_button = tk.Button(root, text="Clip to Clipboard", command=clip_text,
                        padx=10, pady=10, font=("Helvetica", 16))
clip_button.pack()

# Register hotkeys
for key in KEY_MAPPINGS.keys():
    register_hotkey(key)

# Register Caps Lock key as a toggle for hotkeys
keyboard.add_hotkey('caps lock', on_off_toggle_hotkeys, suppress=True)

# Start GUI loop
root.mainloop()

# Unregister hotkeys
for key in KEY_MAPPINGS.keys():
    unregister_hotkey(key)

# Unregister Caps Lock key hotkey
keyboard.remove_hotkey('caps lock')