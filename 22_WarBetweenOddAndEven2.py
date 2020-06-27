'''
For this challenge, you need to take number of elements as input on one line and array elements as an input on another line. You need to find the numbers that are present at odd index, add them. find the numbers that are present at even index, add them and then subtract the smallest of the two values from the lager one.
Note:
Array indexes always starts from 0.

Input Format
In this challenge, you will take number of elements as input on one line and array elements which are space separated as input on another line.

Constraints
1 <  N < 10^5
1 < A[i] < 10^5

Output Format
You will print the value after subtraction to the stdout.

Sample TestCase 1
Input
6
11 22 33 44 55 66
'''


def main():
    number_of_list = int(input())
    array = list(map(int, input().split()))

    odd = [array[i] for i in range(len(array)) if i % 2 == 0]
    even = [array[i] for i in range(len(array)) if i % 2 == 1]

    print(abs(sum(odd) - sum(even)), end="")


main()
