class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hashmap = set(nums)
        max_len = 0
        for i in nums:
            max_ = 1
            j = i
            while j + 1 in hashmap:
                max_ += 1
                j += 1

            max_len = max(max_, max_len)

        return max_len

        