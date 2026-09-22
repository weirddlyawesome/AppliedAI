class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {nums[i]:i for i in range(len(nums))}

        for i, num1 in enumerate(nums):
            query = target - num1
            if query in hashmap and hashmap[query] != i:
                return [i, hashmap[query]]
        