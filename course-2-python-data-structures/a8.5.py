fname = input("Enter file name: ")

if len(fname) < 1:
    fname = "mbox-short.txt"

try:
    fh = open(fname)
except:
    quit('File not found')

count = 0
for line in fh:
    if line.startswith('From'):
        if line[4] != ':':
            words = line.strip().split()
            print(words[1])
            count += 1


print("There were", count, "lines in the file with From as the first word")
