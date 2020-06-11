file = open("input.txt", "r")   # opening a file
file_content = file.read()           # reading file
words = file_content.split()           # split the data

frequency = dict()             # create a dictionary

for word in words:
    word = word.lower()
    if word in frequency:        # check if the word is already in dict
        frequency[word] += 1      # incrementing the count of the word
    else:
        frequency[word] = 1       # if the word in new assign count as 1

f1 = open("output.txt", "w")

for key in list(frequency.keys()):
    print(key, ":", frequency[key]) # printing the word frequency in readable format
    f1.write(str(key) + ":" + str(frequency[key]) + '\n') # writing the result to the file

f1.close()