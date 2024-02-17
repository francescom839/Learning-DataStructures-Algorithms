'''
This is the automated version of the "Find-Unknown-Value-BinarySearch.py", simply enter a number within 1 and 2097151
and the program will find it using binary search.
This code shows how quickly a binary algorithm can find a key value in a sorted amount of data.
'''
numberToGuess = 0  # Number to guess
iterations = 0     # Steps Counter

def query(y):  
    if numberToGuess == y: 
        return 'equal' 
    elif numberToGuess < y: 
        return 'smaller' 
    else: 
        return 'greater' 

def guess(lower, upper):
    global iterations
    middle = (lower + upper) // 2 
    answer = query(middle) 
    iterations += 1
    print(f'Is your number = {middle}? It is {answer}.') 
    if answer == 'equal':
        return print(f"With this binary approach it took {iterations} steps to find your number!\n")
    elif answer == 'smaller': 
        guess(lower, middle - 1)
    else: 
        assert answer == 'greater' 
        guess(middle + 1, upper) 

if __name__ == "__main__":
    numberToGuess = int(input("Please enter the value to guess within 1 and 2,097,151:\n")) 
    guess(1, 2097151)
