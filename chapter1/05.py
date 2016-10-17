#coding: utf-8

text = 'I am an NLPer'

def n_gram(n, seq):
    if n > len(seq):
        print 'ERROR: n is too big.'
        exit()
    n_gram_list = []
    for i in range(len(seq) - n + 1):
        n_gram_list.append(seq[i:i+n])
    return n_gram_list

words = text.split(' ')
print n_gram(2, words)
print n_gram(2, text)
