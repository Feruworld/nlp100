#coding: utf-8

def cipher(text):
    code = ''
    for c in text:
        if ord('a') <= ord(c) < ord('z'):
            code += chr(219 - ord(c))
        else: code += c
    return code

print cipher('Hi He Lied Because Boron Could Not Oxidize Fluorine.')
