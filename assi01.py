'''
Q 1 ->  Write a program that asks the user for their name and age, then prints a
sentence like:
"Hello [name], you are [age] years old."'
'''
a  = input("Enter your name: ")
b  = input("Enter your age: ")
print("Hello " + a + ", you are " + b + " years old.")


''' 
Q2 . -> take two numbers as input from the user and print their
 sum, difference,
product, and quotient'

'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
sum = a + b
defference = a - b
product = a * b
if b != 0:
    quotient = a / b
    
print("Sum: ", sum)
print("Difference: ", defference)
print("product:" ,   product)   


''' 
Q3 -->  ask the user to enter two integers and one float. Convert them all to floats
and print their average.'
'''
a = int(input("enter the first number"))
b = float(input("enter the secound number "))
c = float(a)
sum = a + c
print(sum)

'''
Qs -->4  The user enters a string containing a number (e.g.,"45" ). Convert it to
• an integer
• a float
• a string again
Print all three values with their types.'
 

'''

a = 45
s = int(a)
v = float(s)
d = str(v)
print(a)
print(s)
print(v)
print(d)
print(type(a))
print(type(s))
print(type(v))
print(type(d))
