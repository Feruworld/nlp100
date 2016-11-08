#coding: utf-8
import commands

f1 = open('col1.txt', 'r')
f2 = open('col2.txt', 'r')

for line1, line2 in zip(f1,f2):
    print line1.rstrip(),'\t', line2.rstrip()

f1.close()
f2.close()


#print "$ cat hightemp.txt | tr '\\t' ' '"
#print commands.getoutput("cat hightemp.txt | tr '\\t' ' '")
