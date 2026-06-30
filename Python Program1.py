# 1. variables & basic input program

# Store and print name, age, and city

name = "Archana"
age = 18
city = "surat"

print(name)
print(age)
print(city)

# Take user input and display formatted output

name = input("Enter your name: ")
age=int(input("Enter your age: "))
city=input("Enter your city: ")

print(f"My name is {name},and i am {age} years old!,and i am from{city}")

# Swap two variables

a = 10
b = 20

a,b=b,a

print("a=",a)
print("b=",b)

# Find square and cube of a number

x=10

x*=x
print("square = ",x)

y=20

y=y**3
print("cube = ",y)


# Convert temperature (Celsius → Fahrenheit)

celsius = float(input("enter temperature in celsius: "))
fahrenheit = (celsius ** 9/5) +32

print("Fahrenheit = ", fahrenheit)


# 2. Arithmetic Operators

# Simple calculator (+,-,*,/)

a = 10
b = 20

print("addition:", a+b)
print("substraction:", a-b)
print("multipication:", a*b)
print("division:", a/b)

# fIND REMAINDER USING %

a=10
b=5

mod=a%b

print("modulas=",mod)


# calculate area of rectangle/circle

a=float(input("enter a lenth/redious : "))
b=float(input("enter a wight :"))

rec_area=a*b
print("rectangle area is = ",rec_area)


cir_area=3.14*a
print("circle area is = ",cir_area)


# Calculate simple interest

p=float(input("Enter a principal amount : "))
r=float(input("Enter a rate amount : "))
t=float(input("Enter a time : "))

si=p*r*t/100

print("simple interest is = ",si)


#3. Comparison Operators

#Check greater number between two inputs

num1=int(input("Enter a num1 : "))
num2=int(input("Enter a num2 : "))

print(num1>num2)

#Check if number is equal or not

a=10
b=10

print(a==b)

#Voting eligibility (age ≥ 18) 

age=int(input("Enter your age : "))

print(age>=18)

# Find largest of 3 numbers

a=10
b=20
c=30

largest=max(a,b,c)
print("The largest num is = ",largest)

#Cheke pass or fail
marks=int(input("Enter a marks"))

if marks >= 45:
    print("pass")

else :
    print("fail")


#4. Logical Operators 

#Check if number is between 1–100

num=int(input("Enter a num : " ))
if num>=1 and num<=100:
    print("your num is between 1 to 100 ")
else:
    print("your num is not between 1 to 100")

#2. Login system (username + password)

user=input("Enter a username : ")
pasw=int(input("Enter a password : "))

if user=="admin" and pasw == 123:
    print("chack in ")
else:
    print("Invalide your password and username")

#Check leap year (multiple conditions)




#Check if number is divisible by 3 AND 5

num=int(input("Enter a num : "))

if num/3 and num/5:
    print("your num is divide by both")
else:
    print("your num is not divide by both ")

#Validate input (age > 18 AND city == "Surat")

age=int(input("Enter your age : "))
city=input("Enter your city : ")

if age>18 and city=="surat":
    print("Vaild data")
else:
    print("Unvalide data")


#5. Assignment Operators

#Increment and decrement a number

num=int(input("Enter a num : "))
num2=int(input("Enter a num2 :"))

num+=num2

print("num is =",num)

num2-=num

print("num2 is =",num2)


#Use +=, -=, *= in calculations

num=int(input("Enter a number : "))

num+=num

print(num)

num*=num

print(num)

num-=num

print(num)

#Create running total (add numbers step by step) 

num=int(input("Enter a num : "))


num+=num
num+=num
num+=num

print(num)

#Salary increment calculation

salary=int(input("Enter your salary : "))
increment=float(input("Enter a increment salary : "))

new_salary=salary+(salary*(increment/100))

print("new salary = ",new_salary)

#Discount calculation using assignment operators

price=int(input("Enter your price : "))

dis_price=float(input("Enter your disscount price : "))

total_price=price-price*(dis_price/100)

print("total_price is = ",total_price)

#6. Mixed Practice 

#Student marks → calculate total & average

marks1=int(input("Enter your marks1 : "))
marks2=int(input("Enter your marks2 : "))
marks3=int(input("Enter your marks3 : "))

total=marks1+marks2+marks3
average=total/3

print("ttal = ",total)
print("average = ",average)

#Bill generator (price + tax)

price1=float(input("Enter a first thing price : "))
price2=float(input("Enter a secound thing price : "))
price3=float(input("Enter a third thing price : "))
tax=float(input("Enter a tax : "))

total_price=price1+price2+price3
tax=total_price*(tax/100)

bill_price = total_price+tax

print("bill price is = ",bill_price)

#Age calculator (current year - birth year)

current_year=float(input("Enter current year : "))
birth_year=float(input("Enter your birth year : "))

age=current_year-birth_year

print(f"you are {age} years old!")


# Even/Odd + positive/negative check 

num = int(input("Enter a number: "))

if num%2 == 0:
    print("Even")
else:
    print("Odd")

if num>0:
    print("Positive")
else:
    print("Negative")


#Mini calculator with all operators
num1=int(input("Enter a num1 : "))
num2=int(input("Enter a num2 : "))
operator = input("enter operator (+,-,*,/,%) : ")

match operator:
    case  "+":
        print("addition = ",num1+num2)
    case  "-":
        print("substaction = ",num1-num2)
    case  "*":
        print("multification = ",num1*num2)
    case  "/":
        print("division = ",num1/num2)
    case  "%":
        print("modulas = ",num1%num2)
    case _:
        print("invalid operator")




