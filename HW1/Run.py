'''
CS 4720 - Algorithms
01 MAR 2021

Inversions / Split Inversions
'''


# ///////////////////
# ADAPTED
# ///////////////////


def sort_and_countInv(arrayA):
    n = len(arrayA)
    if n == 0 or n == 1:
        return arrayA, 0
    else:

        mid = int(len(arrayA) // 2)
        left = arrayA[:mid]
        right = arrayA[mid:]

        arrayC, leftInv = sort_and_countInv(left)
        arrayD, rightInv = sort_and_countInv(right)
        arrayB, splitInv = merge_and_countSplitInv(arrayC, arrayD)

        totalInv = leftInv + rightInv + splitInv

        # DEBUG LINE
        print("Inversions: T: " + str(totalInv) + " L: " + str(leftInv) + " R: " + str(rightInv) + " S: " + str(splitInv))

        return arrayB, totalInv


def merge_and_countSplitInv(aC, aD):
    n = len(aC) + len(aD)
    splitInversions = 0
    i = 0
    j = 0
    k = 0
    aB = []

    while k < n:
        if (i < len(aC)) and (j < len(aD)):

            if aC[i] < aD[j]:
                aB.append(aC[i])
                i = i + 1
                k = k + 1

            else:
                aB.append(aD[j])
                j = j + 1
                splitInversions = splitInversions + ((len(aC) // 2) - i + 1)
                k = k + 1
                
        if (i >= len(aC)) and (j < len(aD)):
            while j < len(aD):
                aB.append(aD[j])
                j = j + 1
                k = k + 1

        if (j >= len(aD)) and (i < len(aC)):
            while i < len(aC):
                aB.append(aC[i])
                i = i + 1
                k = k + 1

    return aB, splitInversions


# ///////////////////
# MAIN
# ///////////////////


# The first list of arrays for the problem:
# 28 INVERSIONS
dataset1 = [[5, 4, 0, 4, 4], [1, 4, 1, 0, 8], [7, 9, 2, 9, 4], [2, 9, 6, 4, 9], [2, 5, 2, 6, 0], [6, 0, 6, 6, 0],
            [2, 9, 9, 5], [5, 3, 7, 7, 7], [4, 9, 6, 8, 9], [9, 0, 8, 3]]

# FIRST DATA SET
totalInversions = 0

for arrays in dataset1:
    arrays1, inversionCount = sort_and_countInv(arrays)
    totalInversions = inversionCount + totalInversions
    print("Inversions: " + str(inversionCount) + '\t Sorted Array: ' + str(arrays1) + '\n')

print('\nTotal Inversions: ' + str(totalInversions))
