def sort(A, min = -1000, max = 1000):
    C = [0] * (max - min + 1)
    for i in range(0, len(A)):
        C[A[i] - min] = C[A[i] - min] + 1
    for j in range(1, len(C)):
        C[j] = C[j - 1] + C[j]
    B = [0] * len(A)
    for k in range(len(A) - 1, -1, -1):
        C[A[k] - min] = C[A[k] - min] - 1
        B[C[A[k] - min]] = A[k] 
    return B


