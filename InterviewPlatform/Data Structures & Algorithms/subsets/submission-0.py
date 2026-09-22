class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        self.nums = nums
        self.r = len(nums) - 1
        self.res = set()
        
        def find_subsets(pos, curr_combination):
            #boundary
            if pos >self.r:
                self.res.add(tuple(curr_combination))
                return

            #case1: exclude number at pos
            find_subsets(pos+1, curr_combination)

            #case2: include number at pos
            new_list = curr_combination.copy()
            new_list.append(self.nums[pos])
            find_subsets(pos+1, new_list)


        find_subsets(0, [])

        res = []
        for t in self.res:
            res.append(list(t))

        return res

