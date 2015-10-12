def Capitalize(S):
    for i in range(len(S) - 1):
        T = S[i+1]
        #T.insert(0, chr(ord(T[0] + 32)))
        N = chr(ord(T[0]) - 32)
        T = N + T[1:]
        S.insert(i+1, T)
        S.pop(i + 2)
    K = str()
    for i in range(len(S)):
        K += str(S[i]) + ' '
    print(K)
S = input().split()
Capitalize(S)