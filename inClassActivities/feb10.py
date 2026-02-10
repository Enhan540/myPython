# printing out hi5 or hi2
'''
num = int(input("Type num: "))

if num % 5 == 0:
    print("High 5!")
elif num % 2 == 0:
    print("High 2!")
else:
    print(":(")
'''
# Random importing and checking numbers
'''
import random
num1 = random.randint(0, 9)
num2 = random.randint(0, 9)

if num1 < num2:
    # Swapping num1 and num2
    num1, num2 = num2, num1
answer = int(input(f"What is {num1} - {num2}? "))
print("You're correct!" if answer == num1 - num2 else "You're wrong.")
'''
'''
# Print depending on 3 and 5 divisibility
num = int(input("Give a num: "))
if num % 15 == 0:
    print("FizzBuzz")
elif num % 5 == 0:
    print("Buzz")
elif num % 3 == 0:
    print("Fizz")
else:
    print(num)
'''

# Leap year calculator
year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("not a leap year")
elif year % 4 == 0:
    print("leap year")
else:
    print("not a leap year")