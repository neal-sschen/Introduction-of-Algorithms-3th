def P(A,x):
    i = 0
    r = len(A)-1
    while i < r:
        k = x - A[i]
        j = i+1
        while j <= r:
            if A[j] == k:
                return 'Yes'
            else:
                j = j+1
        i = i +1
    return 'No'

A = [1,2,3,1,4,5]
x = 10

print(P(A,x))
