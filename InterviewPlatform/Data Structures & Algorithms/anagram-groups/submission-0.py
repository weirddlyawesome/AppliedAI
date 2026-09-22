class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for i,string in enumerate(strs):
            key = self.utility_conv2tuple(string)
            hashmap[key].append(string)


        return list(hashmap.values())




    def utility_conv2tuple(self, string):
        arr = [0]*26
        for i in string:
            arr[ord(i)-ord('a')] += 1

        return tuple(arr)