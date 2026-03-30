class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums.sort()

        l = 0
        r = len(nums)-1
        while l<=r:
            mid = l + ((r-l)//2)
            midValue = nums[mid]

            if midValue < target:
                l+=1
            elif midValue > target:
                r-=1
            else:
                return mid
        return -1