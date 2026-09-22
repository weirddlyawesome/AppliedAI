class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        arr = [0]*26

        for i in s:
            arr[ord(i) - ord('a')] += 1

        for i in t:
            index = ord(i) - ord('a')

            if arr[index] == 0:
                return False

            arr[index] -= 1

        return not sum(arr)