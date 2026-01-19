matrix_a = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix_b = [
    [7, 8],
    [9, 10],
    [11, 12]
]


def fill_matrix(matrix):
    n = int(input("n: "))
    m = int(input("m: "))

    for i in range(n):
        matrix.append([])
        for j in range(m):
            value = int(input(f"{i + 1}-{j + 1}: "))
            matrix[i].append(value)


def print_matrix(name, matrix):
    print(f"\n{name}: ")
    for row in matrix:
        print(row)

    print(end="\n")


#
# fill_matrix(matrix_a)
print_matrix("matrix_a", matrix_a)
#
# fill_matrix(matrix_b)
print_matrix("matrix_b", matrix_b)


def mult(A, B):
    # Check if multiplication is possible
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in A must equal number of rows in B")

    # Create result matrix filled with zeros
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    # Perform multiplication
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result



mult(matrix_a, matrix_b)
