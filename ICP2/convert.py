n = int(input('Enter number of inputs')) # Reading the integer value from console
lbs = [] # declaring empty list for lbs
kgs = [] # declaring empty list for kgs
for i in range(n): # looping based on the input number
    temp = int(input('Enter weight in lbs')) # reading the input from console
    lbs.append(temp) # Appending the entered input to lbs
    kgs.append(temp * 0.45359237) # converting the entered value into kgs and appending to kgs list
print('Entered weights in Lbs:',lbs)
print('Converted weights in kgs:',kgs)

kgsList = [ item*0.45359237 for item in lbs] # list comprehension syntax
print('Converted Using List Comprehension:', kgsList)
