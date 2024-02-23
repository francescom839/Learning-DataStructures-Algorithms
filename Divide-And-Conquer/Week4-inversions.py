"""
This is my solution to the 5th problem of the week 4 of the "Data Structure and Algorithm Specialization" offered by the University of California San Diego. 
- - - Number of Inversions - - -
Compute the number of inversions in a sequence of integers 
Input: A sequence of n integers a1,...,an
Output: The number of inversions in the sequence , i.e., the number of indices i < j such that ai > aj
"""
import sys

def merge(left, right):
    sortedArray = [] # Empty array
    inversions = 0 
    while left and right: # Till they are not empty
        if left[0] <= right[0]:
            sortedArray.append(left.pop(0))
        else:
            sortedArray.append(right.pop(0))
            inversions += len(left)

    sortedArray += left or right
    return sortedArray, inversions


def merge_sort(a):
    if len(a) == 1: # The array is made of 1 element
        return a, 0

    mid = len(a) // 2
    left, invLeft = merge_sort(a[:mid]) # invLeft captures the number of inversions on the left side
    right, invRight = merge_sort(a[mid:]) # invRight captures the number of inversions on the right side

    merged, merged_inv = merge(left, right) # The inversions between left and right
    return merged, merged_inv + invLeft + invRight # Sum all the inversions counted at each step


if __name__ == "__main__":
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(merge_sort(a)[1])