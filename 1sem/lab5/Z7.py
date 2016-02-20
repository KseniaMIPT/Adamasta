input = open('int_data.txt', 'r')
File = input.read().split()
List = list(map(int, File))

Stat = {number: List.count(number) for number in range(100)}

max = 0
min = 100
max_key = int()
min_key = int()
for key in Stat:
    if Stat[key] > max:
        max = Stat[key]
        max_key = key
    if Stat[key] < min:
        min = Stat[key]
        min_key = key
print('самое часто встречающееся число', Stat[max_key],'\nсамое редко встречающееся число', Stat[min_key])

Count = 0
for key in Stat:
    if Stat[key] != 0:
        Count += 1
print('сколько различных чисел встречается в последовательности', Count)