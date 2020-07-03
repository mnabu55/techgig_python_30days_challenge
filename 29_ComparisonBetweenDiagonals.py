'''
For this challenge, you need to take a matrix as an input from the stdin , calculate the sum of the digits for each diagonal and compare them.For example,
in the below matrix
1 2 3
4 5 6
7 8 9
Diagonal 1 is 1,5,9.
Diagonal 2 is 3,5,7.

Input Format
A matrix is to be taken as input from stdin.On first line you need to tell that how many rows and columns your matrix need to have and these values should be separated by space.

Constraints
1 < (n,m) < 100

Output Format
If sum of digits for diagonal 1 is found to be greater than diagonal 2, then print 'Diagonal 1' to the stdout. If sum of digits for diagonal 2 is found to be greater than diagonal 1, then print 'Diagonal 2' to the stdout. If both of the diagonal found to be equal, then print 'Equal' to the stdout.

Sample TestCase 1
Input
3 3
2 3 4
1 4 6
7 8 9
Output
Equal
'''


def main():
    row, column = map(int, input().split())
    array = []
    for i in range(row):
        array.append(list(map(int, input().split())))

    # diagonals 1
    diagonals1 = 0
    for i in range(row):
        diagonals1 += array[i][i]

    # diagonals 2
    diagonals2 = 0
    for i in range(row):
        diagonals2 += array[i][row-i-1]

    result = ""
    if diagonals1 > diagonals2:
        result = "Diagonal 1"
    elif diagonals1 < diagonals2:
        result = "Diagonal 2"
    else:
        result = "Equal"

    print(result, end="")


main()
