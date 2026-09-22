class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        nums.sort()

        def dfs(i, curr):
            if i > len(nums) - 1:
                self.res.append(curr.copy())
                return

            curr.append(nums[i])
            dfs(i + 1, curr)

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1

            curr.pop()
            dfs(i+1, curr)


        dfs(0, [])
        return self.res
        