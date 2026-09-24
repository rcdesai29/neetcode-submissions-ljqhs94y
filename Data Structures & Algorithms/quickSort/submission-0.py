# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs) -1)
        return pairs
    
    def quickSortHelper(self, arr, start, end):
        if end - start <= 0:
            return 
        
        pivot = arr[end] # pivot is the last element
        left = start # pointer for left side

        #Parititon: elements smaller than pivot on left side
        for i in range(start, end):
            if arr[i].key < pivot.key:
                temp = arr[left]
                arr[left] = arr[i]
                arr[i] = temp
                left += 1

        arr[end] = arr[left]     
        arr[left] = pivot

        self.quickSortHelper(arr, start, left - 1)
        self.quickSortHelper(arr, left + 1, end)