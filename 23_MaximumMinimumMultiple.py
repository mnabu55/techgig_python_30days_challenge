
def main():
    n = int(input())
    array = list(map(int, input().split()))
    print(min(array) * max(array), end="")


main()
