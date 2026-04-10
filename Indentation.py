# Q1 What is indentation in Python?
'''Indentation refers to correct amount of spaces between code lines'''

# Q2 How many spaces are recommended for one level of indentation in Python?
'''For one level of identation one space is recomended'''

# Q3 Does Python use curly braces {} to define code blocks? Explain what it uses instead.
'''No, python don't uses curly braces to define code block. It uses colon and indentation to define code block'''

# Q4 What error does Python throw when indentation is wrong?
'''Indentation error'''

# Q5 Can you mix tabs and spaces for indentation in Python 3? What happens if you do?
'''No we can't. Mixing them within the same block of code is strictly disallowed and will cause your program to fail. '''

# Q6 What is the output?  = Hello World
'''if True:
    print("Hello")
print("World")'''

# Q7 What is the output? = Big Number
'''x = 10
if x > 5:
    print("Big")
    print("Number")'''

# Q8 What is the output? = 0 1 2
'''for i in range(3):
    print(i)'''

# Q9 What is the output? = three done
'''x = 3
if x == 3:
    print("three")
print("done")'''

# Q10 What is the output? = Hi
'''def greet():
    print("Hi")
greet()'''

# Q11 Is indentation only required inside if statements, or also inside loops and functions?
'''No, Indentation needs in loops and functions same as if statements'''

# Q12 What does it mean when we say Python is "indentation-sensitive"?
'''This means python strictly maintains the rule of spacing between code lines'''

# Q13 Will this code run without error? = No, it will give and Indentation Error
'''if True:
    print("A")
  print("B")'''

# Q14 What is the output? = 
'''for i in range(2):
    print("Loop")
print("End")'''

# Q15 What keyword marks the beginning of an indented block in Python?
''': colon'''

# Q16 What is the output? = Hello World
'''def say():
    print("Hello")
    print("World")
say()'''

# Q17 In Python, what character ends a line that starts a new indented block (e.g., after if, for, def)?
''': colon'''
# Q18 What is the output? = 
'''x = 0
while x < 2:
    print(x)
    x += 1'''

# Q19 True or False: In Python, a code block ends when the indentation level goes back to the previous level.
'''True'''

# Q20 What is the output? = Yes
'''if 5 > 2:
    print("Yes")'''

# Q21 Fix the indentation error:
'''
def add(a, b):
return a + b
''' #Wrong 
'''
def add(a, b):
    return a + b
''' # Correct

# Q22 What is the output? = Found 2 
'''
for i in range(3):
    if i == 2:
        print("Found", i)
'''

# Q23 Fix the error:
'''
x = 10
if x > 5:
print("Greater")
else:
    print("Smaller")
''' # Wrong
'''x = 10 
if x > 5:
    print("Greater")
else: print("Smaller")
''' #Correct

# Q24 What is the output? = Not Positive
'''
def check(n):
    if n > 0:
        print("Positive")
    else:
        print("Not positive")
check(-1)
'''

# Q25 Fix the error:
'''
for i in range(3):
    print(i)
  print("done") # Wrong
'''
'''
for i in range(3):
    print(i)
print("done") # Correct
'''
# Q26 What is the output? = outer, inner
'''
def outer():
    print("outer")
    def inner():
        print("inner")
    inner()
outer()
'''

# Q27 Fix the error:
'''
if True:
    print("Line 1")
        print("Line 2") # Wrong
'''
'''
if True:
    print("Line 1")
print("Line 2") # Correct
'''

# Q28 What is the output? = 
'''
x = 5
if x > 3:
    if x > 4:
        print("greater than 4")
'''

# Q29 Fix the error:
'''
while True: 
print("running")
break  # Wrong
'''
'''
while True: 
print("running")
break  # Correct
'''

# Q30 What is the output? = 
'''0 0
0 1
1 0
1 1
2 0
2 1'''
'''
for i in range(3):
    for j in range(2):
        print(i, j)
'''

# Q31 Fix the error:
'''
def greet(name):
    print("Hello")
  print(name) # Wrong
'''
'''
def greet(name):
    print("Hello")
  print(name) # Correct
'''

# Q32 What is the output? = ten
'''
def test():
    x = 10
    if x == 10:
        print("ten")
test()
'''

# Q33 Fix the error:
'''
for i in range(5):
    if i % 2 == 0:
    print(i) # Wrong
'''
'''
for i in range(5):
    if i % 2 == 0:
     print(i) # Correct
'''

# Q34 What is the output? = 0, 1, 2
'''
def run():
    for i in range(3):
        print(i)
run()
'''

# Q35 Fix the error:
'''
try:
    x = 1/0
    except ZeroDivisionError:
    print("Error") # Wrong
'''
'''
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Error") # Correct
'''

# Q36 What is the output? = one , small, done
'''
x = 1
if x == 1:
    print("one")
    if x < 5:
        print("small")
print("done")
'''

# Q37 Fix the error:
'''
class Dog:
def bark(self):
    print("Woof") # Wrong
'''
'''
class Dog:
 def bark(self):
    print("Woof") # Correct
'''
# Q38 What is the output? = after
'''
def fn():
    pass
fn()
print("after")
'''

# Q39 Fix the error:
'''
for i in range(3):
    print(i)
        print(i * 2) # Wrong
'''
'''
for i in range(3):
    print(i)
    print(i * 2) # Correct
'''

# Q40 What is the output? = A
'''
x = 10
if x > 5:
    print("A")
elif x > 3:
    print("B")
else:
    print("C")
'''

'''
Q41

Write a function is_even(n) that prints "Even" if n is even, "Odd" otherwise. Use proper indentation.
Q42

Write a nested loop that prints a 3x3 grid of * using proper indentation.
Q43

Write a while loop that counts from 1 to 5 and prints each number. Use correct indentation.
Q44

Write a function that takes a list of numbers and prints only the positive ones. Use a for loop and if with correct indentation.
Q45

Write a function with a nested if-elif-else inside a for loop that classifies numbers 1–10 as "low" (1–3), "mid" (4–7), or "high" (8–10).
Q46

Write a try-except block that tries to divide two numbers and catches ZeroDivisionError. Use correct indentation.
Q47

Write a class Animal with a method speak() that prints "I am an animal". Create an object and call the method. Use proper indentation.
Q48

Write a function print_table(n) that prints the multiplication table of n from 1 to 10 using a for loop. Proper indentation required.
Q49

Write a recursive function countdown(n) that counts down from n to 0 and prints each number. Use proper indentation.
Q50

Write a function that takes a 2D list (list of lists) and prints each element using nested loops. Use correct indentation at every level.'''