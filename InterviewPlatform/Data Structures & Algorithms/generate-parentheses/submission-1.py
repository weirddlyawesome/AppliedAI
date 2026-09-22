class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []

        def dfs(curr, left, right):
            if left > n or right > n:
                return

            if right > left:
                return

            if left == n and right ==n:
                self.res.append(curr)
                return



            left += 1
            curr += "("
            dfs(curr, left, right)

            left -= 1
            curr = curr[:-1] + ")"
            dfs(curr, left, right + 1)

        dfs("", 0, 0)
        return self.res