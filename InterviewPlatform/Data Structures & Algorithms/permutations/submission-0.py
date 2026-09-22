class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack([], [False]*len(nums), nums)
        return self.res

    def backtrack(self, curr_perm, pick, nums):
        if len(curr_perm) == len(nums):
            self.res.append(curr_perm[:])
            return

        for i in range(len(nums)):
            if not pick[i]:
                curr_perm.append(nums[i])
                pick[i] = True
                self.backtrack(curr_perm, pick, nums)

                pick[i] = False
                curr_perm.pop()





        