class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        

        while l<len(numbers):
            if l+1 <len(numbers):
                r = l+1
            while numbers[l] + numbers[r] != target and r<len(numbers)-1:
                r+=1
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            l+=1