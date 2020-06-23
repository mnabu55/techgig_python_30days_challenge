'''
GCD of two numbers (100 Marks)
For this challenge, you need to take input of two numbers , calculate their greatest common divisor (GCD) and print it to the stdout.

Input Format
You need to take two integers as an input which are separated by a single space.

Constraints
1 < (a,b) < 10^5

Output Format
Print the single integer result to the stdout.
'''


def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


main()
