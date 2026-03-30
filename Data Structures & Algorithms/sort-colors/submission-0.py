class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def merge(arr, l, r, m):
            left = arr[l:m+1]
            right = arr[m+1:r+1]

            i, j, k = 0, 0, l

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
            while i<len(left):
                arr[k] = left[i]
                i += 1
                k+=1
            while j<len(right):
                arr[k] = right[j]
                j += 1
                k+=1
            return arr
        

        def mergeSort(arr, l, r):
            if l >= r:
                return

            m = (l + r) // 2
            mergeSort(arr, l, m)
            mergeSort(arr, m+1, r)
            merge(arr, l, r, m)
        
        mergeSort(nums, 0, len(nums)-1)

