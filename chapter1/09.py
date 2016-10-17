import random

def typoglycemia(text):
    words = text.split()
    typo = []
    for i,word in enumerate(words):
        if i in (0, len(words)-1) or len(word) <= 4:
            typo.append(word)
            continue
        arrange = range(1, len(word)-1)
        random.shuffle(arrange)
        arr_word = word[0]
        arr_word += ''.join([word[j] for j in arrange])
        arr_word += word[len(word)-1]
        typo.append(arr_word)
    return ' '.join(typo)

print typoglycemia("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .")
