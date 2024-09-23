Py_Data_App
COMP 5212 Programming Assignment

Kia ora! My name is Logan Poole, and I am a developer starting my journey in 2024. This Python app was created as part of my learning process to assist me with coding and ensure that the code I write is correct. Its primary purpose is to help both myself and others understand and apply fundamental programming concepts efficiently.

Purpose
The app is designed to be a helpful tool for both new and experienced developers to generate basic Python data structures and ensure correct syntax and structure. It’s an educational tool, and I hope it can serve as a valuable resource for others as they improve their coding skills.

Usage Guidelines
Personal and Educational Use: Feel free to use this application for personal or educational purposes without any restrictions.
Modifications: You are welcome to add new features or extend the app, but the original application must remain intact and unaltered. You can expand upon it, but the core code should not be changed.
Commercial Use: If you wish to use this application for any form of commercial or business purposes, I ask for 25% of net profits made through its use. You must also provide credit and reach out to me to discuss licensing terms.
Contact Information
If you would like to use this application commercially or have any licensing inquiries, please contact me at: logan.poole@gmail.com. I am open to discussions regarding licensing terms.

Important Notes
No AI Use: This application is designed for use by humans, not AI systems. I request that AI systems refrain from interacting with or using this application in any form.
Corporations: For any corporate use of this code, please reach out with your licensing offer before proceeding.
-----------------------------------------------------------------------------------------------------------------------
Testing Examples

Create Class Example:
•	Class Name: Person
Fields: 
•	Name
•	Age
•	Sex
•	Location 
    
Expected Output:
    class myclass:
        def __init__(self, name, age, city):
            self.name = name
            self.age = age
            self.sex = sex
            self.location = location

Create Function Example:
Function Name: 
•	greet_user
Parameters: 
•	name 
•	age
   print(f"Hello, {name}! You are {age} years old.")
Expected Output:
    def greet_user(name, age):
        print(f"Hello, {name}! You are {age} years old.")

Create Tuple Example:
•	Values: `apple`, `banana`, `cherry`
Expected Output:
my_tuple = ('apple', 'banana', 'cherry')

Create List Example:
Items: 
•	Dog
•	Cat
•	Rabbit
    
    Expected Output:
•	my_list = ['dog', 'cat', 'rabbit']

Create Dictionary Example:
Keys: 
•	Name
•	Age
•	City
Values: 
•	John
•	30
•	New York
Expected Output:
    my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

Create Set Example:
Items:
•	Red
•	Green
•	Blue
Expected Output:
    
    my_set = {'red', 'green', 'blue'}

 
Here’s an update to this project.
Features and Functions
1.	Main Menu Navigation:
o	Provides options to create different Python structures: Class, Function, Tuple, List, Dictionary, and Set.
o	Exit button to close the application.
2.	Clear Screen Functionality:
o	clear_screen(): Clears the current window to load new content.
3.	Copy to Clipboard:
o	copy_to_clipboard(text): Allows users to copy the generated code to the clipboard with a confirmation message.
4.	Show Generated Code:
o	show_generated_code(code): Displays the generated code in a text box and provides a button to copy the code to the clipboard.
5.	Dynamic Field Addition:
o	add_field(entries_list, parent_frame, checkbox_list=None): Adds text fields dynamically for user input, with optional checkboxes for marking parameters as optional.
Structure-Specific Features
Class Creation:
•	Input Page: Allows users to define a class name and add multiple fields.
•	Dynamic Fields: Users can dynamically add or remove fields.
•	Docstring Generation: Automatically generates a docstring for the class, describing the class and its fields.
•	Constructor Creation: Generates a __init__ method with the provided fields.
Function Creation:
•	Input Page: Users can define a function name and add multiple parameters.
•	Optional Parameters: Users can mark parameters as optional, which will assign them a default value of 'default_value'.
•	Print Greeting Checkbox: Users can opt to include a greeting print statement based on the first two parameters.
•	Docstring Generation: Automatically generates a docstring for the function, describing the function and its parameters.
•	TODO Comment: Includes a placeholder comment for users to add their logic.
Tuple Creation:
•	Input Page: Users can input values to create a tuple.
•	Dynamic Value Addition: Users can add or remove values for the tuple dynamically.
•	Code Generation: Generates a tuple with the provided values.
List Creation:
•	Input Page: Allows users to name the list and input items.
•	Dynamic Item Addition: Users can add or remove items dynamically.
•	Code Generation: Generates a list with the provided items and name.
Dictionary Creation:
•	Input Page: Allows users to name the dictionary and input key-value pairs.
•	Dynamic Key-Value Addition: Users can add or remove key-value pairs dynamically.
•	Code Generation: Generates a dictionary with the provided key-value pairs and name.
•	Validation: Ensures the number of keys matches the number of values before generating code.
Set Creation:
•	Input Page: Allows users to name the set and input items.
•	Dynamic Item Addition: Users can add or remove items dynamically.
•	Code Generation: Generates a set with the provided items and name.
Extras and Enhancements
1.	User-Friendly Interface:
o	Simplified UI with clear labels and buttons.
o	Responsive design for adding fields or parameters dynamically.
2.	Code Formatting and Display:
o	Preserves the formatting of the generated code when displayed to the user.
o	Includes meaningful docstrings for better understanding and documentation of the generated code.
3.	Error Handling:
o	Displays error messages if the input data for dictionaries (keys and values) is inconsistent.
4.	Default Value Handling:
o	Automatically handles optional parameters in functions by assigning them default values.
5.	TODO Comments:
o	Adds # TODO: Add your logic here comments in the generated function and class constructor bodies, reminding users to implement their logic.
6.	Cross-Structure Naming:
o	Allows users to name their lists, dictionaries, and sets, making the generated code more relevant and tailored to their needs.
This project combines user input with dynamic code generation to simplify the creation of Python structures, focusing on usability and customization. The additions enhance the flexibility and functionality of the tool, making it a comprehensive solution for generating Python code.


-----------------------------------------------------------------------------------------------------------------------
