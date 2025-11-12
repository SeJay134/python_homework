"""
Task 1: Hello
Write a hello function that takes no arguments and returns Hello!.  
Now, what matters here is what the function returns.  
You can print() whatever you want for debugging purposes, but the tests ignore that, 
and only check the return value.
"""
def hello():
    return "Hello!"

print(hello())

"""
Task 2: Greet with a Formatted String
Write a greet function.  It takes one argument, a name, and returns Hello, Name!.  
Use a formatted string.  Note that you have to return exactly the right string or the test 
fails -- but PyTest tells you what didn't match.
"""
def greet(name):
    return f"Hello, " + name + "!"

print(greet("James"))

"""
Task 3: Calculator
Write a calc function. It takes three arguments. The default value for the third argument is "multiply". 
The first two arguments are values that are to be combined using the operation requested by the third argument, 
a string that is one of the following add, subtract, multiply, divide, modulo, int_divide (for integer division) 
and power. The function returns the result.
Error handling: When the function is called, it could ask you to divide by 0. That will throw an exception: 
Which one? You can find out by triggering the exception in your program or in the Python Interactive Shell. 
Wrap the code within the calc function in a try block, and put in an except statement for this exception. 
If the exception occurs, return the string "You can't divide by 0!".
More error handling: When the function is called, the parameters that are passed might not work for 
the operation. For example, you can't multiply two strings. Find out which exception occurs, catch it, 
and return the string "You can't multiply those values!".
Here's a tip. You have to do different things for add, multiply, divide and so on. So you can do 
a conditional cascade, if/elif/elif/else. That's perfectly valid. But you might want to use 
the match-case Python statement instead. Look it up! It just improves code appearance.
Again, as you complete each function, you run the test to see whether everything is correct.
"""
def calc(num1, num2, value = "multiply"):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        return "You can't multiply those values!"
    if value == "multiply":
        return num1 * num2 # 30
    elif value == "add":
        return num1 + num2 # 11
    elif value == "divide":
        try:
            result = num1 / num2
        except ZeroDivisionError:
            return "You can't divide by 0!"
        else:
            return result
        
    elif value == "int_divide":
        try:
            result = num1 // num2
        except ZeroDivisionError:
            return "You can't divide by 0!"
        else:
            return result
        
    elif value == "modulo": # 4
        return num1 % num2
    elif value == "subtract":
        return num1 - num2 # 8.2
    else:
        return "You can't do it!"
    
print(calc(5, 6, value = "multiply")) # 30
print(calc(5, 6, value = "add")) # 11
print(calc(20, 5, value = "divide"))
print(calc(12.6, 4.4, value = "subtract")) # 8.2
print(calc(9, 5, value = "modulo")) # 4
print(calc(10, 0, value = "divide")) # can't divide by 0
print(calc("first", "second", value = "multiply")) # can't multiply words

"""
Task 4: Data Type Conversion
Create a function called data_type_conversion. It takes two parameters, the value and the name of 
the data type requested, one of float, str, or int. Return the converted value.
Error handling: The function might be called with a bad parameter. For example, the caller might 
try to convert the string "nonsense" to a float. Catch the error that occurs in this case. If this error 
occurs, return the string You can't convert {value} into a {type}., except you use the value and data 
type that are passed as parameters -- so again you use a formatted string.
"""
def data_type_conversion(value, data_type): # float, str, int
    if data_type == "int":
        try:
            return int(value)
        except ValueError:
            return f"You can't convert {value} into a {data_type}."
    elif data_type == "float":
        try:
            return float(value)
        except ValueError:
            return f"You can't convert {value} into a {data_type}."
    elif data_type == "str":
        try:
            return str(value)
        except ValueError:
            return f"You can't convert {value} into a {data_type}."
        
print(data_type_conversion("110", "int"))
print(data_type_conversion("5.5", "float"))
print(data_type_conversion(7,"float"))
print(data_type_conversion(91.1,"str"))
print(data_type_conversion("banana", "int")) # "You can't convert banana into a int."
    

