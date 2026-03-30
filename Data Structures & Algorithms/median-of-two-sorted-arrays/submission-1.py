class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = nums1
        b = nums2
        total = len(a)+len(b)
        half = total // 2
        
        if len(b) < len(a):
            a,b = b, a

        l, r = 0, len(a) -1
        while True:
            i = (l+r)//2 # a
            j = half - i - 2 # b

            aLeft = a[i] if i>=0 else float('-infinity')
            aRight = a[i+1] if i+1<len(a) else float('infinity')
            bLeft = b[j] if j>=0 else float("-infinity")
            bRight = b[j+ 1] if j+1<len(b) else float('infinity')

            if aLeft <= bRight and bLeft <= aRight:
                #odd
                if total % 2 != 0:
                    return (min(aRight, bRight))
                else:
                    return ((min(aRight, bRight) + max(aLeft, bLeft))/2)
            elif aLeft > bRight:
                r = i - 1
            else:
                l = i + 1
