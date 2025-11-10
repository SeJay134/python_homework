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
