# Python is an interpreted language
# The interpreter reads and executes code line by line
# Python code is executed by the Python Virtual Machine (PVM)
# Python uses indentation (commonly 4 spaces) to define code blocks

# Variable assignment
x = 10  # 'x' is a memory location that points to an object
# Python is Dynamically typed we don't need to declare the type of variable, but the object it stores does have a type

# Keywords are reserved words in Python and cannot be used as identifiers
# Python has 35 keywords

# Everything in python is a class
# Basic data types in Python
a = 5
print(type(a))  # <class 'int'>

b = 5.5
print(type(b))  # <class 'float'>

is_important = True
print(type(is_important))  # <class 'bool'>

fruit = "Mango"
print(type(fruit))  # <class 'str'>

# Type conversion
num = 10
print(type(num))

str_num = str(num)  # Explicit type conversion (int to string)
print(type(str_num))

# Arithmetic operation
add = a + b
print(add)
print(type(add))  # Implicit type conversion (int + float → float)

# Input and Output
name = input("Enter your name: ")
print(name)

number = int(input("Enter a number: "))  # Convert input string to integer
print(number)

# Function with a docstring
def func(my_name):
    """
    This function prints the name of the user.
    """
    print(f"Hello, my name is {my_name}")

# Accessing the function's docstring
print(func.__doc__)
# help(func)

# Function call
func("Bhavika")

# Arithmetic Operations
a1 = 3
b1 = 2
print(a1+b1)
print(a1-b1)
print(a1*b1)
print(a1/b1)
print(a1//b1)
print(a1%b1)
print(a1**b1)

#Math Functions
n = 2.957
print(round(n,2))

m = -1
print(abs(m))

# Floating precision
# Due to the way floating-point numbers are represented in binary, some decimal numbers cannot be represented exactly, leading to precision issues.
print(round(0.1 + 0.2, 2)) #0.3