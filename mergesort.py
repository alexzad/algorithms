def sort(A):
    mergesort(A)
    return A

def mergesort(A):
    if len(A) == 1:
        return A
    if len(A) == 2:
        if A[0] > A[1]:
            A[0], A[1] = A[1], A[0]
        return A
    if len(A) > 2:
        mid = len(A)//2
        L = mergesort(A[:mid])
        R = mergesort(A[mid:])
        l = 0
        r = 0
        a = 0
        while a < len(A):
            if l < len(L) and r < len(R):
                if L[l] <= R[r]:
                    A[a] = L[l]
                    l = l + 1
                else:
                    A[a] = R[r]
                    r = r + 1
            elif l >= len(L):
                A[a] = R[r]
                r = r + 1
            else:
                A[a] = L[l]
                l = l + 1
            a = a + 1  
        return A