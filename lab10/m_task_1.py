__author__ = 'student'
A = set('bqlpzlkwehrlulsdhfliuywemrlkjhsdlfjhlzxcovt')
B = set('zmxcvnboaiyerjhbziuxdytvasenbriutsdvinjhgik')
C = str()
for x in A:
    if x not in B:
        C += x
print(C)