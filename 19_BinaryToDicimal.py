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
    pos = 1
    for i in number_string[::-1]:
        decimal += 2 ** (pos - 1) * int(i)
        pos += 1
    print(f'{decimal}', end="")


main()

