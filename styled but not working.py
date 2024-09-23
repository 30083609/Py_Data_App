import tkinter as tk

# Function to clear the screen
def clear_screen():
    for widget in root.winfo_children():
        widget.pack_forget()

# Function to add more fields dynamically
def add_field(entries_list, parent_frame):
    entry = tk.Entry(parent_frame)
    entry.pack(pady=5)
    entries_list.append(entry)

# Input pages for different structures
def class_input_page():
    clear_screen()
    
    global fields_entries
    
    label = tk.Label(root, text="Enter Class Information", font=("Helvetica", 14, "bold"), bg="white")
    label.pack(pady=10)
    
    class_name_label = tk.Label(root, text="Class Name:", font=("Helvetica", 12), bg="white")
    class_name_label.pack(pady=5)
    class_name_entry = tk.Entry(root)
    class_name_entry.pack(pady=5)
    
    fields_label = tk.Label(root, text="Fields (one per box):", font=("Helvetica", 12), bg="white")
    fields_label.pack(pady=5)
    
    fields_frame = tk.Frame(root, bg="white")
    fields_frame.pack(pady=5)
    
    fields_entries = []
    for _ in range(4):  # Start with 4 fields
        add_field(fields_entries, fields_frame)
    
    add_field_button = tk.Button(root, text="Add Field", command=lambda: add_field(fields_entries, fields_frame), font=("Helvetica", 12, "bold"))
    add_field_button.pack(pady=5)
    
    submit_button = tk.Button(root, text="Generate Class", font=("Helvetica", 12, "bold"))
    submit_button.pack(pady=10)
    
    back_button = tk.Button(root, text="Back to Menu", command=main_menu, font=("Helvetica", 12, "bold"))
    back_button.pack(pady=10)

def function_input_page():
    clear_screen()
    
    global params_entries
    
    label = tk.Label(root, text="Enter Function Information", font=("Helvetica", 14, "bold"), bg="white")
    label.pack(pady=10)
    
    func_name_label = tk.Label(root, text="Function Name:", font=("Helvetica", 12), bg="white")
    func_name_label.pack(pady=5)
    func_name_entry = tk.Entry(root)
    func_name_entry.pack(pady=5)
    
    params_label = tk.Label(root, text="Parameters (one per box):", font=("Helvetica", 12), bg="white")
    params_label.pack(pady=5)
    
    params_frame = tk.Frame(root, bg="white")
    params_frame.pack(pady=5)
    
    params_entries = []
    for _ in range(4):  # Start with 4 parameters
        add_field(params_entries, params_frame)
    
    add_param_button = tk.Button(root, text="Add Parameter", command=lambda: add_field(params_entries, params_frame), font=("Helvetica", 12, "bold"))
    add_param_button.pack(pady=5)
    
    body_label = tk.Label(root, text="Function Body (one statement per line):", font=("Helvetica", 12), bg="white")
    body_label.pack(pady=5)
    body_entry = tk.Text(root, height=5, width=40)
    body_entry.pack(pady=5)
    
    submit_button = tk.Button(root, text="Generate Function", font=("Helvetica", 12, "bold"))
    submit_button.pack(pady=10)
    
    back_button = tk.Button(root, text="Back to Menu", command=main_menu, font=("Helvetica", 12, "bold"))
    back_button.pack(pady=10)

def tuple_input_page():
    clear_screen()
    
    global tuple_entries
    
    label = tk.Label(root, text="Enter Tuple Values", font=("Helvetica", 14, "bold"), bg="white")
    label.pack(pady=10)
    
    values_label = tk.Label(root, text="Values (one per box):", font=("Helvetica", 12), bg="white")
    values_label.pack(pady=5)
    
    tuple_frame = tk.Frame(root, bg="white")
    tuple_frame.pack(pady=5)
    
    tuple_entries = []
    for _ in range(4):  # Start with 4 values
        add_field(tuple_entries, tuple_frame)
    
    add_value_button = tk.Button(root, text="Add Value", command=lambda: add_field(tuple_entries, tuple_frame), font=("Helvetica", 12, "bold"))
    add_value_button.pack(pady=5)
    
    submit_button = tk.Button(root, text="Generate Tuple", font=("Helvetica", 12, "bold"))
    submit_button.pack(pady=10)
    
    back_button = tk.Button(root, text="Back to Menu", command=main_menu, font=("Helvetica", 12, "bold"))
    back_button.pack(pady=10)

def list_input_page():
    clear_screen()
    
    global list_entries
    
    label = tk.Label(root, text="Enter List Items", font=("Helvetica", 14, "bold"), bg="white")
    label.pack(pady=10)
    
    items_label = tk.Label(root, text="Items (one per box):", font=("Helvetica", 12), bg="white")
    items_label.pack(pady=5)
    
    list_frame = tk.Frame(root, bg="white")
    list_frame.pack(pady=5)
    
    list_entries = []
    for _ in range(4):  # Start with 4 items
        add_field(list_entries, list_frame)
    
    add_item_button = tk.Button(root, text="Add Item", command=lambda: add_field(list_entries, list_frame), font=("Helvetica", 12, "bold"))
    add_item_button.pack(pady=5)
    
    submit_button = tk.Button(root, text="Generate List", font=("Helvetica", 12, "bold"))
    submit_button.pack(pady=10)
    
    back_button = tk.Button(root, text="Back to Menu", command=main_menu, font=("Helvetica", 12, "bold"))
    back_button.pack(pady=10)

def dict_input_page():
    clear_screen()
    
    global dict_keys_entries, dict_values_entries
    
    label = tk.Label(root, text="Enter Dictionary Keys and Values", font=("Helvetica", 14, "bold"), bg="white")
    label.pack(pady=10)
    
    keys_label = tk.Label(root, text="Keys (one per box):", font=("Helvetica", 12), bg="white")
    keys_label.pack(pady=5)
    
    keys_frame = tk.Frame(root, bg="white")
    keys_frame.pack(pady=5)
    
    dict_keys_entries = []
    for _ in range(3):  # Start with 3 keys
        add_field(dict_keys_entries, keys_frame)
    
    add_key_button = tk.Button(root, text="Add Key", command=lambda: add_field(dict_keys_entries, keys_frame), font=("Helvetica", 12, "bold"))
    add_key_button.pack(pady=5)
    
    values_label = tk.Label(root, text="Values (one per box):", font=("Helvetica", 12), bg="white")
    values_label.pack(pady=5)
    
    values_frame = tk.Frame(root, bg="white")
    values_frame.pack(pady=5)
    
    dict_values_entries = []
    for _ in range(3):  # Start with 3 values
        add_field(dict_values_entries, values_frame)
    
    add_value_button = tk.Button(root, text="Add Value", command=lambda: add_field(dict_values_entries, values_frame), font=("Helvetica", 12, "bold"))
    add_value_button.pack(pady=5)
    
    submit_button = tk.Button(root, text="Generate Dictionary", font=("Helvetica", 12, "bold"))
    submit_button.pack(pady=10)
    
    back_button = tk.Button(root, text="Back to Menu", command=main_menu, font=("Helvetica", 12, "bold"))
    back_button.pack(pady=10)

def set_input_page():
    clear_screen()
    
    global set_entries
    
    label = tk.Label(root, text="Enter Set Items", font=("Helvetica", 14, "bold"), bg="white")
    label.pack(pady=10)
    
    items_label = tk.Label(root, text="Items (one per box):", font=("Helvetica", 12), bg="white")
    items_label.pack(pady=5)
    
    set_frame = tk.Frame(root, bg="white")
    set_frame.pack(pady=5)
    
    set_entries = []
    for _ in range(4):  # Start with 4 items
        add_field(set_entries, set_frame)
    
    add_item_button = tk.Button(root, text="Add Item", command=lambda: add_field(set_entries, set_frame), font=("Helvetica", 12, "bold"))
    add_item_button.pack(pady=5)
    
    submit_button = tk.Button(root, text="Generate Set", font=("Helvetica", 12, "bold"))
    submit_button.pack(pady=10)
    
    back_button = tk.Button(root, text="Back to Menu", command=main_menu, font=("Helvetica", 12, "bold"))
    back_button.pack(pady=10)

# Main menu
def main_menu():
    clear_screen()
    
    label = tk.Label(root, text="Python Code Generator", font=("Helvetica", 16, "bold"), bg="white")
    label.pack(pady=20)
    
    buttons = [
        ("Create Class", class_input_page),
        ("Create Function", function_input_page),
        ("Create Tuple", tuple_input_page),
        ("Create List", list_input_page),
        ("Create Dictionary", dict_input_page),
        ("Create Set", set_input_page)
    ]
    
    for text, command in buttons:
        button = tk.Button(root, text=text, command=command, font=("Helvetica", 12, "bold"), width=20)
        button.pack(pady=10)
    
    exit_button = tk.Button(root, text="Exit", command=root.quit, font=("Helvetica", 12, "bold"), width=20)
    exit_button.pack(pady=10)

# Initialize Tkinter window
root = tk.Tk()
root.title("Python Structure Generator")
root.geometry("400x600")
root.configure(bg="white")

# Start with the main menu
main_menu()

root.mainloop()
