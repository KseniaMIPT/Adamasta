A = list(map(int, str(input()).split())) # нет необходимость вводить n
for i in A:
    min = 0
    max = 0
    for j in A:
        if j > i: max += 1
        elif j < i: min += 1
        else:
            min += 1
            max += 1
        if max == min: mediana = i
print(mediana)