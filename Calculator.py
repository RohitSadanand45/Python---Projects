# Calculator using Python ~ MINI PROJECT

import math
#addition
def add(x,y):
    return x+y
#Subtraction
def subtract(x,y):
    return x-y
#Multiplication
def multiply(x,y):
    return x*y
#Division
def divide(x,y):
    if y == 0:
        return "Error! Division by zero."
    return x/y
#Modules
def mod(x,y):
    return x%y
#Floor Division
def floor(x,y):
    return x//y
#Power 
def pow(x,y):
    return x**y

while True:
    print("\n ===== Simple Calculator=====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modules")
    print("6. Floor Division")
    print("7. Power")
    print("8. Exit")

    choice = input("Enter your choice (1/2/3/4/5/6/7/8):")

    if choice == '8':
        print("Exiting Calculator...")
        break

    if choice in ('1','2','3','4','5','6','7'):
        num1 = float(input("Enter your First number:"))
        num2 = float(input("Enter your Second number:"))

        if choice == '1':
            print("Result:", add(num1,num2))
        elif choice == '2':
            print("Result:",subtract(num1,num2))
        elif choice == '3':
            print("Result:", multiply(num1,num2))
        elif choice == '4':
            print("Result:", divide(num1,num2))
        elif choice == '5':
            print("Result:",mod(num1,num2))
        elif choice == '6':
            print("Result:",floor(num1,num2))
        elif choice == '7':
            print("Result:",pow(num1,num2))
        else:
            print("Invalid input! Please try again.")
