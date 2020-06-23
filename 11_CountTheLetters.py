'''
For this challenge, you need to take a string as an input from the stdin, count the number of uppercase and lowercase letters and print them to the stdout.

Input Format
A single line of string to be taken as an input and store it in a variable of your choice.

Constraints
1 < = |s| < = 100000

Output Format
print the number of uppercase letters on one line and number of lowercase letters on another side.
'''

def main():
    s = input()

    number_of_uppercase = 0
    number_of_lowercase = 0
    for c in s:
        if c.islower():
            number_of_lowercase += 1
        elif c.isupper():
            number_of_uppercase += 1

    print(f'{number_of_uppercase}\n{number_of_lowercase}', end="")


main()

