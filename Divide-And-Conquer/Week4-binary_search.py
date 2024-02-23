'''
This is my solution to the 1st problem of the week 4 of the "Data Structure and Algorithm Specialization" offered by the University of California San Diego. 
- - - Sorted Array Search Problem - - -
Search a key in a sorted array of keys.
Input: A sorted array K = [k0,...,kn−1] of distinct integers (i.e.,k0 < k1 <···< kn−1) and an integer q.
Output: Check whether q occurs in K.
'''
def binary_search(keys, query):
    left = 0
    right = len(keys) - 1
    while right >= left:
        middle = (left + right) // 2
        if keys[middle] == query:
            return middle
        elif keys[middle] > query:
            right = middle - 1
        else:
            left = middle + 1
    return -1 # If the right is < than left (0), that means the array is empty

if  __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
