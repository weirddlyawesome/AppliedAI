class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1_dict = self.util_dict(s1)
        for i in range(len(s2) - len(s1)+1):
            if s1_dict == self.util_dict(s2[i:i+len(s1)]):
                return True

        return False


    def util_dict(self, s):
        dict_ = {}
        for i in s:
            dict_[i] = 1 + dict_.get(i, 0)

        return dict_