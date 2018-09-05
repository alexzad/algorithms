import math 

def sort(A, radix = 2001, min = -1000, max = 1000):
    if len(A) < 1:
        return A

    def counting_sort(A, digit, radix):
        B = [0]*len(A)
        C = [0]*int(radix)
        for i in range(0, len(A)):
            digit_of_Ai = (int)(A[i]/radix**digit)%radix
            C[digit_of_Ai] = C[digit_of_Ai] + 1 
        for j in range(1,radix):
            C[j] = C[j] + C[j-1]
        for m in range(len(A)-1, -1, -1): 
            digit_of_Ai = (int)(A[m]/radix**digit)%radix
            C[digit_of_Ai] = C[digit_of_Ai] -1
            B[C[digit_of_Ai]] = A[m]
        return B

    for i in range(len(A)):
        A[i] = A[i] - min

    output = A

    digits = int(math.floor(math.log(max - min, radix)+1))
    for i in range(digits):
        output = counting_sort(output,i,radix)

    for i in range(len(output)):
        output[i] = output[i] + min

    return output
