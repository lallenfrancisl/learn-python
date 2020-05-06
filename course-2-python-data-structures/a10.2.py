name = input("Enter file:")

if len(name) < 1:
    name = "mbox-short.txt"

try:
    handle = open(name)
except:
    quit('File not found')

time_dist = dict()
for line in handle:
    if line.startswith('From'):
        if line[4] != ':':
            words = line.strip().split()
            time_dist[words[5][:2]] = time_dist.get(words[5][:2], 0) + 1

time_dist = sorted([(key, val) for key, val in time_dist.items()])

for hour, freq in time_dist:
    print(hour, freq)
