from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        result = [[] for i in range(len(nums)+1)]

        for num, cnt in count.items():
            result[cnt].append(num)

        res = []

        for i in range(len(result)-1, 0, -1):
            for num in result[i]:
                res.append(num)
                if len(res) == k:
                    return res
