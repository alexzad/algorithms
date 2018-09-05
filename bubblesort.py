def sort(A):
    sorted = 0
    while not sorted:
        sorted = 1
        for j in range(1, len(A)):
            if A[j - 1] > A[j]:
                sorted = 0
                A[j - 1], A[j] = A[j], A[j - 1]
    return A