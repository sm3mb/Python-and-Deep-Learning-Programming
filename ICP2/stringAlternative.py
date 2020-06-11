def string_alternative(value): # function definition
    return value[::2] # returning the result after slicing the alternative characters

if __name__ == "__main__":
    s = input('Enter a string:') # reading the input from console
    alternative = string_alternative(s) # function call and assigning the result to a variable
    print('Entered string is:',s,'& Altered string is:',alternative)