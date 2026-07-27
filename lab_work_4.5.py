# Create a 2D array in 3*3 matrix.
'''
matrix = []

for i in range(3):
    rows = list(map(int , input(f"Enter rows {i + 1} : ").split()))

    matrix.append(rows)

print("matrix : ")

for rows in matrix:
    for value in rows:
        print(value , end="\t")


    print()

print(matrix)

print(matrix[0][0])
'''

# Transpose of 2*3 matrix
'''
matrix = []

for i in range(5):
    rows = list(map(int , input(f"Entre rows {i + 1} : ").split()))

    matrix.append(rows)

print(matrix)

transpose = []
for j in range(3):
    temp = []
    for i in range(2):
        temp.append(matrix[i][j])
    transpose.append(temp)
print(rows)
'''

# Sum all matrix value

rows = int(input("Enter number of rows:"))
cols = int(input("Enter number of columns:"))

matrix = []

for i in range(rows):
    
    row = list(map(int , input(f"Enter Row {i + 1} :").split()))

    matrix.append(row)

print(matrix)

total = 0

for row in matrix:
    for value in row:
        total += value

print(total)

'''
rows = int(input("Enter Number of rows:"))
cols = int(input("Enter Number of columns:"))

matrix = []

for i in range(rows):

    row = list(map(int , input(f"Enter Row {i + 1} :").split()))

    if len(row) == cols:
        matrix.append(row)
        break

    else:
        print("Please Enter exactly values.")
    
    matrix.append(row)
        
print(matrix)

total = 0

for row in matrix:
    for value in row:
        total += value

print(total)
'''


