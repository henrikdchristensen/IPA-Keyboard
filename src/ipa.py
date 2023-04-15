import tkinter as tk
from tkinter import ttk
import keyboard
import clipboard

# Define key mappings
KEY_MAPPINGS = {
    'a': '\u00E6',
    'ctrl+a': '\u0061',
    'ctrl+shift+a': '\u0251',
    'b': '\u0062\u0325',
    'd': '\u0064\u0325',
    'ctrl+d': '\u00F0',
    'e': '\u0065',
    'ctrl+e': '\u0259',
    'ctrl+shift+e': '\u0250',
    'f': '\u0066',
    'g': '\u0261\u030A',
    'h': '\u0068',
    'i': '\u0069',
    'ctrl+shift+i': '\u026A',
    'j': '\u006A',
    'ctrl+j': '\u006A\u030A',
    'k': '\u006B\u02B0',
    'l': '\u006C',
    'ctrl+l': '\u006C\u0325',
    'm': '\u006D',
    'n': '\u006E',
    'ctrl+n': '\u014B',
    'o': '\u006F',
    'p': '\u0070\u02B0',
    'r': '\u0281',
    'ctrl+r': '\u0281\u0325',
    's': '\u0073',
    'ctrl+s': '\u0255',
    't': '\u0074\u02E2',
    'ctrl+t': '\u0074\u1D9D',
    'u': '\u0075',
    'v': '\u0076',
    'w': '\u0077',
    'y': '\u0079',
    'ctrl+y': '\u028F',
    'ø': '\u00F8',
    'ctrl+ø': '\u0153',
    'ctrl+shift+ø': '\u0276',
    'æ': '\u025B',
    'å': '\u0254',
    'ctrl+å': '\u0252',
    ':': '\u02D0',
    '?': '\u02C0',
    '<': '\u032F',
    '|': '\u007C',
    '\'': '\u02C8',
    ',': '\u0329',
    '-': '\u032F',
}

# Create a dictionary to store the hotkey IDs
hotkey_ids = {}

# Define a function to insert the special character for a given key


def insert_special_char(key):
    if key in KEY_MAPPINGS:
        keyboard.write(KEY_MAPPINGS[key])
    else:
        keyboard.write(key)

# Create a function to register a hotkey


def register_hotkey(key):
    hotkey_id = keyboard.add_hotkey(
        key, insert_special_char, args=[key], suppress=True)
    hotkey_ids[key] = hotkey_id

# Create a function to unregister a hotkey


def unregister_hotkey(key):
    hotkey_id = hotkey_ids[key]
    keyboard.remove_hotkey(hotkey_id)
    del hotkey_ids[key]

# Define a function to toggle the hotkeys on and off


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
root.title("IPA key-mapper")

# Create button to toggle hotkeys on and off
hotkeys_enabled = True
on_off_button = tk.Button(root, text="Hotkeys: ON", command=toggle_hotkeys,
                          padx=10, pady=10, font=("Helvetica", 16))
# Create a helper label, to show the Caps lock is the hotkey to toggle the hotkeys on and off
on_off_button.pack()

label = tk.Label(root, text="use caps lock to toggle hotkeys on/off",
                 font=("Helvetica", 10))
label.pack()

# Create the table of keys and special characters
table = ttk.Treeview(root, columns=("hotkey", "ipa_char"),
                     show="headings", height="20")
table.heading("hotkey", text="Hotkey")
table.heading("ipa_char", text="IPA-character")
table.column("hotkey", width=100)
table.column("ipa_char", width=100)

# Add data to the table
for key, special_char in KEY_MAPPINGS.items():
    table.insert("", tk.END, values=(key, special_char))

# Pack the table into the root window
# Create a vertical scrollbar for the table
# Create a vertical scrollbar for the table
scrollbar = ttk.Scrollbar(root, orient="vertical", command=table.yview)
table.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")
table.pack()

# Create buttons to insert selected special character
buttons_frame = tk.Frame(root)
# Define the maximum number of buttons on each row
MAX_BUTTONS_PER_ROW = 17
# Initialize a counter for the number of buttons in the current row
button_count = 0
# Initialize a variable to keep track of the current row frame
current_row_frame = tk.Frame(buttons_frame)
for key, special_char in KEY_MAPPINGS.items():
    # If the maximum number of buttons per row has been reached, create a new row frame
    if button_count == MAX_BUTTONS_PER_ROW:
        # Pack the current row frame and create a new one
        current_row_frame.pack()
        current_row_frame = tk.Frame(buttons_frame)
        # Reset the button count
        button_count = 0
    # Create the button and add it to the current row frame
    button = tk.Button(current_row_frame, text=special_char,
                       command=lambda k=key: insert_special_char(k),
                       padx=2, pady=2, font=("Helvetica", 13))
    button.pack(side=tk.LEFT)
    # Increment the button count
    button_count += 1
# Pack the final row frame
current_row_frame.pack()
buttons_frame.pack()

# Create text widget
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
