'''
For this challenge, you will take an integer input from stdin, store it in a variable, find the digits in a number and then print the biggest of them.

Input Format
A single integer value to be taken as input from stdin and stored it in a variable of your choice.

Constraints
1 < N < 10^9

Output Format
Print the biggest digit in a number.

Sample TestCase 1
Input
345678
Output
8
'''


def main():
    s = input()
    array = []
    for d in s:
        array.append(int(d))
    print(max(sorted(array)), end="")


main()
