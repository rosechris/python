fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    exit()

ul = []
for line in fhand:
    wl=line.split()

    for word in wl:
        if word in ul: continue
        ul.append(word)

ul.sort()
print ("Number of words: ")
print(len(ul))
print (ul)
