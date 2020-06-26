'''
Multiplication between odd and even (100 Marks)

For this challenge, you need to take number of elements as input on one line and array elements as an input on another line. You need to find the numbers that are odd, add them. find the numbers that are even add them and then multiply the two values that you get after addition of even numbers and that of addition of odd numbers.

Input Format
In this challenge, you will take number of elements as input on one line and array elements which are space separated as input on another line.

Constraints
1<  N < 10^5
1 < A[i] < 10^5

Output Format
You will print the value after multiplication to the stdout.

Sample TestCase 1
Input
6
11 22 33 44 55 66
Output
13068
'''


def main():
    number = int(input())
    array = list(map(int, input().split()))

    even = []
    odd = []
    for x in array:
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)

    print(sum(even) * sum(odd), end="")


main()