print("*" * 20)
print("sets, dictionary, Type coversion, list of dictionary!!!!!")
print("*" * 20)
print("1. set opreations_____.")
print("*" * 20)

numbers = {1,2,3,4,5}
print(numbers)
print("type",(numbers))

# add

numbers.add(6)
print(numbers)

# remove

numbers.remove(3)
print(numbers)

# cheak

print("Is 2 present?" ,2 in numbers)

print("-*-" * 20)
print("2. Union , Intersection and diffrerence_____.")
print("-*-" * 20)
      
set_a = {1,2,3,4}
set_b = {3,4,5,6}

print(set_a)
print(set_b)

print("Union:", set_a.union(set_b))
print("Intersection:", set_a.intersection(set_b))
print("Difference:", set_a.difference(set_b))

print("*"*20)
print("3. Dictonary operations---")
print("*"*20)

student = {
    "name":"Aarohi",
    "age":20,
    "grade":"A"
    }
for keys in student.keys():
    print(f"{keys} : {student[keys]}")

student["city"] = "delhi"
print(student)

del student["grade"]
student["age"] = 21
print(student)

print("/"*20)
print("4. Dictinary from lists!!!!!")
print("/"*20)

keys = ['id' ,'name' ,'email']
values = [10002 ,'Aarohi' ,'aarohi23@gmail.com']
user = {}
for i in range(len(keys)):
    user[keys[i]] = values[i]
    print(user)

print("=" * 20)
print("5. Type Conversion")
print("=" * 20)

num = '123'

print(type(num))

nums = int(num)

print(type(nums))

list_1 = [1 , 2 , 3 , 4]

tuple_1 = tuple(list_1)

print(tuple_1)


pairs = [(1 , "A") , (2 , "B")]

print(dict(pairs))    
   
