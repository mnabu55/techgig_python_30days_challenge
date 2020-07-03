'''
For this challenge, you will take an integer input from stdin, store it in a variable, find the digits in that number, identify digits that are odd and add them, identify which digits are even and add them. Subtract the smaller with the larger one.

Input Format
A single integer value to be taken as input from stdin and stored it in a variable of your choice.

Constraints
1 < N < 10^9

Output Format
Print the single number after subtraction.

Sample TestCase 1
Input
34567
Output
5
'''


def main():
    s = input()
    even = [int(c) for c in s if int(c) % 2 == 0]
    odd = [int(c) for c in s if int(c) % 2 != 0]
    print(abs(sum(even) - sum(odd)), end="")


main()
