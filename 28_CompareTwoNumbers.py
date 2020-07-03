'''
For this challenge, you will take two integers input from stdin, sum the digits of a number and same is to be done with another number. Then compare the sum of the digits of two numbers and if one sum found to be greater then print that number to the stdout. If found both sum to be equal then print 'Equal' to the stdout.

Input Format
Two integer values to be taken as input from stdin.

Constraints
1 < (a,b) < 10^9

Output Format
Print the single number after comparison. If found equal, then print 'Equal' to the stdout.

Sample TestCase 1
Input
345678   444444
Output
345678
'''

def get_sum_digits(number):
    sum_digits = 0
    while number != 0:
        sum_digits += number % 10
        number = number // 10
    return sum_digits


def main():
    array = list(map(int, input().split()))

    sum_digits_list = []
    for n in array:
        sum_digits_list.append(get_sum_digits(n))

    print(array[sum_digits_list.index(max(sum_digits_list))], end="")


main()
