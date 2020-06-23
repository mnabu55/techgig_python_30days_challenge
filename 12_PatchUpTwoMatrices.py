'''
Patch Up Two Matrices (100 Marks)
For this challenge, you need to take 2 matrices as an input from the stdin , add them and print the resultant matrix to the stdout.

Input Format
Two matrices to be taken as an input.
For each matrix, on first line you need to tell that how many rows and columns your matrix need to have and these values should be separated by space.
Then after that, each line will represent will represent each row and you need to enter numbers which each rows should have separated by a space.

Constraints
1 <  (n,m) < 100
1 <  (p,q) < 100

Output Format
Print the resultant matrix to the stdout where each each line should represent
Note : Please do not include space after the numbers which are in the last column as it will affect your submission and you will not get marks.
each row and values in the row should be separated by a space.
'''


def print_matrix(matrix, row, column):
    for r in range(row):
        print(' '.join([str(matrix[r][c]) for c in range(column)]), end="")
        if r != row-1:
            print("")


def main():
    matrix = []
    for n in range(2):
        row, column = map(int, input().split())
        matrix.append([])
        for i in range(row):
            matrix[n].append(list(map(int, input().split())))

#    print(f"matrix: {matrix}")
    result = [[0] * column for i in range(row)]

    for n in range(2):
        for r in range(row):
            for c in range(column):
                result[r][c] += matrix[n][r][c]
#    print(f'result: {result}')

    print_matrix(result, row, column)


main()
