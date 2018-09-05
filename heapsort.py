def sort(A):
    for i in range(len(A)//2, -1, -1):
        max_heapify(A, i, len(A))
    for i in range(len(A) - 1, -1, -1):
        A[0], A[i] = A[i], A[0]
        max_heapify(A, 0, i)
    return A

def max_heapify(A, root, count):
    left = (root + 1)*2 - 1
    right = (root + 1)*2
    max = root
    if left < count and A[left] > A[max]:
        max = left
    if right < count and A[right] > A[max]:
        max = right
    if max != root:
        A[max], A[root] = A[root], A[max]
        max_heapify(A, max, count)

