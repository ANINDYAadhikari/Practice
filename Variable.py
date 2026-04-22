# Q1 What is a variable in Python? 
'''ANS = variable is used for to store data of code block.'''

# Q2 Do you need to declare the data type of a variable in Python? Why or why not?  
'''ANS = It depends on the situation, 
        if we want to know what type of data we have used then we can print data type in the print statement.'''

# Q3 Which of these are valid Python variable names? 2name, my_name, _name, my-name
'''ANS = my_name, _name'''

# Q4 What is the naming convention for variables in Python (e.g., myName vs my_name)?
'''ANS = Variable naming follows the snake_case convention, 
         where words are lowercase and separated by underscores'''

# Q5 Can a Python variable name start with a number? Give an example.
'''ANS = No a Python variable name can't start with a number'''

# Q6 What is the output? = 8
'''
x = 5
y = 3
print(x + y)
'''

# Q7 What is the output?
'''
name = "Alice"
print(name)
'''

# Q8 What is the output? = 20
'''
x = 10
x = 20
print(x)
'''

# Q9 What is the output? = 5
'''
a = b = c = 5
print(a, b, c)
'''

# Q10 What is the output? = 3 7 
'''
x, y = 3, 7
print(x)
print(y)
'''

# Q11 What does it mean that Python variables are "dynamically typed"?
'''ANS = Variables are dynamically typed means that the interpreter determines the data type of a variable at runtime
'''

# Q12 What is the difference between a local and a global variable in Python?
'''ANS = We can call a local variable only in a specified block of code but in other hands, 
         we can call the global variable from any where in the code'''

# Q13 What is the output? = int
'''
x = "hello"
x = 10
print(type(x))
'''

# Q14 What is the output? = int
'''
x = 5
print(type(x))
'''

# Q15 Are Python variable names case-sensitive? Is Name different from name?
'''ANS = Yes, Python variable names are case-sensitive. Definietaly Name is different from name.
'''

# Q16 What is the output? = 10
'''
a = 10
b = a
a = 20
print(b)
'''

# Q17 What is a reserved keyword in Python? Can you use it as a variable name? Give 2 examples of reserved keywords.
'''ANS = A reserved keyword in Python is a word that has a special, predefined meaning and is part of the language's syntax and structure.
        No we can't use it as a variable name.
        if, for'''

# Q18 What is the output? = No Output
'''
x = 100
del x
print(x)
'''

# Q19 What does the del keyword do to a variable?
'''ANS = del keyword delets a variable'''

# Q20 What is the output? = True
'''
x = 5
y = x
print(x == y)
'''

# Q21 Fix the error:
'''
2myvar = 10
print(2myvar) #Wrong
'''
'''
myvar = 10
print(myvar) #Correct
'''

# Q22 What is the output? = 20 , 10
'''
x = 10
def fn():
    x = 20
    print(x)
fn()
print(x)
'''

# Q23 Fix the error:
'''
class = "Python"
print(class)
'''
# We can't use class as a var name, cause it is a reserved keyword in python.

# Q24 What is the output? = 99
'''
x = 5
def change():
    global x
    x = 99
change()
print(x)
'''

# Q25 Fix the error:
'''
a, b = 1, 2, 3
print(a, b) #Wrong
'''
'''
a, b, c = 1, 2, 3
print(a, b, c) #Correct
'''

# Q26 What is the output? = Python
'''
x = "Python"
y = x
x = "Java"
print(y)
'''

# Q27 Fix the error:
'''
print(score)
score = 100 #Wrong
'''
'''
score = 100
print(score) #Correct
'''

# Q28 What is the output? = 3, 10
'''
x = 10
y = 3
x, y = y, x
print(x, y)
'''

# Q29 Fix the error:
'''
my var = 10
print(my var) #Wrong
'''
'''
my_var = 10
print(my_var) #Correct
'''

# Q30 What is the output? = 3
'''
a = 1
b = 2
c = a + b
a = 10
print(c)
'''

# Q31 Fix the error:
'''
def add():
    total = a + b
a = 5
b = 3
add()
print(total)  #Wrong
'''
'''
def add():
    a = 5
    b = 3
    return a + b

total = add()
print(total)  #Correct
'''

# Q32 What is the output? = [1, 2, 3, 4]
'''
x = [1, 2, 3]
y = x
y.append(4)
print(x)
'''

# Q33 Fix the error so that the function modifies the global variable:
'''
count = 0
def increment():
    count += 1
increment()
print(count) #Wrong
'''
'''
count = 0
def increment():
    global count
    count += 1
increment()
print(count) #Correct
'''

# Q34 What is the output? = str
'''
x = None
print(type(x))
'''

# Q35 Fix the error:
'''
True = 1
print(True)
'''
'''
var = 1
print(var)
'''
# We can't use True as a variable name, cause it is a reserved keyword in python.

# Q36 What is the output? = 16
'''
x = 5
x += 3
x *= 2
print(x)
'''

# Q37 Fix the error:
'''
for = 10
print(for) #Wrong
'''
'''
var = 10
print(var) #Correct
'''

# Q38 What is the output? John Jane
'''
name = "John"
NAME = "Jane"
print(name, NAME)
'''

# Q39 Fix the error:
'''
x = 10
y = "5"
print(x + y) #Wrong
'''
'''
x = 10
y = 5
print(x + y) #Correct
'''

# Q40 What is the output? 16 /n
#                        4   3
'''
a = 3
b = a
a += 1
print(a, b)
'''

# Q41 Write a program that swaps two variables a = 10 and b = 20 without using a third variable. Print both after swapping.
'''
a = 10
b = 20
# Swapping without third variable
a = a + b
b = a - b
a = a - b
print("After swapping:")
print("a =", a)
print("b =", b)
'''

# Q42 Write a function that takes a number as argument, stores the square and cube in separate variables, and returns both.
# Function definition
'''
def square_and_cube(num):
    square = num ** 2
    cube = num ** 3
    return square, cube

number = int(input("Enter a number: "))
sq, cb = square_and_cube(number)
print("Square:", sq)
print("Cube:", cb)
'''

# Q43 Create a program using global keyword — define a global counter, write a function that increments it 5 times, and print the final count.
'''
counter = 0
def increment_counter():
    global counter   # Access the global variable
    for i in range(5):
        counter += 1
increment_counter()
print("Final counter value:", counter)
'''

# Q44 Write a program where you assign 5 different types of values to the same variable one by one and print the type of the variable each time.
'''
x = 10
print(x, "->", type(x))
x = 3.14
print(x, "->", type(x))
x = "Hello"
print(x, "->", type(x))
x = True
print(x, "->", type(x))
x = [1, 2, 3]
print(x, "->", type(x))
'''

# Q45 Write a program that takes user input and stores it in a variable. Then checks if the variable is empty ("") or not and prints a message accordingly.
'''
user_input = input("Enter something: ")
if user_input == "":
    print("The variable is empty.")
else:
    print("The variable is not empty.")
'''

# Q46 Explain with code why x = [1,2,3]; y = x; y.append(4) also changes x. Then fix it so x is not affected.
'''
x = [1, 2, 3]
y = x          # Both x and y point to the SAME list
y.append(4)
print("x:", x)
print("y:", y)
'''

# Q47 Write a program that unpacks a list of 5 elements into 5 separate variables and prints each one with its variable name.
'''
lst = [10, 20, 30, 40, 50]
a, b, c, d, e = lst
print("a =", a)
print("b =", b)
print("c =", c)
print("d =", d)
print("e =", e)
'''

# Q48 Write a program using multiple assignment in one line to store the result of 3 different mathematical expressions.
'''
a, b, c = 10 + 5, 20 * 2, 30 - 10

print("a =", a)
print("b =", b)
print("c =", c)
'''

# Q49 Write a program that demonstrates variable scope: show that a variable inside a function is NOT accessible outside it, and handle the error properly using try-except.
'''
def my_function():
    x = 100   # Local variable
    print("Inside function, x =", x)
my_function()
# Trying to access x outside
try:
    print("Outside function, x =", x)
except NameError:
    print("Error: x is not accessible outside the function")
'''

# Q50 Write a function safe_divide(a, b) that stores the result in a variable. If b is 0, store None instead and print a message. Test with both cases.
'''
def safe_divide(a, b):
    if b == 0:
        result = None
        print("Cannot divide by zero")
    else:
        result = a / b
    return result
# Test cases
print("Result 1:", safe_divide(10, 2))  # normal case
print("Result 2:", safe_divide(10, 0))  # division by zero
'''