"""
The set function in Python operates on a list and returns a set object that contains the unique elements of that list
intersection returns a set which is the intersection of A and B. The method intersection is a member of the Set class,
but it can accept lists as arguments too. This solution is fine considering it works on unsorted arrays as well.
"""

A = [2, 3, 3, 5, 7, 11]
B = [3, 3, 7, 15, 31]

print(set(A).intersection(B))


def intersect_sorted_arrays(A,B):
    i = 0
    j = 0
    intersection = []
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if i == 0 or A[i] != A[i-1]:
                intersection.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    return intersection


A = [2, 3, 3, 5, 7, 11]
B = [3, 3, 7, 15, 31]

print(intersect_sorted_arrays(A, B))