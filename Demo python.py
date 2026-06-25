# Python basic
'''
# Print your name

print("My name is Archana!!!!")

# add tow number

a=5
b=10

sum = a+b

print(" the sum is :", sum)

# Ask user's name

name = input("what is your name:?")

print(name)

# simple calcutor

a = int(input("enter first number:"))
b = int(input("enter second number:"))

print("addition :", a+b)
print("subtraction :", a-b)
print("multipication :", a*b)
print("division :", a/b)

# print () formating using sep and end

print("apple","banana","papaya", sep ="|", end ="<____end of list\n")
'''
# formating massage from user input
'''
name = input("enter your name: ")
age = int(input("enter your age : "))
hobby = input("enter your favorite hobby :")

# f string method

print(f"hello, {name}! at{age}, enjoying{hobby} sounds fun !!!")

# declare variables of diffrent data type and show their type

a = 10
b = 3.5
c = "python"
d = "true"

print(a,"type :", type (a))
print(b,"type :", type (b))
print(c,"type :", type (c))
print(d,"type :", type (d))
'''
# Python program 1

subject1 = input("enter subject1 name: ")
marks1 = int(input("enter your marks: "))

subject2 = input("enter subject2 name: ")
marks2 = int(input("enter your marks: "))

subject3 = input("enter subject3 name: ")
marks3 = int(input("enter your marks: "))

# calculate total and average

total = marks1 + marks2 + marks3
average = total/3

# decide grade

if average >= 90:
    grade = "a"

elif average >= 75:
      grade = "b"

elif average >= 60:
      grade = "c"      

else :
    grade = "fail"

print("\n_____result_____")
print(f"{subject1} : {marks1}")
print(f"{subject2} : {marks2}")
print(f"{subject3} : {marks3}")
print(f"total marks : {total}")
print("average marks : {average}")
print(f"grade : {grade}")
