import random
import insertionsort

def sort(A):
    return quicksort(A, 0, len(A))

def quicksort(A, p, q):
    if p < q:
        pivot = partition(A, p, q)
        quicksort(A, p, pivot)
        quicksort(A, pivot + 1, q)
    return A

def partition(A, p, q):
    r = random.randint(p, q - 1)
    A[p], A[r] = A[r], A[p]
    i = p
    for j in range(p + 1, q):
        if A[j] <= A[p]:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[p], A[i] = A[i], A[p]
    return i
