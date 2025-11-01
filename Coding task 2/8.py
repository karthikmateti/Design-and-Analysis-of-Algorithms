def get_matrix_input(rows, cols):
    matrix = []
    print(f"Enter elements row-wise for a {rows}x{cols} matrix:")
    for i in range(rows):
        row = list(map(int, input().split()))
        while len(row) != cols:
            print(f"Please enter exactly {cols} elements.")
            row = list(map(int, input().split()))
        matrix.append(row)
    return matrix

def multiply_matrices(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    
    if cols_A != rows_B:
        return None  # Cannot multiply
    
    # Initialize result matrix with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result

# Input first matrix dimensions
r1 = int(input("Enter no of rows for first matrix: "))
c1 = int(input("Enter no of columns for first matrix: "))
A = get_matrix_input(r1, c1)

# Input second matrix dimensions
r2 = int(input("Enter no of rows for second matrix: "))
c2 = int(input("Enter no of columns for second matrix: "))
B = get_matrix_input(r2, c2)

if c1 != r2:
    print("Matrix multiplication not possible")
else:
    product = multiply_matrices(A, B)
    print("Product of the matrices:")
    for row in product:
        print(*row)
