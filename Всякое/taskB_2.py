def Capitalize():
    for i in range(len(S)): #выбираем слово
        T = S[i] #слово
        if (ord(T[0]) >= 97) and (ord(T[0]) <= 122):
            N1 = chr(ord(T[0]) - 32) #делает из строчной заглавную
            T = N1 + T[1:] #складывает первую букву и остальное слово
            S.insert(i, T) #заменяет слово на слово с заглавной буквой
            S.pop(i + 1) #удаляет старый вариант слова
        for n in range(len(T)-1):
            if (ord(T[n+1]) <= 90) and (ord(T[n+1]) >= 65):
                N2 = chr(ord(T[n + 1]) + 32) #делает из заглавной строчную
                T = T[:n+1] + N2 + T[n+2:] #складывает букву и остальное слово
                S.insert(i, T) #заменяет слово на слово с измененной буквой
                S.pop(i + 1) #удаляет старый вариант слова

    K = str() #преобразует список в строку
    for i in range(len(S)):
        K += str(S[i]) + r
    print(K)
    
D = str(input())
f = -1
n = 0
while ((ord(D[f]) >= 97) and (ord(D[f]) <= 122)) or ((ord(D[f]) <= 90) and (ord(D[f]) >= 65)):
    f += 1
    n += 1

S = D.split(D[n - 1])
r = D[n-1]

Capitalize()