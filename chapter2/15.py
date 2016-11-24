import sys

argvs = sys.argv
argc = len(argvs)

if argc != 2:
    print 'argument error'
    quit()

n = int(argvs[1])
f = open('hightemp.txt', 'r')
lines = f.readlines()
row = len(lines)

for i in range(row - n, row):
    print lines[i].rstrip()
