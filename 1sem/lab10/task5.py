def sort(A):
    if len(A) <= 1:
        return A
    barier = A[0]
    left = [x for x in A if x < barier]
    middle = [x for x in A if x == barier]
    right = [x for x in A if x > barier]
    left = sort(left)
    right = sort(right)
    return left + middle + right

file = open('input5.txt', 'r')
dictionary = dict()
for line in file:
    T = line.replace('\n', '').split(' - ')
    dictionary[T[0]] = T[-1]
dictionary_2 = {dictionary[key] : key for key in dictionary}
Keys = []
for key in dictionary_2:
    Keys.append(key)
output = open('ru_en.txt', 'w')
Keys = sort(Keys)
for i in Keys:
    for key in dictionary_2:
        if key == i:
            print(key, '-', dictionary_2[key], file = output)
file.close()
output.close()