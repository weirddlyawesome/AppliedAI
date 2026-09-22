class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            if i >0 and nums[i-1] == nums[i]:
                continue
            l = i + 1
            r = len(nums) - 1

            while l < r:
                sum_ = nums[l] + nums[r] + nums[i]
                if sum_ == 0 :
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1 # always do the dry run
                    r -= 1
                    
                    while l <r and nums[l] == nums[l-1]:
                        l += 1
                    while l <r and nums[r] == nums[r+1]:
                        r -=1
                if sum_ <0:
                    l += 1
                if sum_ >0:
                     r-=1


        return res


        