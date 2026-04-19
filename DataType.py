Q1
Theory
What are the 4 most common built-in data types in Python?
Q2
Theory
What is the difference between int and float in Python?
Q3
Theory
What data type does "Hello" belong to in Python?
Q4
Theory
What are the only two values a bool (boolean) can have in Python?
Q5
Theory
What is the difference between a list and a tuple in Python?
Q6
Code Output
What is the output?
x = 3.14
print(type(x))
Q7
Code Output
What is the output?
x = True
print(type(x))
Q8
Code Output
What is the output?
x = [1, 2, 3]
print(type(x))
Q9
Code Output
What is the output?
x = (1, 2, 3)
print(type(x))
Q10
Code Output
What is the output?
x = {"name": "Alice", "age": 25}
print(type(x))
Q11
Theory
What does type() function do in Python?
Q12
Theory
What is type casting? Give an example of converting a string to an integer.
Q13
Code Output
What is the output?
x = int("42")
print(x + 8)
Q14
Code Output
What is the output?
x = str(100)
print(type(x))
Q15
Theory
What is None in Python? Which data type does it belong to?
Q16
Code Output
What is the output?
print(int(3.9))
Q17
Theory
What is the difference between list and set in Python?
Q18
Code Output
What is the output?
x = {1, 2, 2, 3}
print(x)
Q19
Theory
Are Python strings mutable or immutable? What does that mean?
Q20
Code Output
What is the output?
x = float("3.14")
print(x + 1)
Medium — Q21 to Q40
Q21
Fix the Bug
Fix the error:
x = "10"
y = 5
print(x + y)
Q22
Code Output
What is the output?
x = True
y = False
print(x + y)
Q23
Fix the Bug
Fix the error:
t = (1, 2, 3)
t[0] = 10
print(t)
Q24
Code Output
What is the output?
d = {"a": 1, "b": 2}
print(d["a"])
Q25
Fix the Bug
Fix the error:
x = int("hello")
print(x)
Q26
Code Output
What is the output?
x = [1, 2, 3]
x.append(4)
print(len(x))
Q27
Fix the Bug
Fix the error:
x = "5.5"
print(int(x))
Q28
Code Output
What is the output?
a = [1, 2]
b = [3, 4]
print(a + b)
Q29
Fix the Bug
Fix the error (duplicate key):
d = {"a": 1, "a": 2, "b": 3}
print(d["a"])
Q30
Code Output
What is the output?
s = "hello"
print(s[1])
Q31
Fix the Bug
Fix the error:
x = {1, 2, 3}
x[0] = 10
print(x)
Q32
Code Output
What is the output?
x = bool(0)
y = bool(1)
print(x, y)
Q33
Fix the Bug
Fix the error:
x = [1, 2, 3]
x.add(4)
print(x)
Q34
Code Output
What is the output?
x = "hello"
print(x.upper())
Q35
Fix the Bug
Fix the error:
d = {"key": "value"}
print(d["keys"])
Q36
Code Output
What is the output?
x = None
print(x == None)
print(x is None)
Q37
Fix the Bug
Fix the error (concatenating int to string):
age = 25
print("My age is " + age)
Q38
Code Output
What is the output?
x = [1, [2, 3], 4]
print(x[1][0])
Q39
Fix the Bug
Fix the error:
x = (1, 2, 3)
x.append(4)
print(x)
Q40
Code Output
What is the output?
x = {"a": 1}
x["b"] = 2
print(x)
Hard — Q41 to Q50
Q41
Write Code
Write a program that takes a list of mixed types (int, str, float, bool) and prints the type of each element.
Q42
Write Code
Write a function that accepts any value and returns "number", "text", "collection", or "other" based on its type.
Q43
Write Code
Write a program that converts a list to a set to remove duplicates, then converts it back to a list and prints it sorted.
Q44
Write Code
Write a program that stores student data (name, age, grade) in a dictionary and prints each key-value pair using a loop.
Q45
Write Code
Write a function safe_cast(value, target_type) that tries to cast a value to a given type and returns None if it fails (use try-except).
Q46
Write Code
Write a program that demonstrates the immutability of strings — try to change one character, show the error, then show the correct way using string methods.
Q47
Write Code
Create a nested dictionary representing 2 students with their name, age, and marks. Write a loop to print all details.
Q48
Write Code
Write a program that takes a list of numbers and separates them into two lists: one for int and one for float. Print both lists.
Q49
Write Code
Write a program that merges two dictionaries into one. If a key exists in both, keep the value from the second dictionary.
Q50
Write Code
Write a program that uses all 5 data types (int, float, str, list, dict) in a meaningful way — for example, a mini student record system that stores and displays info.