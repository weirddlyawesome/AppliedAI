class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            num = len(string)
            res += str(num) + '#' + string
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        start = 0
        while start < len(s):
            num = ""
            while s[start] != '#':
                num += s[start]
                start += 1

            length = int(num)
            res.append(s[start+1:start +1+length])
            start = start + 1 + length
        return res


