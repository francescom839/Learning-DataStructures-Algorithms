'''
This is my solution to the 2nd problem of the week 4 of the "Data Structure and Algorithm Specialization" offered by the University of California San Diego. 
- - - Binary Search with Duplicates Problem - - -
Find the index of the first occurrence of a key in a sorted array.
Input: A sorted array K = [k0,...,kn−1] possibly with duplicates and an integer q.
Output: Index f the first occurrence of q in the array or "-1" if q does not appear in the array.
'''
def binary_search(keys, query):
    left = 0
    right = len(keys) - 1
    while right >= left:
        middle = (left + right) // 2
        if keys[middle] == query:
            right = middle # Once the value has been found, limit the range to the possible duplicates
            while right > left: # Create a "sub problem" and solves it with another binary search.
                middle = (right + left) // 2
                if keys[middle] == query:
                    right = middle # Reduce the range
                elif keys[middle] < query:
                    left = middle + 1
            return right # Returns once right and left are equal
        elif keys[middle] > query:
            right = middle - 1
        else:
            left = middle + 1
    return -1 # If the right is < than left (0), that means the array is empty

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
