class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, curr, curr_sum):
            if curr_sum == target:
                res.append(curr.copy())
                return

            if i == len(candidates) or candidates[i] > target - curr_sum:
                return


            
            curr.append(candidates[i])
            dfs(i+1, curr, curr_sum + candidates[i])

            curr.pop()
            
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1

            dfs(i +1, curr, curr_sum)



        dfs(0, [], 0)

        return res