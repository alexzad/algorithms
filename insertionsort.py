def sort(A):
    return insertionsort(A, 0, len(A))

def insertionsort(A, p, q):
    for i in range(p + 1, q):
        j = i
        while j > 0 and A[j - 1] > A[j]:
            A[j], A[j - 1] = A[j - 1], A[j]
            j = j - 1        
    return A

