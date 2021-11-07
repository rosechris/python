import string

fhand = open('mbox.txt')
counts = dict()
cnt = 0
for line in fhand:
    words = line.split()
    if len(words) == 0: continue
    if words[0] != 'From': continue

    if words[1] not in counts:
        counts [words[1]] = 1
    else:
        counts [words[1]] +=1

lst = list()
for key, val in list(counts.items()):
    lst.append ((val,key))

lst.sort(reverse=True)
for key, val in lst:
    print (key, val)
