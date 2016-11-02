#coding: utf-8
import commands

f = open('hightemp.txt', 'r')

for line in f:
    print line.replace('\t',' '),

f.close()

print "$ cat hightemp.txt | tr '\\t' ' '"
print commands.getoutput("cat hightemp.txt | tr '\\t' ' '")
