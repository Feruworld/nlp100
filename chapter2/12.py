#coding: utf-8
import commands

f = open('hightemp.txt', 'r')
col1, col2 = [], []

for line in f:
    words = line.split()
    col1.append(words[0] + '\n')
    col2.append(words[1] + '\n')

f.close()

f1 = open('col1.txt', 'w')
f2 = open('col2.txt', 'w')
f1.writelines(col1)
f2.writelines(col2)
f1.close()
f2.close()


#print "$ cat hightemp.txt | tr '\\t' ' '"
#print commands.getoutput("cat hightemp.txt | tr '\\t' ' '")
