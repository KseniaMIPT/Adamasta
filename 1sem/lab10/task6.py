file1 = open('en_ru_6.txt', 'r')
file2 = open('ru_en_6.txt', 'r')
dictionary1 = dict()
for line in file1:
    T = line.replace('\n', '').split(' - ')
    dictionary1[T[0]] = T[-1]
dictionary2 = dict()
for line in file2:
    T = line.replace('\n', '').split(' - ')
    dictionary2[T[0]] = T[-1]
inv_dictionary = {dictionary2[key] :key for key in dictionary2}
synchronized_dictionary = dict()
synchronized_dictionary_2 = dict()
#print(dictio)
for key1 in dictionary1:
    for key2 in inv_dictionary:
        if key1 == key2:
            synchronized_dictionary[key1] = str(dictionary1[key1] + ', ' + inv_dictionary[key2])
            synchronized_dictionary_2[dictionary1[key1]] = key1
            synchronized_dictionary_2[inv_dictionary[key2]] = key2
#print(synchronized_dictionary)
file1.close()
file2.close()
file_1_new = open('en_ru_syn.txt', 'w')
file_2_new = open('ru_en_syn.txt', 'w')
for key in synchronized_dictionary:
    print(key, '-', synchronized_dictionary[key], file = file_1_new)
for key in synchronized_dictionary_2:
    print(key, '-', synchronized_dictionary_2[key], file = file_2_new)
file_1_new.close()
file_2_new.close()
