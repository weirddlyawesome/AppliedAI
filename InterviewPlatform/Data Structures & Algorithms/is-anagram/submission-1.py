class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if self.create_dict(s) != self.create_dict(t):
            return False

        return True
        

    def create_dict(self, s: str) -> dict:
        dict_rep = {}

        for i in s:
            dict_rep[i] = 1 + dict_rep.get(i, 0)

        return dict_rep
            
        