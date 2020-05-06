name = input("Enter file:")

if len(name) < 1:
    name = "mbox-short.txt"

try:
    handle = open(name)
except:
    quit('File not found')

sender_cnt = dict()
for line in handle:
    if line.startswith('From'):
        if line[4] != ':':
            words = line.strip().split()
            sender_cnt[words[1]] = sender_cnt.get(words[1], 0) + 1

max_sender = None
max_count = None
for sender in sender_cnt:
    if max_count is None or (sender_cnt[sender] > max_count):
        max_sender = sender
        max_count = sender_cnt[sender]

print(max_sender, max_count)
