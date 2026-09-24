# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs)-1)
    
    def mergeSortHelper(self, pairs, start, end):
        if end - start + 1 <= 1:
            return pairs
        
        M = (end + start) // 2

        self.mergeSortHelper(pairs, start, M)
        self.mergeSortHelper(pairs, M+1, end)

        #merge sorted halfs
        self.merge(pairs, start, M, end)
        return pairs

    def merge(self, arr, start, mid, end):
        left = arr[start : mid+1]
        right = arr[mid+1 : end+1]

        i = 0 # index for L
        j = 0 # index for R
        k = start # index for arr

        while i < len(left) and j < len(right):
            if left[i].key <= right[j].key:
                arr[k] = left[i]
                i +=1 
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1