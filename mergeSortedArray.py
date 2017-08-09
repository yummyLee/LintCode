class Solution:
    # @param A and B: sorted integer array A and B.
    # @return: A new sorted integer array
    def mergeSortedArray(self, A, B):
        # write your code here
        C = list()
        len_a = len(A)
        len_b = len(B)
        index_a = 0
        index_b = 0
        while index_a < len_a and index_b < len_b:
            if A[index_a] >= B[index_b]:
                C.append(A[index_a])
                index_a += 1
            else:
                C.append(B[index_b])
                index_b += 1
            while index_a < len_a:
                C.append(A[index_a])
                index_a += 1
            while index_b < len_b:
                C.append(B[index_b])
                index_b += 1
        return C
