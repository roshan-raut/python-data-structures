"""
We wish to determine the optimal way in which to assign tasks to some workers.
Each worker must work on exactly two tasks.
Tasks are independent of each other, and each task takes a certain amount of time.

we have been given an array of tasks where the value of each element in the array
corresponds to the number of hours required for each task.

In the greedy approach, we’ll focus on the following rule:
    -Pair the longest task with the shortest one.
"""

A = A = [6, 3, 2, 7, 5, 5]

A = sorted(A)

for i in range(len(A)//2):
    print(A[i], A[~i])