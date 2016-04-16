import random
__author__ = 'Ksenia Lupyr and Timofey Khirianov'
# -*- coding: utf8 -*-


def frequency_analysis(txt):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    frequency_dict = {}
    for symbol in alphabet:
        frequency_dict[symbol] = txt.count(symbol)
    all_count = sum([frequency_dict[symbol] for symbol in frequency_dict])
    result = sorted(frequency_dict, key=frequency_dict.__getitem__, reverse=True)
    percent = [frequency_dict[key]/all_count for key in result]
    return [result, percent]


def sort_keytable(freq_alphabet, secret_alphabet):
    freq_dict = {}
    for i in range(len(freq_alphabet)):
        freq_dict[secret_alphabet[i]] = freq_alphabet[i]
    return freq_dict


class Monoalphabet:

    def __init__(self, keytable):
        lowercase_code = keytable
        uppercase_code = {key.upper():keytable[key].upper() for key in keytable}
        self._decode = dict(lowercase_code)
        self._decode.update(uppercase_code)
        self._encode = {self._decode[key]:key for key in self._decode}

    def encode(self, line):
        if len(line) == 1:
            return self._encode[line] if line in self._encode else line
        else:
            return ''.join([self.encode(char) for char in line])

    def decode(self, line):
        if len(line) == 1:
            return self._decode[line] if line in self._decode else line
        else:
            return ''.join([self.decode(char) for char in line])

    def change_char(self, secret_char, normal_char):
        x = self._decode[secret_char]
        self._decode[secret_char] = normal_char
        for key in self._decode:
            if self._decode[key] == normal_char:
                self._decode[key] = x



text = open('text', 'r')
secret_text = open('secret_text', 'r')
txt = text.read()
secret_txt = secret_text.read()
text.close()
secret_text.close()

txt_frequency_analysis = frequency_analysis(txt)
text_analysis = txt_frequency_analysis[0]
secret_frequency_analysis = frequency_analysis(secret_txt)
secret_text_analysis = secret_frequency_analysis[0]
keytable = sort_keytable(text_analysis, secret_text_analysis)

keytable['ж'] = 'ш'  # Шифр
keytable['й'] = 'и'
keytable['р'] = 'ф'
keytable['ъ'] = 'в'  # В году
keytable['г'] = 'г'
keytable['л'] = 'о'
keytable['с'] = 'д'
keytable['х'] = 'у'
keytable['е'] = 'ж'   # Виженера
keytable['д'] = 'е'
keytable['а'] = 'н'
keytable['ч'] = 'а'

keytable['и'] = 'п'
keytable['э'] = 'й'
keytable['ы'] = 'т'
keytable['ь'] = 'з'
keytable['з'] = 'м'
keytable['ц'] = 'ы'

keytable['н'] = 'б'
keytable['о'] = 'л'
keytable['ю'] = 'с'
keytable['я'] = 'ь'
keytable['ё'] = 'я'
keytable['ш'] = 'к'
keytable['ф'] = 'х'
keytable['у'] = 'ю'
keytable['б'] = 'ц'
keytable['м'] = 'ё'
keytable['щ'] = 'щ'
keytable['к'] = 'э'

cipher = Monoalphabet(keytable)

for i in range(33):
    print(txt_frequency_analysis[0][i], end=' ')
    print("%5.4f" % (txt_frequency_analysis[1][i]), end=' ')
print()
for i in range(33):
    print(secret_frequency_analysis[0][i], end=' ')
    print("%5.4f" % (secret_frequency_analysis[1][i]), end=' ')
print()

f = open('text_for_mono', 'r')
print_mono = f.read()
f.close()
print(cipher.decode(print_mono))

