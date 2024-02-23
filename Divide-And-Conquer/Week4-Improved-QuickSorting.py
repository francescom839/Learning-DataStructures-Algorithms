"""
This is my solution to the 4rd problem of the week 4 of the "Data Structure and Algorithm Specialization" offered by the University of California San Diego. 
- - - Speeding-Up Randomized Quick Sort - - -
Sort a given sequence of numbers (that may contain duplicates) using a modification of Randomized-Quick-Sort that works in O(n log n) expected time.
Input: An integer array with n elements that may contain duplicates
Output: Sorted array (generated using a modification of Randomized Quick Sort) that works in O(n log n) expected time.
"""

from random import randint


def partition3(array, left, right): # This function must create 3 partitons [< Pivot, == Pivot, > Pivot]
    pivot, m1, m2 = array[left], left, right # Array[left] is our random pivot
    i = m1
    while i <= m2: # Iterate through i(m1) --> m2
        if array[i] < pivot:
            array[m1], array[i] = array[i], array[m1] # Moves that value to the left side of the pivot
            m1 += 1 # Increase the index where the values are LESS than the pivot
        elif array[i] > pivot:
            array[m2], array[i] = array[i], array[m2] # Moves that value to the right side of the pivot
            m2 -= 1 # Decrease the index where the values are MORE than the pivot
            i -= 1 # We must recheck the value just swapped from m2
        else:
            i += 1 # If the value is equal, do nothing, just continue iterating
    return m1, m2


def randomized_quick_sort(array, left, right):
    if left >= right:  # if there is only 1 element, just return
        return
    pivot = randint(left, right)  # randomly choose a pivot
    array[left], array[pivot] = array[pivot], array[left] # Swaps the pivot with the first element
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)


if __name__ == "__main__":
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
