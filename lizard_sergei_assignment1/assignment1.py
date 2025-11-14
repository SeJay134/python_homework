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
    
"""
Task 5: Grading System, Using *args
Create a grade function. It should collect an arbitrary number of parameters, compute the average, 
and return the grade. based on the following scale:
A: 90 and above
B: 80-89
C: 70-79
D: 60-69
F: Below 60
When you use *args you get access to a variable named args in your function, which is a tuple, 
an ordered collection of values like a list. You'll learn more about tuples and lists in the next lesson. 
There are some helpful functions you can use at this point: sum(args), len(args), and so on. 
One of the curiosities of Python is that these are not methods of any class. They are just standalone functions.
Handle the error that occurs if the parameters are nonsense. Return the string "Invalid data was provided." 
in this case. (Typically, you don't handle every possible exception in your error handling, except if 
the values in the parameters comes from the end user.)
"""
def grade(*args):
    try:
        if all(isinstance(x, (int, float)) for x in args):
            res = sum(args)/len(args)
            if res >= 90:
                return "A"
            elif res >= 80:
                return "B"
            elif res >= 70:
                return "C"
            elif res >= 60:
                return "D"
            else:
                return "F"
        else:
            return "Invalid data was provided."
    except ValueError:
        return "Invalid data was provided."

print(grade(75, 85, 95))
print(grade("three", "blind", "mice"))

"""
Task 6: Use a For Loop with a Range
Create a function called repeat. It takes two parameters, a string and a count, and returns a new string that 
is the old one repeated count times.
You can get the test to pass by just returning string * count. That would produce the correct return value. 
But, for this task, do it using a for loop and a range.
"""
def repeat(data_string, data_count):
    res = ""
    for x in range(data_count):
        res += data_string
    return res
print(repeat("up,", 4)) # "up,up,up,up,"

"""
Task 7: Student Scores, Using **kwargs
Create a function called student_scores. It takes one positional parameter and an arbitrary 
number of keyword parameters. The positional parameter is either "best" or "mean". If it is "best", 
the name of the student with the higest score is returned. If it is "mean", the average score is returned.
As you are using **kwargs, your function can access a variable named kwargs, which is a dict. The next lesson 
explains about dicts. What you need to know now is the following:
A dict is a collection of key value pairs.
You can iterate through the dict as follows:
for key, value in kwargs.items():
You can also get kwargs.keys() and kwargs.values().
The arbitrary list of keyword arguments uses the names of students as the keywords and their test score as 
the value for each.
"""
def student_scores(pos_param, **kwargs):
    for key, value in kwargs.items():
        if pos_param == "mean":
            return sum(kwargs.values())/len(kwargs)
        elif pos_param == "best":
            x = max(kwargs, key=lambda k: kwargs[k])
            return x
        
print(student_scores("mean", Tom=75, Dick=89, Angela=91))
print(student_scores("best", Tom=75, Dick=89, Angela=91, Frank=50))

"""
Task 8: Titleize, with String and List Operations
Create a function called titleize. It accepts one parameter, a string. The function returns a new string, 
where the parameter string is capitalized as if it were a book title.
The rules for title capitalization are: 
(1) The first word is always capitalized. 
(2) The last word is always capitalized. 
(3) All the other words are capitalized, except little words. 
For the purposes of this task, the little words are "a", "on", "an", "the", "of", "and", "is", and "in".
The following string methods may be helpful: split(), join(), and capitalize(). Look 'em up.
The split() method returns a list. You might store this in the words variable. words[-1] gives the last element 
in the list.
The in comparison operator: You have seen in used in loops. But it can also be used for comparisons, for example 
to check to see if a substring occurs in a string, or a value occurs in a list.
A new trick: As you loop through the words in the words list, it is helpful to have the index of the word for 
each iteration. You can access that index using the enumerate() function:
for i, word in enumerate(words):
"""
def titleize(stringi):
    small_words = ["a", "an", "the", "of", "and", "is", "in"]
    words = stringi.split()
    for index, word in enumerate(words):
        if index == 0:
            words[index] = word.capitalize()
        elif index == len(words) - 1:
            words[index] = word.capitalize()
        else:
            if word in small_words:
                words[index] = word
            else:
                words[index] = word.capitalize()
            
    return ' '.join(words)

print(titleize("war and peace")) # "War and Peace"
print(titleize("a separate peace")) # "A Separate Peace"
print(titleize("after on")) # "After On"