n = open("madhu.txt","r")  # open file, read-only
s = open("sorter.txt", "w") # open file, write
lines = n.readlines()
lines.sort()

for line in lines:
 s.write(line)

n.close()
s.close()