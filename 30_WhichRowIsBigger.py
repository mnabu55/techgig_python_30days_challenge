'''
For this challenge, you need to take a matrix as an input from the stdin, identify which row has the maximum sum of the digits.For example, in the below matrix
1 2 3
4 5 6
7 8 9
Row 1 is 1,2,3
Row 2 is 4,5,6
Row 3 is 7,8,9

Input Format
The first line contains two integers N, M denoting the number of rows and columns respectively.
Each of the 'N' Next line contains M integers each.

Constraints
1 < (n,m) < 100

Output Format
If the sum of the digits of row 1 found to be greater than that of row 2 and row 3, then print 'Row 1' to the stdout. If the sum of all the rows found to be equal, then print 'Equal' to the stdout.

Sample TestCase 1
Input
3 4
2 3 4 2
1 4 6 5
4 8 9 6
Output
Row 3
'''


def main():
    row, column = map(int, input().split())
    array = []
    for i in range(row):
        array.append(list(map(int, input().split())))
    # print(array)

    sum_row_value_list = [0]*row

    for i in range(row):
        sum_row_value_list[i] = sum(array[i])

    print(f'Row {sum_row_value_list.index(max(sum_row_value_list))+1}', end="")


main()
