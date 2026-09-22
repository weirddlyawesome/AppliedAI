class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        my_heap = []

        for i in nums:
            heapq.heappush(my_heap, i)

            if len(my_heap) > k:
                heapq.heappop(my_heap)

            
        return heapq.heappop(my_heap)