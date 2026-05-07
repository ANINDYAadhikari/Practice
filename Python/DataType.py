# Q1 What are the 4 most common built-in data types in Python?
'''
int
float
str
boolean
'''

# Q2 What is the difference between int and float in Python?
'''
int denotes whole number. While float denotes floating numbers.
int ex. = 11
float ex. = 0.8
'''
# Q3 What data type does "Hello" belong to in Python?
'''
string(str)
'''

# Q4 What are the only two values a bool (boolean) can have in Python?
'''
True, False
'''

# Q5 What is the difference between a list and a tuple in Python?

# Q6 What is the output? = float
'''
x = 3.14
print(type(x))
'''

# Q7 What is the output? = Bool (Boolean)
'''
x = True
print(type(x))
'''

# Q8 What is the output? = list
'''
x = [1, 2, 3]
print(type(x))
'''
# Q9 What is the output? = tuple
'''
x = (1, 2, 3)
print(type(x))
'''
# Q10 What is the output? = dict (dictionary)
'''
x = {"name": "Alice", "age": 25}
print(type(x))
'''
# Q11 What does type() function do in Python?
'''
type() functions print the type of data we are using.
ex.
var = 11
print(type(var))
'''

# Q12 What is type casting? Give an example of converting a string to an integer.
'''
type casting is a method where we can change any data type into another data type. 
ex. 
# Original values
s = "10"     # string
i = 5        # integer
f = 3.5      # float
# Type casting
x = int(s)       # string → int
y = float(i)     # int → float
z = str(f)       # float → string
b = bool(0)      # int → bool
# Printing results with types
print(x, type(x))
print(y, type(y))
print(z, type(z))
print(b, type(b))
'''

# Q13 What is the output? = 50
'''
x = int("42")
print(x + 8)
'''

# Q14 What is the output?
'''
x = str(100)
print(type(x))
'''
# Q15 What is None in Python? Which data type does it belong to?
'''
when a variable has no data assigned or a function does not return anything.
ex. 
x = None
print(x)
print(type(x))
'''

# Q16 What is the output?
'''
print(int(3.9))
'''
# Q17 What is the difference between list and set in Python?
'''
list is ordered and set is unordered.
list allows duplicate and set doesn't allows deplicate.
ex.
# List
lst = [1, 2, 2, 3]
print("List:", lst)

# Set
st = {1, 2, 2, 3}
print("Set:", st)
'''

# Q18 What is the output?
'''
x = {1, 2, 2, 3}
print(x)
'''
# Q19 Are Python strings mutable or immutable? What does that mean?
'''
Strings are immutable, meaning their values cannot be changed after they are created.
'''

# Q20 What is the output?
'''
x = float("3.14")
print(x + 1)
'''

# Q21 Fix the error:

'''x = "10"
y = 5
print(x + y) # Wrong
'''
'''
x = 10
y = 5
print(x + y) # Correct
'''

# Q22 What is the output? = 1
'''
x = True
y = False
print(x + y)
'''

# Q23 Fix the error: 
'''
t = (1, 2, 3)
t[0] = 10
print(t) # Wrong  # tiple is immutable it's can't be changed after creation
'''
'''
t = (1, 2, 3)
print(t) # Correct
'''

# Q24 What is the output?
'''
d = {"a": 1, "b": 2}
print(d["a"])
'''

# Q25 Fix the error:
'''
x = int("hello")
print(x) # Wrong
'''
'''
x = "hello"
print(x) # Correct
'''

# Q26 What is the output? = length of list is 4 
'''
x = [1, 2, 3]
x.append(4)
print(len(x))
'''

# Q27 Fix the error:
'''
x = "5.5"
print(int(x)) # Wrong
'''
'''
x = 5.5
print(int(x)) # Correct
'''

# Q28 What is the output? = [1, 2, 3, 4]
'''
a = [1, 2]
b = [3, 4]
print(a + b)
'''

# Q29 Fix the error (duplicate key):
'''
d = {"a": 1, "a": 2, "b": 3}
print(d["a"]) # Wrong
'''
'''
d = {"a": 1, "a1": 2, "b": 3}
print(d["a"]) # Correct
'''

# Q30 What is the output? = e
'''
s = "hello"
print(s[1])
'''

# Q31 Fix the error:  # Set is not mutable
'''
x = {1, 2, 3}
x[0] = 10
print(x) # Wrong
'''
'''
x = {1, 2, 3}
print(x) # Correct 
'''

# Q32 What is the output? = False, True 
# In bool(boolean) 0 denotes False and 1 denotes True
'''
x = bool(0)
y = bool(1)
print(x, y)
'''

# Q33 Fix the error:
'''
x = [1, 2, 3]
x.add(4)
print(x) #Wrong 
'''
'''
x = [1, 2, 3]
x.append(4)
print(x) # Correct
'''

# Q34 What is the output? = HELLO
'''
x = "hello"
print(x.upper())
'''

# Q35 Fix the error:
'''
d = {"key": "value"}
print(d["keys"]) #Wrong
'''
'''
d = {"key" : "value"}
print(d["key"]) #Correct
'''

# Q36 What is the output? = True
# X is none so next two statements supports the first variable logic
'''
x = None
print(x == None)
print(x is None)
'''

# Q37 Fix the error (concatenating int to string):
'''
age = 22
print("My age is " + age)
'''
'''
age = 22
print("My age is ", age)
'''

# Q38 What is the output? = 2
'''
x = [1, [2, 3], 4]
print(x[1][0])  # Gets 2 from the inner list
'''

# Q39 Fix the error: #Tuple is not mutable
'''
x = (1, 2, 3)
x.append(4)
print(x) #Wrong
'''
'''
x = (1, 2, 3)
print(x) #Correct
'''

# Q40 What is the output? = {'a': 1, 'b': 2}
'''
x = {"a": 1}  # creates a new dict 
x["b"] = 2    # adding a new key and value pair into that dict
print(x)
'''

# Q41 Write a program that takes a list of mixed types (int, str, float, bool) and prints the type of each element.
'''
var = [11, "Hii", 0.8, True]
for item in var:
    print(item, "->", type(item))  # Print value and it's items
'''

# Q42 Write a function that accepts any value and returns "number", "text", "collection", or "other" based on its type.
'''
def check_type(value):
    if isinstance(value, (int, float)):
        return "number"
    elif isinstance(value, str):
        return "text"
    elif isinstance(value, (list, tuple, set, dict)):
        return "collection"
    else:
        return "other"
# Test examples
print(check_type(10))        # number
print(check_type("Hello"))   # text
print(check_type([1, 2]))    # collection
print(check_type(True))      # other
'''

# Q43 Write a program that converts a list to a set to remove duplicates, then converts it back to a list and prints it sorted.

'''
# Original list with duplicates
lst = [5, 2, 3, 2, 1, 5, 4]
unique_set = set(lst) # Convert list → set (removes duplicates)
new_list = list(unique_set) # Convert set → list
new_list.sort() # Sort the list
print("Sorted list without duplicates:", new_list)
'''

# Q44 Write a program that stores student data (name, age, grade) in a dictionary and prints each key-value pair using a loop.
'''
student = {
    "name": "Anindya",
    "age" : 22,
    "grade": "A"
}
# Loop through dictionary and print key-value pairs
for key, value in student.items():
    print(key, ":", value)
'''

# Q45 Write a function safe_cast(value, target_type) that tries to cast a value to a given type and returns None if it fails (use try-except).
'''
def safe_cast(value, target_type):
    try:
        result = target_type(value)
    except:
        result = None
    return result
# Test cases
print(safe_cast("100", int))     # valid
print(safe_cast("abc", int))     # invalid
print(safe_cast("3.5", float))   # valid
print(safe_cast("hello", int))   # invalid
'''

# Q46 Write a program that demonstrates the immutability of strings — try to change one character, show the error, then show the correct way using string methods.
'''
s = "hello"
# Trying to change a character (will cause error)
try:
    s[0] = 'H'
except TypeError as e:
    print("Error:", e)

# Correct way: create a new string
s = "hello"
new_s = s.replace('h', 'H')
print("Original string:", s)
print("Modified string:", new_s)
'''

# Q47 Create a nested dictionary representing 2 students with their name, age, and marks. Write a loop to print all details.
'''
nested_dict = {
    "student1": {
        "Name": "Anamika Pal",
        "Age": 22,
        "Marks": 99
    },
    "student2": {
        "Name": "Anindya Adhikari",
        "Age": 22,
        "Marks": 96
    }
}
for student, details in nested_dict.items():
    print(student)

    for key, value in details.items():
        print(key, ":", value)
'''

# Q48 Write a program that takes a list of numbers and separates them into two lists: one for int and one for float. Print both lists.
'''
numbers = [1, 2.5, 3, 4.7, 5, 6.0]
int_list = []
float_list = []
for num in numbers:
    if isinstance(num, int):
        int_list.append(num)
    else:
        float_list.append(num)
print("Integers:", int_list)
print("Floats:", float_list)
'''

# Q49 Write a program that merges two dictionaries into one. If a key exists in both, keep the value from the second dictionary.
'''
# Two dictionaries
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
# Merge dictionaries
d1.update(d2)
print("Merged dictionary:", d1)
'''

# Q50 Write a program that uses all 5 data types (int, float, str, list, dict) in a meaningful way — for example, a mini student record system that stores and displays info.
'''
name = "Anindya"              # str
age = 22                      # int
marks = 85.5                  # float
subjects = ["Algorithm", "Python", "Science"]   # list
student = {                 # dict
    "Name": name,
    "Age": age,
    "Marks": marks,
    "Subjects": subjects
}
# Display student record
print("Student Record")

for key, value in student.items():
    print(key, ":", value)
'''