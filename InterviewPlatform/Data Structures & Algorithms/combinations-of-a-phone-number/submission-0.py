class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.mapping = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        self.res = []

        def dfs(digits, curr_string):
            if not digits:
                self.res.append(curr_string)
                return

            for i in range(len(self.mapping[digits[0]])):
                curr_string += self.mapping[digits[0]][i]
                dfs(digits[1:], curr_string)

                curr_string = curr_string[:-1]


        dfs(digits, "")

        return self.res