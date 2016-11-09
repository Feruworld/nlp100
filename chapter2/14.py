#coding: utf-8
import sys

argvs = sys.argv
argc = len(argvs)

if (argc != 2):
    print 'argument error'
    quit()

n = int(argvs[1])
f = open('hightemp.txt', 'r')
count = 0

for line in f:
    print line.rstrip()
    count += 1
    if count == n: break
