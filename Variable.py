'''Q1
Theory
What is a variable in Python?
Q2
Theory
Do you need to declare the data type of a variable in Python? Why or why not?
Q3
Theory
Which of these are valid Python variable names? 2name, my_name, _name, my-name
Q4
Theory
What is the naming convention for variables in Python (e.g., myName vs my_name)?
Q5
Theory
Can a Python variable name start with a number? Give an example.
Q6
Code Output
What is the output?
x = 5
y = 3
print(x + y)
Q7
Code Output
What is the output?
name = "Alice"
print(name)
Q8
Code Output
What is the output?
x = 10
x = 20
print(x)
Q9
Code Output
What is the output?
a = b = c = 5
print(a, b, c)
Q10
Code Output
What is the output?
x, y = 3, 7
print(x)
print(y)
Q11
Theory
What does it mean that Python variables are "dynamically typed"?
Q12
Theory
What is the difference between a local and a global variable in Python?
Q13
Code Output
What is the output?
x = "hello"
x = 10
print(type(x))
Q14
Code Output
What is the output?
x = 5
print(type(x))
Q15
Theory
Are Python variable names case-sensitive? Is Name different from name?
Q16
Code Output
What is the output?
a = 10
b = a
a = 20
print(b)
Q17
Theory
What is a reserved keyword in Python? Can you use it as a variable name? Give 2 examples of reserved keywords.
Q18
Code Output
What is the output?
x = 100
del x
print(x)
Q19
Theory
What does the del keyword do to a variable?
Q20
Code Output
What is the output?
x = 5
y = x
print(x == y)
Medium — Q21 to Q40
Q21
Fix the Bug
Fix the error:
2myvar = 10
print(2myvar)
Q22
Code Output
What is the output?
x = 10
def fn():
    x = 20
    print(x)
fn()
print(x)
Q23
Fix the Bug
Fix the error:
class = "Python"
print(class)
Q24
Code Output
What is the output?
x = 5
def change():
    global x
    x = 99
change()
print(x)
Q25
Fix the Bug
Fix the error:
a, b = 1, 2, 3
print(a, b)
Q26
Code Output
What is the output?
x = "Python"
y = x
x = "Java"
print(y)
Q27
Fix the Bug
Fix the error (variable used before assignment):
print(score)
score = 100
Q28
Code Output
What is the output?
x = 10
y = 3
x, y = y, x
print(x, y)
Q29
Fix the Bug
Fix the error:
my var = 10
print(my var)
Q30
Code Output
What is the output?
a = 1
b = 2
c = a + b
a = 10
print(c)
Q31
Fix the Bug
Fix the error:
def add():
    total = a + b
a = 5
b = 3
add()
print(total)
Q32
Code Output
What is the output?
x = [1, 2, 3]
y = x
y.append(4)
print(x)
Q33
Fix the Bug
Fix the error so that the function modifies the global variable:
count = 0
def increment():
    count += 1
increment()
print(count)
Q34
Code Output
What is the output?
x = None
print(type(x))
Q35
Fix the Bug
Fix the error:
True = 1
print(True)
Q36
Code Output
What is the output?
x = 5
x += 3
x *= 2
print(x)
Q37
Fix the Bug
Fix the error:
for = 10
print(for)
Q38
Code Output
What is the output?
name = "John"
NAME = "Jane"
print(name, NAME)
Q39
Fix the Bug
Fix the error:
x = 10
y = "5"
print(x + y)
Q40
Code Output
What is the output?
a = 3
b = a
a += 1
print(a, b)
Hard — Q41 to Q50
Q41
Write Code
Write a program that swaps two variables a = 10 and b = 20 without using a third variable. Print both after swapping.
Q42
Write Code
Write a function that takes a number as argument, stores the square and cube in separate variables, and returns both.
Q43
Write Code
Create a program using global keyword — define a global counter, write a function that increments it 5 times, and print the final count.
Q44
Write Code
Write a program where you assign 5 different types of values to the same variable one by one and print the type of the variable each time.
Q45
Write Code
Write a program that takes user input and stores it in a variable. Then checks if the variable is empty ("") or not and prints a message accordingly.
Q46
Write Code
Explain with code why x = [1,2,3]; y = x; y.append(4) also changes x. Then fix it so x is not affected.
Q47
Write Code
Write a program that unpacks a list of 5 elements into 5 separate variables and prints each one with its variable name.
Q48
Write Code
Write a program using multiple assignment in one line to store the result of 3 different mathematical expressions.
Q49
Write Code
Write a program that demonstrates variable scope: show that a variable inside a function is NOT accessible outside it, and handle the error properly using try-except.
Q50
Write Code
Write a function safe_divide(a, b) that stores the result in a variable. If b is 0, store None instead and print a message. Test with both cases.'''