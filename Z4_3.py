A = [1,2,2,2,3,3,34,8]
B = str()
for i in range(len(A)):
    if A.count(A[i]) == 1:
        print(A[i])