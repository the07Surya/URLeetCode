class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        def findKth(i: int, j: int, k: int) -> float:
            if i >= m:
                return nums2[j + k - 1]
            if j >= n:
                return nums1[i + k - 1]
            if k == 1:
                return min(nums1[i], nums2[j])

            # Division a // b :  floordiv(a, b)
            midVal1 = nums1[i + k // 2 - 1] if i + k // 2 - 1 < m else math.inf
            midVal2 = nums2[j + k // 2 - 1] if j + k // 2 - 1 < n else math.inf

            if midVal1 < midVal2:
                return findKth(i + k // 2, j, k - k // 2) # '+' or '-' k//2
            else:
                return findKth(i, j + k // 2, k - k // 2)

        m = len(nums1)
        n = len(nums2)
        # Division a // b :  floordiv(a, b)
        left = (m + n + 1) // 2 
        right = (m + n + 2) // 2
        return (findKth(0, 0, left) + findKth(0, 0, right)) / 2.0

############

class Solution(object):
  def findMedianSortedArrays(self, nums1, nums2):
    a, b = sorted((nums1, nums2), key=len)
    m, n = len(a), len(b)
    after = (m + n - 1) / 2
    lo, hi = 0, m
    while lo < hi:
      i = (lo + hi) / 2
      if after - i - 1 < 0 or a[i] >= b[after - i - 1]:
        hi = i
      else:
        lo = i + 1
    i = lo
    nextfew = sorted(a[i:i + 2] + b[after - i:after - i + 2])
    return (nextfew[0] + nextfew[1 - (m + n) % 2]) / 2.0
