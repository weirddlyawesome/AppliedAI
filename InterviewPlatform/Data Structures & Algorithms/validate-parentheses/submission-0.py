from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        uti_dic = {'(':')', '{':'}', '[':']'}

        for i in s:
            if i in uti_dic:
                stack.append(i)
            else:
                if not stack or i != uti_dic[stack[-1]]:
                    return False
                stack.pop()

        return not stack


        