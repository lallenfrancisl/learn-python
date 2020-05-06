# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

# find the spam confidence
spam = 0
spam_count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        pos = line.find(':')
        spam += float(line[(pos + 1):].strip())
        spam_count += 1

# calculate the spam average
spam_conf = spam / spam_count

print('Average spam confidence:', spam_conf)
