#coding: utf-8
text1 = u'パトカー'
text2 = u'タクシー'

text = u''
'''
for i in range(len(text1)):
    text += text1[i]
    text += text2[i]
'''

for i,j in zip(text1, text2):
    text += i + j

print text
