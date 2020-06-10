import random
s = input('Enter a String:') # Reading the user input
i = 0 # initializing the iterator
strLen = len(s) - 1 # Calculating the length of the string
if strLen > 0 : # checking for valid string
    while i < 2: # Looping for 2 times
        randomNumber = random.randint(0,strLen) # Generating the Random number
        s = s[:randomNumber] + s[(randomNumber+1):] # slicing based on the generated random number and concatinating the string
        i += 1 # incrementing the iterator
else :
    print('Enter a proper string') # Message to enter a proper string
print('Result after removing 2 characters from string:',s)
s = s[::-1] # This will perform the string reverse operation
print('After string reverse:',s)