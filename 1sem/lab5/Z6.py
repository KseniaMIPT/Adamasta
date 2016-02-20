input = open('float_data.txt', 'r')
File = input.read().split()
List = list(map(float, File))

Average = sum(List)/len(List)
print('среднее арифметическое', Average)

sum_sigma = 0
for i in List:
    sum_sigma += (Average - i) ** 2
sigma = sum_sigma/len(List)
print('среднеквадратическое отклонение от среднего', sigma)

max_number = max(List)
print('максимальное число', max_number, 'его местоположение', List.index(max_number))

min_number = min(List)
print('минимальное число', min_number, 'его местоположение', List.index(min_number))

#for i in File:
 #   List += float(File[i])
#print(File)
#print(List)