#coding: utf-8

def n_gram(n, seq):
    if n > len(seq):
        print 'ERROR: n is too big.'
        exit()
    n_gram_list = [seq[i:i+n] for i in range(len(seq)-n+1)]
    return n_gram_list


text1 = 'paraparaparadise'
text2 = 'paragraph'

X = n_gram(2, text1)
Y = n_gram(2, text2)

union = list(set(X + Y))
meet = list(set([elem for elem in X if elem in Y]))
diff = [elem for elem in union if not elem in meet]

print 'X:',X
print 'Y:',Y

print 'se in X:', 'se' in X
print 'se in Y:', 'se' in Y

print '和集合:', union
print '積集合:', meet
print '差集合:', diff
