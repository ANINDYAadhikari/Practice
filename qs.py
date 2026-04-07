'''#write a program to check numbers positive, negative, or zero.
num = int(input("write a number :"))
if num > 0:
    print("entered number is positive")
elif num < 0:
    print("entered number is negetive")
else:
    ("entered number is zero")'''



#Even Numbers
#Use a for loop to print all even numbers from 1 to 20.
for i in range (1,21):
    if (i % 2 ==0):
        print(i)


#Simple Sum
#Take two numbers as input and print their sum.
a = int(input("Enter the first number :"))
b = int(input("Enter the second number :"))
print("Sum of two numbers is :",a + b)


#Counting Letters
#Ask the user to input a word and print the number of characters in it.
word = input("Enter a word :")
length = len(word)
print("Number of charecter is :", length)


#Print all odd numbers from 1 to 50 using a loop.
for i in range (1,51):
    if (i % 2 != 0):
        print(i)

    
#Ask the user for a number n and print the sum of numbers from 1 to n.
num = int(input("enter a number :"))
sum = 0
for i in range (1, num+1):
    sum = sum + i
print (sum)


#Print the squares of numbers from 1 to 10.
for i in range (1,11):
    print(i ** 2)


#Take three numbers as input and print the largest one.
a = int(input("enter a number :"))
b = int(input("enter a number :"))
c = int(input("enter a number :"))
d = int(input("enter a number :"))
if (a>b and a>c and a>d):
    print("this number is largest" , a)
elif (b>a and b>c and b>d):
    print("This number is largest" , b)
elif (c>a and c>b and c>d):
    print("This number is largest" , c)
else:
    print("This number is largest" , d)


#Ask the user to enter a word and print it in reverse order.
word = input("enter a word :")
reverse = ""
for letter in word:
    reverse = letter + reverse
print("Reversed word :", reverse)



#Write a program that asks for a number and prints its factorial.
number=int(input("Enter a number :"))
fact = 1 
for i in range (1,number + 1):
    fact = fact * i
print("factorial of the number is :", fact)



#Take a word as input and print the number of vowels it contains.
word = input("Enter a word :")
count = 0
for letter in word:
    if letter.lower() in 'aeiou':
        count = count + 1
print("Number of vowels in the word is:", count)



'''a = int(input("Enter a number :"))
b = int(input("Enter second number :"))
sum = a+b
print(sum)'''

'''if(5>2):
    print("true")
else:
    print("false")'''

dict = {"name" : "joyjit",
        "car" : "TATA",
        "Daru" : "oldmonk",
        "Khabar" : "Chicken"}
x = dict["name"]
print(x)