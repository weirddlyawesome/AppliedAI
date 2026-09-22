class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        my_heap = [-i for i in stones]
        heapq.heapify(my_heap)

        while len(my_heap) > 1:
            x = heapq.heappop(my_heap)
            y = heapq.heappop(my_heap)

            if x != y:
                heapq.heappush(my_heap, -abs(x-y))


        if len(my_heap) == 0:
            return 0
        else:
            return -my_heap[0]