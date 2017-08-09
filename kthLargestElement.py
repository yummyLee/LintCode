class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        quick_sort(self, A, 0, len(A) - 1, k - 1)
        return A[len(A) - k]


def partition(self, A, ll, hh):
    mid = A[ll]
    l = ll
    h = hh
    while l < h:
        while l < h and A[h] >= mid:
            h -= 1
        if l == h:
            break
        else:
            A[l] = A[h]
        while l < h and A[l] < mid:
            l += 1
        if l == h:
            break
        else:
            A[h] = A[l]
    A[l] = mid
    return l


def quick_sort(self, A, l, h, k):
    if l >= h:
        return
    index = Solution.partition(self, A, l, h)
    if k == len(A) - 1 - index:
        return
    elif k > len(A) - 1 - index:
        quick_sort(self, A, l, index - 1, k)
    else:
        quick_sort(self, A, index + 1, h, k)
