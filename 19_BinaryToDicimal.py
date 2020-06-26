'''
You will be getting a binary number as an input and you need to convert it into a decimal number.

Input Format
You will be taking a binary number as an input.

Constraints
1 < N < 10^9

Output Format
Print the decimal number to the stdout.
'''


def main():
    number_string = input()

    decimal = 0
    for i, v in enumerate(number_string[::-1]):     # get value from 1st position
        decimal += 2 ** i * int(v)                  # i-th weight: 2 ^ (i - 1)
    print(f'{decimal}', end="")


main()

