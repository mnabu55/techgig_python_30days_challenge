'''
For this challenge, you need to take a matrix as an input from the stdin , transpose it and print the resultant matrix to the stdout.

Input Format
A matrix is to be taken as input from stdin. On first line you need to tell that how many rows and columns your matrix need to have and these values should be separated by space. Below lines will represent the elements of the matrix where each line will represent the row of the matrix.

Constraints
1 < (n,m) < 100

Output Format
Print the resultant matrix to the stdout where each line should represent each row and values in the row should be separated by a space.
'''


def print_matrix(matrix, row, column):
    for r in range(row):
        print(' '.join([str(matrix[r][c]) for c in range(column)]), end="")
        if r != row-1:
            print("")


def transpose(a, b, row, column):
    for r in range(row):
        for c in range(column):
            b[c][r] = a[r][c]


def main():
    row, column = map(int, input().split())

    array = []
    for i in range(row):
        array.append(list(map(int, input().split())))
    roll_array = [[0 for r in range(row)] for c in range(column)]
    transpose(array, roll_array, row, column)
    print_matrix(roll_array, column, row)


main()
