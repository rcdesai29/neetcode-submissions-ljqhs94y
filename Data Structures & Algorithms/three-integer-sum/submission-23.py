class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums), 1): 
                if nums[i] > nums[j]:
                    temp = nums[j] #the lower one
                    nums[j] = nums[i] #replaceing with the higher
                    nums[i] = temp #replace i with lower
        res = []
        for i,a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            
            l = i +1
            r = len(nums)-1
            while l<r:
                cur = a + nums[l] + nums[r]
                if cur < 0:
                    l+=1
                elif cur > 0:
                    r-=1
                elif cur == 0:
                    res.append([a, nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
        return res