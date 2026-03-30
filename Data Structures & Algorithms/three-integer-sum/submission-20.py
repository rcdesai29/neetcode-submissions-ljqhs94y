class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        l = 0
        while l < len(nums):
            if l>0 and nums[l] == nums[l-1]:
                l +=1
                continue
            
            a = l+1
            r = len(nums)-1

            while a < r:
                cur = nums[l] + nums[a] + nums[r]
                if cur < 0:
                    a+=1
                elif cur > 0:
                    r-=1
                elif cur == 0:
                    res.append([nums[l],nums[a],nums[r]])
                    a+=1
                    r-=1
                    while a < r and nums[a] == nums[a-1]:
                        a+=1
            l+=1
        return res

