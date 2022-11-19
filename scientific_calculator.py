import math


def addition(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def exponent(x, y):
    return x ** y


def tan(x):
    return math.tan(x)


def sin(x):
    return math.sin(x)


def cos(x):
    return math.cos(x)


def factorial(x):
    return math.factorial(x)


def log(x):
    return math.log(x)


print \
    ("""press -
      "1 - Addition \n"
      "2 - subtraction \n"
      "3 - multiplication \n"
      "4 - division \n"
      "5 - exponent \n"
      "6 - tan (x) \n"
      "7 - sin (x) \n"
      "8 - cos (x)\n"
      "9 - factorial (x) \n"
      "10 - log (x) \n"
""")

o = input("")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if o == "1":
    num1 = int(input("1st number -"))
    num2 = int(input("2nd number -"))
    print(num1 +num2)
if o == "2":
    num1 = int(input("1st number -"))
    num2 = int(input("2nd number -"))
    print(num1 - num2)
if o == "3":
    num1 = int(input("1st number -"))
    num2= int(input("2nd number -"))
    print(num1 * num2)
if o == "4":
    if num2 == 0:
       print("You cannot divide by 0!")
       raise SystemExit
    print(num1, "/", num2, "=", divide(num1, num2))
if o == "5":
    num1 = int(input("1st number -"))
    num2 = int(input("2nd number -"))
    print(num1 ** num2)
if o == "6":
    num1 = int(input("enter value"))
    print(math.tan(num1))
if o == "7":
    num1= int(input("enter value"))
    print(math.sin(num1))
if o == "8":
    num1 = int(input("enter value"))
    print(math.cos(num1))
if o == "9":
    num1 = int(input("enter value"))
    print(math.factorial(num1))
if o == "10":
    num1 = int(input("enter value"))
    print(math.log(num1))
