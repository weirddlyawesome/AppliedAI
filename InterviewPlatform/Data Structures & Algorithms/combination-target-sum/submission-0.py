class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(subset, sum_, largest_pos):
            if sum_ > target:
                return
            if sum_ == target:
                res.append(subset.copy())
                return

            for i in range(len(nums)):
                if i >= largest_pos:
                    subset.append(nums[i])
                    dfs(subset, sum_ + nums[i], i)
                    subset.pop()



        dfs([], 0, 0)

        return res