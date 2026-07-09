# Basic Patterns in python
#1. patterns(without space pattern)
'''
size = 5
for i in range(size):
    for j in range(size):
        print("*" ,end="")
    print()
'''
#2. Right-Angled Triangle patterns
'''
size = 5
for i in range(1,size + 1):
    for j in range(i):
        print("*" ,end="")
    print()
'''
#3. Invested Right Angled tringle pattern
'''
size = 5
for i in range(size , 0 , -1):
    for j in range(i):
        print("*" ,end="")
    print()

'''

# Diamond pattern
'''
rows = 5

for i in range(1 , rows + 1):
    print("  " * (rows - i) , end="")

    if i == 1:
        print("*")
    else:
        print("*" + "  " * (2 * i - 3) + "*")
        
for i in range(rows - 1 , 0 , -1):
        print("  " * (rows - i)  , end="")
        if i == 1:
            print("*")
        else:
            print("*" + "  " * (2 * i - 3) + "*")

'''        
    
