class Solution:
    def partition(self, s: str) -> List[List[str]]:

        self.res = []

        def solution(string, curr_list):
            if not string:
                self.res.append(curr_list[:])
                return


            for i in range(1, len(string) +1):
                if self.is_palindrome(string[:i]):
                    curr_list.append(string[:i])
                    solution(string[i:], curr_list)
                    curr_list.pop()
        
        solution(s, [])
        return self.res


    def is_palindrome(self, string):
        if not string:
            return True
            
        if string == string[::-1]:
            return True

        return False        