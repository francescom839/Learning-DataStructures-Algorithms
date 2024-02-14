"""
This is a game to better understand how binary search works.
A person will think about a number between 1 and n.
You will find out what number they are thinking by using binary search.
The only input the person must give you is tell you if the current
value is higher or lower.
"""
def FindUnknownValue():
    i = 0
    LowerIndex = 1
    HigherIndex = int(input("Please enter the greatest value to choose from 1 to n:\n "))
    while LowerIndex <= HigherIndex:
        middle = (LowerIndex + HigherIndex) // 2
        print(f"Is your value {middle}?")
        answer = input("Enter the following answers: \n (<) No, it's lower.\n (>) No, it's larger. \n (Y) Yes, that's it! \n")
        if (answer == "Y"):
            i += 1
            return print(f"There you go! With binary search I found your number in {i} iterations. \n Remember, binary search has a O(Log n)!")
        elif (answer == "<"):
            i += 1
            HigherIndex = middle - 1
        elif (answer == ">"):
            i += 1
            LowerIndex = middle + 1
        else:
            print(f"The value {answer} is invalid. Please use the values <, > or Y\n")
    print(f"Well.. that can't be possible, your number must be {middle}!\nUnless you forgot the number :)")

if __name__ == "__main__":
    FindUnknownValue()