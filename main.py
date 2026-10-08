fhand = open('mbox-short.txt')
fhand.read()
count = 0
with open('mbox-short.txt') as fhand:
    for line in fhand:
        line = line.rstrip()
        if line.startswith('From:'):
            words = line.split()
            print(words[1])
            count += 1
print("There were ", count , " lines in the file")
fhand.close()
