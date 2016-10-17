#coding: utf-8
import re

text = u'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
text = re.sub(',|[.]', "", text)
words = text.split(' ')
pi = []

for w in words:
    pi.append(len(w))

print pi
