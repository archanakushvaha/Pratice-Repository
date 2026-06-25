# 1. variables & basic input program

# Store and print name, age, and city

name = "Archana"
age = 18
city = "surat"

print(name)
print(age)
print(city)

# Take user input and display formatted output

name = input("enter your name:")
print("Hello", name)

# Swap two variables

a = 10
b = 20

sum = a + b

print("The sum is:", sum)

# Find square and cube of a number

 # Get number from the user and convert it to an integer
num = int(input("Enter a number: "))

# Calculate square and cube using the ** operator
square = num ** 2
cube = num ** 3

#  the results using f-strings
print(f"Square of {num} is: {square}")
print(f"Cube of {num} is: {cube}")

# Convert temperature (Celsius → Fahrenheit)

celsius = float(input("enter temperature in celsius: "))
fahrenheit = (celsius ** 9/5) +25

print(f"{celsius}°C = {fahrenheit}°f")



