'''
CS 4720 - Algorithms
24 FEB 2021

Computation / Sorting Time Differences
'''

import time
from timeit import default_timer as timer

# ///////////////////
# ADAPTED PSEUDO CODE
# ///////////////////

def Partition(A, L, R):
    p = A[R]
    i = L - 1

    for j in range(L, R):

        # If A[j] > p, do nothing
        if A[j] <= p:
            # Restore invariant
            i = i + 1

            # Swap
            temp1 = A[j]
            A[j] = A[i]
            A[i] = temp1

    # Swap A[l] and A[i + 1] to place pivot correctly
    temp2 = A[R]
    A[R] = A[i + 1]
    A[i + 1] = temp2

    # Report final pivot position
    return i + 1


# PAGE 127
def QuickSort(A, L, R):
    # 1 or 0 subarray
    if L < R:
        # SINCE WE ARE ONLY DOING THE FIRST ELEMENT, IT'S 0
        # j = new pivot position
        j = Partition(A, L, R)
        # Recurse first part
        QuickSort(A, L, j - 1)
        # Recurse second part
        QuickSort(A, j + 1, R)


def ChoosePivot(A, L, R):
    return 0

# ///////////////////
# FILE IO
# ///////////////////

def read_integers(filename):
    with open(filename) as f:
        return [int(x) for x in f]


# ///////////////////
# MAIN
# ///////////////////

# DATASET 1
print('\n')
print("\\\\\\\\\\\\ DATASET 1 \\\\\\\\\\\\")
arraySetFile = read_integers("dataset1.txt")
start = timer()
QuickSort(arraySetFile, 0, len(arraySetFile) - 1)
end = timer()
print("DATASET 1 USING QUICKSORT:")
print(*arraySetFile, sep=', ')
totalTime = end - start
print("Time Elapsed: " + str(totalTime))

# DATASET 2
print('\n')
print("\\\\\\\\\\\\ DATASET 2 \\\\\\\\\\\\")
arraySetFile = read_integers("dataset2.txt")
start = timer()
QuickSort(arraySetFile, 0, len(arraySetFile) - 1)
end = timer()
print("DATASET 2 USING QUICKSORT:")
print(*arraySetFile, sep='\n')
totalTime = end - start
print("Time Elapsed: " + str(totalTime))

# DATASET 3
print('\n')
print("\\\\\\\\\\\\ DATASET 3 \\\\\\\\\\\\")
arraySetFile = read_integers("dataset3.txt")
start = timer()
QuickSort(arraySetFile, 0, len(arraySetFile) - 1)
end = timer()
print("DATASET 3 USING QUICKSORT:")
print(*arraySetFile, sep=', ')
totalTime = end - start
print("Time Elapsed: " + str(totalTime))

print('\n\n\n\n\n')
# FIN
