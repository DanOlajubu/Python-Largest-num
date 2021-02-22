#Project 4 - Create a program to find the largest number from the given numbers
#Like before - need user input
#Can use some IF, ELIF & ELSE statements
#Can use some comparison operators

num1 = int(input("What is the first number?: "))
num2 = int(input("What is the second number?: "))
num3 = int(input("What is the third number?: "))
num4 = int(input("What is the fourth number?: "))

if (num1 > num2) and (num1 > num3) and (num1 > num4):
    largest = num1
elif (num2 > num1) and (num2 > num2) and (num2 > num4):
    largest = num2
elif (num3 > num1) and (num3 > num2) and (num3 > num4):
    largest = num3
else:
    largest = num4

print("The largest number is ", largest)
