# DAY 1 -- 30/03/2026

# what is indentation ?
if(5 > 2):
    print("five is bigger than two")
print("hii")


# what is case-sensitive ?
'''print("hiii") # THIS IS CORRECT 
PRINT("hiii") # THIS IS WRONG '''


# what is comment line ? and type of comment line ?
# hashtag denotes single line comment 
'''three columns denotes
 multi line comments'''


# what is variable ?
a = 5
print(a)


# How to check what type of variable ?
x = 5
y = "Anindya"
z = 0.5
print(type(x))
print(type(y))
print(type(z))


x = str(5)
print(x)
print(type(x))


# how to asssign multi values in a single var ?
x, y, z = "11", "Anindya", "0.11"
print(x, y, z)


# one value to single var
x = y = z = 11
print(x, y, z)


# DAY 2 -- 02/04/2026

# What is Data Type ? Types of data type :--
'''    Text Type - str, char
    Numeric type - Int, Float, Complex
    Sequence type - List, Tuple, Range
    Mapping type - Dict / Dictionary
    Set type - Set, Frozen set 
    Boolean type - bool '''

# Example of data types :- 
'''    str/char = "Anindya"
    int = 11
    float = 1.1
    complex = 1A
    List = ["Anindya", "Adhikari"]
    Tuple = ("Anindya", "Adhikari")
    Range = range(11)
    Dict = {"Anindya", "Adhikari"}
    Set = {"Anindya", "Adhikari"}
    Frozen set = frozenset({"Anindya", "Adhikari"})
    Boolean = True/False'''
    

# String Slicing 
# What is String Slicing ? 

# Print First two letter 
x = "abcdefghijk"
print(x[:2])
# Print Middle two letter
x = "abcdefghijk"
print(x[4:6])
# Print Last two letter
x = "abcdefghijk"
print(x[-2:])



