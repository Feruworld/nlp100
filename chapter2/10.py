#coding: utf-8
import commands

f = open('hightemp.txt', 'r')
print len(f.readlines())

f.close()
print '$wc hightemp.txt'
print commands.getoutput('wc hightemp.txt')
