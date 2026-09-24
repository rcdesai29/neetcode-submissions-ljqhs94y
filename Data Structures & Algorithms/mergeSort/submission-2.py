# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeHelper(pairs, 0, len(pairs)-1)

    def mergeHelper(self, pairs, start, end):
        if end - start <= 0:
            return pairs
        
        mid = (start + end) // 2

        #left side
        self.mergeHelper(pairs, start, mid)

        #right side
        self.mergeHelper(pairs, mid +1, end)

        #merge both side
        self.merge(pairs, start, mid, end)

        return pairs
    
    def merge(self, arr, start, mid, end):
        
        left = arr[start : mid + 1]
        right = arr[mid + 1 : end + 1]

        i = 0
        j = 0
        k = start

        while i < len(left) and j < len(right):
            if left[i].key <= right[j].key:
                arr[k] = left[i]
                i += 1
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
        


             
