"""
Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].
"""

def flipAndInvertImage(A):
    """
    For the list of matrices:
    - reverse the order of values in each matrix
    - inverse the binary value
    - return the new list of matrices
    """

    # iterate through the list  `A` to reverse the elements in each matrix
    for i, n in enumerate(A):
        A[i] = A[i][::-1]
    
    # iterate again through the reversed matrix to swap out 1's with 0's and 0's with 1's
    for i, n in enumerate(A):
        for j, m in enumerate(n):
            if m is 0:
                n[j] = 1
            if m is 1:
                n[j] = 0
    
    return A

test = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
flipAndInvertImage(test)

"""
TIME & SPACE COMPLEXITY

TIME: O(n²)

There is a nested for loop used to replace the elements in the list of reversed matrices, giving this solution a general runtime of O(n²).

SPACE: O(1)

The solution does not use any additional data structures to store values. It consists of swapping values using the given input list instead.
"""