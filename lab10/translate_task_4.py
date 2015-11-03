__author__ = 'student'
file = open('en-ru.txt', 'r')
dictionary = dict()
for line in file:
    T = line.replace('\n', '').split(' - ')
    dictionary[T[0]] = T[-1]

file_for_translation = open('input.txt', 'r')
for line in file_for_translation:
    line = line.lower().replace('.', '').replace('\n', '').split()
    translation = str()
    for word in line:
        translation += dictionary[word] + ' '
    print(translation)

