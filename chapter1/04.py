#coding: utf-8
import re

text = u'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
first = [1, 5, 6, 7, 8, 9, 15, 16, 19]

text = re.sub(',|[.]', "", text)
words = text.split(' ')
first = [x-1 for x in first]
index = {}

for i,word in enumerate(words):
    if i in first:
        key = word[0]
    else:
        key = word[0:2]
    index[key] = i+1

print index
