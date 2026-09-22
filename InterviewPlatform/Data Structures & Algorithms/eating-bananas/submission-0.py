import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # number of bananas = piles[i]
        # OUTPUT - k bananas per hour return minimum k

        # CONSTRAINT - hours to eat all bananas = h

        k_max = max(piles)

        k_min = 1

        while k_min <= k_max:
            mid = (k_min + k_max )//2
            t = self.utility(piles, mid)
            if t > h:
                k_min = mid + 1
            else:
                ans =  mid
                k_max = mid - 1

        return ans


            



    def utility(self, piles, k):
        t = 0

        for i in piles:
            t += math.ceil(i/k)

        return t
        