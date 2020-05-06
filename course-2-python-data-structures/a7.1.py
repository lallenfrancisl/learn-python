# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    quit("Error opening file!")

# read and capitalize the text in the file
text = fh.read().upper().rstrip()

# print the capitalized text
print(text)
