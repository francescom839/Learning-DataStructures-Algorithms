'''
This is my solution to the 3rd problem of the week 4 of the "Data Structure and Algorithm Specialization" offered by the University of California San Diego. 
- - - Majority Element Problem - - -
Check wheter a given sequence of numbers contains an element that appears more than half of the times.
Input: A sequence of n integers
Output: 1, if there is an element that is repeated more than n/2 times, and 0 otherwsie.
'''
def majority_element(elements):
    counterDict = {} # Create a dictionary to count all the occurrencies
    for number in elements:
        if number in counterDict:
            counterDict[number] += 1
        else:
            counterDict[number] = 1
    
    for key, value in counterDict.items():
        if value > len(elements) // 2: # Check if a value was present more than the half of the array's lenght
            return 1
    return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
