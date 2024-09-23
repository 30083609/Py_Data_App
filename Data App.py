import tkinter as tk
from tkinter import messagebox

# Function to clear the screen
def clear_screen():
    for widget in root.winfo_children():
        widget.pack_forget()

# Function to copy text to clipboard
def copy_to_clipboard(text):
    root.clipboard_clear()  # Clear the clipboard
    root.clipboard_append(text)  # Append the text to the clipboard
    messagebox.showinfo("Copied", "Code copied to clipboard!")

# Function to show the generated code
def show_generated_code(code):
    clear_screen()
    
    result_label = tk.Label(root, text="Generated Code:", font=("Verdana", 14, "bold"), bg="white")
    result_label.pack(pady=10)
    
    code_text = tk.Text(root, height=10, width=50)
    code_text.insert(tk.END, code)  # Display the code as-is
    code_text.pack(pady=10)
    
    copy_button = tk.Button(root, text="Copy to Clipboard", command=lambda: copy_to_clipboard(code), font=("Verdana", 12, "bold"))
    copy_button.pack(pady=10)
    
    back_button = tk.Button(root, text="Back to Menu", command=main_menu, font=("Helvetica", 12, "bold"))
    back_button.pack(pady=10)

# Function to add more fields dynamically with optional checkbox
def add_field(entries_list, parent_frame, checkbox_list=None):
    entry_frame = tk.Frame(parent_frame, bg="white")
    entry_frame.pack(pady=5)
    
    entry = tk.Entry(entry_frame)
    entry.pack(side=tk.LEFT, padx=5)
    entries_list.append(entry)
    
    if checkbox_list is not None:
        var = tk.IntVar()
        checkbox = tk.Checkbutton(entry_frame, text="Optional", variable=var, bg="white")
        checkbox.pack(side=tk.LEFT)
        checkbox_list.append(var)

# Input page for creating a class
def class_input_page():
    clear_screen()
    
    global class_name_entry, fields_entries
    
    label = tk.Label(root, text="Enter Class Information", font=("Verdana", 14, "bold"), bg="white")
    label.pack(pady=10)
    
    class_name_label = tk.Label(root, text="Class Name:", font=("Verdana", 12), bg="white")
    class_name_label.pack(pady=5)
    class_name_entry = tk.Entry(root)
    class_name_entry.pack(pady=5)
    
    fields_label = tk.Label(root, text="Fields (one per box):", font=("Verdana", 12), bg="white")
    fields_label.pack(pady=5)
    
    fields_frame = tk.Frame(root, bg="white")
    fields_frame.pack(pady=5)
    
    fields_entries = []
    for _ in range(4):  # Start with 4 fields
        add_field(fields_entries, fields_frame)
    
    add_field_button = tk.Button(root, text="Add Field", command=lambda: add_field(fields_entries, fields_frame), font=("Verdana", 12, "bold"))
    add_field_button.pack(pady=5)
    
    submit_button = tk.Button(root, text="Generate Class", command=generate_class, font=("Helvetica", 12, "bold"))
    submit_button.pack(pady=10)
    
    back_button = tk.Button(root, text="Back to Menu", command=main_menu, font=("Helvetica", 12, "bold"))
    back_button.pack(pady=10)

def generate_class():
    class_name = class_name_entry.get().strip()
    fields = [entry.get().strip() for entry in fields_entries if entry.get().strip()]
    
    class_code = f"class {class_name}:\n    \"\"\"\n    Class representing {class_name}.\n\n"
    class_code += "    Args:\n"
    for field in fields:
        class_code += f"        {field} (str): Description of {field}.\n"
    class_code += "    \"\"\"\n\n"
    
    class_code += f"    def __init__(self, {', '.join(fields)}):\n"
    for field in fields:
        class_code += f"        self.{field} = {field}\n"
    
    if not fields:
        class_code += "    pass\n"
    
    show_generated_code(class_code)

# Input page for creating a function
def function_input_page():
    clear_screen()
    
    global func_name_entry, params_entries, params_checkboxes, print_params_var
    
    label = tk.Label(root, text="Enter Function Information", font=("Verdana", 14, "bold"), bg="white")
    label.pack(pady=10)
    
    func_name_label = tk.Label(root, text="Function Name:", font=("Verdana", 12), bg="white")
    func_name_label.pack(pady=5)
    func_name_entry = tk.Entry(root)
    func_name_entry.pack(pady=5)
    
    params_label = tk.Label(root, text="Parameters (one per box):", font=("Verdana", 12), bg="white")
    params_label.pack(pady=5)
    
    params_frame = tk.Frame(root, bg="white")
    params_frame.pack(pady=5)
    
    params_entries = []
    params_checkboxes = []
    for _ in range(4):  # Start with 4 parameters
        add_field(params_entries, params_frame, params_checkboxes)
    
    add_param_button = tk.Button(root, text="Add Parameter", command=lambda: add_field(params_entries, params_frame, params_checkboxes), font=("Verdana", 12, "bold"))
    add_param_button.pack(pady=5)
    
    print_params_var = tk.IntVar()  # Variable to hold the checkbox state
    print_params_check = tk.Checkbutton(root, text="Print Greeting", variable=print_params_var, font=("Verdana", 12), bg="white")
    print_params_check.pack(pady=5)
    
    submit_button = tk.Button(root, text="Generate Function", command=generate_function, font=("Verdana", 12, "bold"))
    submit_button.pack(pady=10)
    
    back_button = tk.Button(root, text="Back to Menu", command=main_menu, font=("Helvetica", 12, "bold"))
    back_button.pack(pady=10)

def generate_function():
    func_name = func_name_entry.get().strip()
    params = [entry.get().strip() for entry in params_entries if entry.get().strip()]
    params_with_defaults = [
        f"{param}='default_value'" if checkbox.get() == 1 else param
        for param, checkbox in zip(params, params_checkboxes)
    ]
    
    func_code = f"def {func_name}({', '.join(params_with_defaults)}):\n"
    
    # Auto-generate docstring
    func_code += f"    \"\"\"\n    Function to {func_name}.\n\n"
    func_code += "    Args:\n"
    for param in params:
        func_code += f"        {param} (str): Description of {param}.\n"
    func_code += "    \"\"\"\n\n"
    
    if print_params_var.get() == 1 and len(params) >= 2:
        func_code += f"    print(f\"Hello, {{{params[0]}}}! You are {{{params[1]}}} years old.\")\n"
    
    func_code += "    # TODO: Add your logic here\n"
    
    show_generated_code(func_code)

# Input page for creating a tuple
def tuple_input_page():
    clear_screen()
    
    global tuple_entries
    
    label = tk.Label(root, text="Enter Tuple Values", font=("Verdana", 14, "bold"), bg="white")
    label.pack(pady=10)
    
    values_label = tk.Label(root, text="Values (one per box):", font=("Verdana", 12), bg="white")
    values_label.pack(pady=5)
    
    tuple_frame = tk.Frame(root, bg="white")
    tuple_frame.pack(pady=5)
    
    tuple_entries = []
    for _ in range(4):  # Start with 4 values
        add_field(tuple_entries, tuple_frame)
    
    add_value_button = tk.Button(root, text="Add Value", command=lambda: add_field(tuple_entries, tuple_frame), font=("Verdana", 12, "bold"))
    add_value_button.pack(pady=5)
    
    submit_button = tk.Button(root, text="Generate Tuple", command=generate_tuple, font=("Verdana", 12, "bold"))
    submit_button.pack(pady=10)
    
    back_button = tk.Button(root, text="Back to Menu", command=main_menu, font=("Verdana", 12, "bold"))
    back_button.pack(pady=10)

def generate_tuple():
    values = [entry.get().strip().lower() for entry in tuple_entries if entry.get().strip()]
    
    tuple_code = f"my_tuple = ({', '.join(values)})\n"
    
    show_generated_code(tuple_code)

# Input page for creating a list
def list_input_page():
    clear_screen()
    
    global list_name_entry, list_entries
    
    label = tk.Label(root, text="Enter List Information", font=("Verdana", 14, "bold"), bg="white")
    label.pack(pady=10)
    
    list_name_label = tk.Label(root, text="List Name:", font=("Verdana", 12), bg="white")
    list_name_label.pack(pady=5)
    list_name_entry = tk.Entry(root)
    list_name_entry.pack(pady=5)
    
    items_label = tk.Label(root, text="Items (one per box):", font=("Verdana", 12), bg="white")
    items_label.pack(pady=5)
    
    list_frame = tk.Frame(root, bg="white")
    list_frame.pack(pady=5)
    
    list_entries = []
    for _ in range(4):  # Start with 4 items
        add_field(list_entries, list_frame)
    
    add_item_button = tk.Button(root, text="Add Item", command=lambda: add_field(list_entries, list_frame), font=("Verdana", 12, "bold"))
    add_item_button.pack(pady=5)
    
    submit_button = tk.Button(root, text="Generate List", command=generate_list, font=("Verdana", 12, "bold"))
    submit_button.pack(pady=10)
    
    back_button = tk.Button(root, text="Back to Menu", command=main_menu, font=("Verdana", 12, "bold"))
    back_button.pack(pady=10)

def generate_list():
    list_name = list_name_entry.get().strip()
    items = [entry.get().strip().lower() for entry in list_entries if entry.get().strip()]
    
    list_code = f"{list_name} = [{', '.join(items)}]\n"
    
    show_generated_code(list_code)

# Input page for creating a dictionary
def dict_input_page():
    clear_screen()
    
    global dict_name_entry, dict_keys_entries, dict_values_entries
    
    label = tk.Label(root, text="Enter Dictionary Information", font=("Verdana", 14, "bold"), bg="white")
    label.pack(pady=10)
    
    dict_name_label = tk.Label(root, text="Dictionary Name:", font=("Verdana", 12), bg="white")
    dict_name_label.pack(pady=5)
    dict_name_entry = tk.Entry(root)
    dict_name_entry.pack(pady=5)
    
    keys_label = tk.Label(root, text="Keys (one per box):", font=("Verdana", 12), bg="white")
    keys_label.pack(pady=5)
    
    keys_frame = tk.Frame(root, bg="white")
    keys_frame.pack(pady=5)
    
    dict_keys_entries = []
    for _ in range(3):  # Start with 3 keys
        add_field(dict_keys_entries, keys_frame)
    
    add_key_button = tk.Button(root, text="Add Key", command=lambda: add_field(dict_keys_entries, keys_frame), font=("Helvetica", 12, "bold"))
    add_key_button.pack(pady=5)
    
    values_label = tk.Label(root, text="Values (one per box):", font=("Verdana", 12), bg="white")
    values_label.pack(pady=5)
    
    values_frame = tk.Frame(root, bg="white")
    values_frame.pack(pady=5)
    
    dict_values_entries = []
    for _ in range(3):  # Start with 3 values
        add_field(dict_values_entries, values_frame)
    
    add_value_button = tk.Button(root, text="Add Value", command=lambda: add_field(dict_values_entries, values_frame), font=("Helvetica", 12, "bold"))
    add_value_button.pack(pady=5)
    
    submit_button = tk.Button(root, text="Generate Dictionary", command=generate_dict, font=("Helvetica", 12, "bold"))
    submit_button.pack(pady=10)
    
    back_button = tk.Button(root, text="Back to Menu", command=main_menu, font=("Helvetica", 12, "bold"))
    back_button.pack(pady=10)

def generate_dict():
    dict_name = dict_name_entry.get().strip()
    keys = [entry.get().strip().lower() for entry in dict_keys_entries if entry.get().strip()]
    values = [entry.get().strip() for entry in dict_values_entries if entry.get().strip()]
    
    if len(keys) != len(values):
        messagebox.showerror("Error", "Keys and values must be equal in number!")
        return
    
    dict_code = f"{dict_name} = {{{', '.join(f'{k}: {v}' for k, v in zip(keys, values))}}}\n"
    
    show_generated_code(dict_code)

# Input page for creating a set
def set_input_page():
    clear_screen()
    
    global set_name_entry, set_entries
    
    label = tk.Label(root, text="Enter Set Information", font=("Verdana", 14, "bold"), bg="white")
    label.pack(pady=10)
    
    set_name_label = tk.Label(root, text="Set Name:", font=("Verdana", 12), bg="white")
    set_name_label.pack(pady=5)
    set_name_entry = tk.Entry(root)
    set_name_entry.pack(pady=5)
    
    items_label = tk.Label(root, text="Items (one per box):", font=("Verdana", 12), bg="white")
    items_label.pack(pady=5)
    
    set_frame = tk.Frame(root, bg="white")
    set_frame.pack(pady=5)
    
    set_entries = []
    for _ in range(4):  # Start with 4 items
        add_field(set_entries, set_frame)
    
    add_item_button = tk.Button(root, text="Add Item", command=lambda: add_field(set_entries, set_frame), font=("Helvetica", 12, "bold"))
    add_item_button.pack(pady=5)
    
    submit_button = tk.Button(root, text="Generate Set", command=generate_set, font=("Verdana", 12, "bold"))
    submit_button.pack(pady=10)
    
    back_button = tk.Button(root, text="Back to Menu", command=main_menu, font=("Verdana", 12, "bold"))
    back_button.pack(pady=10)

def generate_set():
    set_name = set_name_entry.get().strip()
    items = [entry.get().strip().lower() for entry in set_entries if entry.get().strip()]
    
    set_code = f"{set_name} = {{{', '.join(items)}}}\n"
    
    show_generated_code(set_code)

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
