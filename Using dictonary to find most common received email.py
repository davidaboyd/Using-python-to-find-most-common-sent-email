#Please google mbox-short.txt
#and download the file

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts=dict()
for line in handle:
    line=line.rstrip()
    if not line.startswith('From '):continue
    words=line.split()
    #print(words[1])
    #for word in words[1]:
    counts[words[1]]=counts.get(words[1],0) + 1
        #counts.append(word)
    print(words[1])
largest=-1

theWord=None

for k,v in counts.items() :
    if v > largest:
           largest=v
           theWord=k
print('Done',largest,theWord)
