'''
For this challenge, Given an unsorted array arr[0..n-1] of size n, find the minimum length subarray arr[s..e] such that sorting this subarray makes the whole array sorted.

Input Format
On the first line, you need to take an integer input which will be the length of the array. Another line will have space separated integer values.

Constraints
1 < n < 10^5
1 < A[i] < 10^5

Output Format
Space separated integer values present in the subarray.
'''


def main():
    len_array = int(input())
    array = list(map(int, input().split()))
    sort_array = sorted(array)

    first = 0
    end = len_array

    # find first element of array
    for v_a, v_s in zip(array, sort_array):
        if v_a == v_s:
            first += 1
        else:
            break

    # find end element of array
    for v_a, v_s in zip(array[::-1], sort_array[::-1]):
        if v_a == v_s:
            end -= 1
        else:
            break

    print(" ".join([str(x) for x in array[first:end]]), end="")


main()
