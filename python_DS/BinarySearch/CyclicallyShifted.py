# An array is “cyclically shifted” if it is possible to shift its entries cyclically so that it becomes sorted.

# You are required to write a function that determines
# the index of the smallest element of the cyclically shifted array.


def find(A):
    low = 0
    high = len(A) - 1

    while low < high:
        mid = (low + high)//2

        if A[mid] > A[high]:
            low = mid + 1
        elif A[mid] <= A[high]:
            high = mid

    return low


A = [4, 5, 6, 7, 1, 2, 3]
idx = find(A)
print(A[idx])
