# Control flow in python
'''
# 1 if statement

age = 20

if age >= 18:
    print("you are eligible to vote.")

# 2 if...else....statement

number = 6

if number >= 0:
  print("positive number")
else:
    print("negative number")
'''
# 3 if....elif....else
'''
marks = 40
if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else :
    print("Fail")
'''
# 4 Match statement

num1 = 20
num2 = 10

operator = input("enter your operator:")

match operator:
    case "+":
        print("Addision:", num1+num2)
    case "-":
        print("substration:", num1-num2)
    case "*":
        print("muiltipication:", num1*num2)
    case "/":
        print("division:", num1/num2)
    case _:
        print("invaild operator:")


# 5 mutiple value in one case use

char = "v"

match char:
    case "a"|"e"|"i"|"o"|"u":
        print("vowel")
    case _:
        print("consonents")
