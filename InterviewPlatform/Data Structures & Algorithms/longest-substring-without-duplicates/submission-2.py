class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict_ = defaultdict()
        i = 0
        j = 0
        max_len = 0
        while j < len(s):
            if s[j] in dict_ and dict_[s[j]] >= i:
                max_len = max(max_len, j - i)
                i = dict_[s[j]] + 1
                
            dict_[s[j]] = j
            j += 1
            max_len = max(max_len, j -i)

        return max_len

        


