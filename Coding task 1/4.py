n = int(input("Enter size of matrix (n): "))   # take size of square matrix
matrix = []
print("Enter the matrix elements row-wise:")
for i in range(n):
    row = list(map(int, input().split()))   # take each row as input
    matrix.append(row)
i = int(input("Enter row number (i): ")) 
j = int(input("Enter column number (j): "))
try:
    print("Value at position (", i, ",", j, ") is:", matrix[i-1][j-1])   # print element at (i,j)
except IndexError:
    print("Error.")  # invalid input
