import random

low = int(input("Enter the lower range number:  "))
high = int(input("Enter the higher range number: "))

num = random.randint(low, high)
#the f in theprint statement basically is like the & in C ...it appends the value of the curly braces
print(f"Your random number is {num}")