class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        before_ = [0]*len(nums)
        after_ = [0]*len(nums)
        before, after = 1, 1
        for i, num in enumerate(nums):
            before_[i] = before
            before = before*num

        for i in range(len(nums) -1, -1, -1):
            after_[i] = after
            after *=nums[i]

        res = []
        for i in range(len(nums)):
            res.append(before_[i]*after_[i])


        return res
                    