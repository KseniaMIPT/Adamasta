__author__ = 'Timofey Khirianov'
# -*- coding: utf8 -*-

class Vigenere:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    def __init__(self, keyword):
        self.alphaindex = {self.alphabet[index]: index for index in range(len(self.alphabet))}
        self.key = [self.alphaindex[letter] for letter in keyword.lower()]

    def caesar(self, letter, shift):
        if letter in self.alphaindex:  # строчная буква
            index = (self.alphaindex[letter] + shift)%len(self.alphabet)
            cipherletter = self.alphabet[index]
        elif letter.lower() in self.alphaindex:  # заглавная буква
            cipherletter = self.caesar(letter.lower(), shift).upper()
        else:
            cipherletter = letter
        return cipherletter

    def encode(self, line, key=None, decode = 1):
        if not key:
            key = self.key
        ciphertext = []
        i = 0
        for letter in line:
            shift = key[i]
            cipherletter = self.caesar(letter, shift*decode)
            ciphertext.append(cipherletter)
            i = (i + 1)%len(key)

        return ''.join(ciphertext)


f = open('text_for_vigenere', 'r')
txt = f.readlines()
f.close()

"""test_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
test_word = 'шифр'
test_result = 'йыгь'
first_part_of_keyword = ''
for i in range(len(test_word)):
    index = test_alphabet.index(test_result[i]) - test_alphabet.index(test_word[i])
    if index >= 0:
       first_part_of_keyword += test_alphabet[index]
    else:
        first_part_of_keyword += test_alphabet[33 + index]
print(first_part_of_keyword)

for i in range(len(test_alphabet)):
    test_char = test_alphabet[i]
    print(test_char)
    ciper = Vigenere('столлман')
    #for line in txt:
    print(ciper.encode(txt[2]))
    print(123456781234567812345678123456781234567812345678)"""

ciper = Vigenere('столлман')
for line in txt:
    print(ciper.encode(line, decode=-1))



