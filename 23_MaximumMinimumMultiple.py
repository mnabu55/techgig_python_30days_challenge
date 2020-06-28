'''
Maximum Vs Minimum (100 Marks)
For this challenge, you need to take number of elements as input on one line and array elements as an input on another line. You need to find the minimum number and maximum number from the array and multiply them.

Input Format
In this challenge, you will take number of elements as input on one line and array elements which are space separated as input on another line.

Constraints
1 < N < 10^5
1 < A[i] < 10^5

Output Format
You will print the value after multiplication to the stdout.

Sample TestCase 1
Input
6
11 22 33 44 55 66
'''


def main():
    n = int(input())
    array = list(map(int, input().split()))
    print(min(array) * max(array), end="")


main()
