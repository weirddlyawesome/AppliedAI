class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        hashmap = set(nums)
        memo = defaultdict(int)
        max_len = 0
        for i in hashmap:
            if i-1 not in hashmap:
                max_ = 1
                j = i
                while j+1 in hashmap:
                    if j+1 in memo:
                        max_ += memo[j+1]
                        break
                    else:
                        max_ += 1
                        j += 1

                memo[i] = max_
                max_len = max(max_, max_len)

        return max_len