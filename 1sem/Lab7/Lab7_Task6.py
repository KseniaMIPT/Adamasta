import matplotlib.pyplot as plt
f = open('input.txt', 'r')
file_lines = f.readlines()
words_list = []
for i in range(len(file_lines)):
    words_list += file_lines[i].split()
words_len = [len(word) for word in words_list]
number_of_words_with_length = [words_len.count(length) for length in range(min(words_len), max(words_len))]
plt.plot(number_of_words_with_length, )
plt.show()