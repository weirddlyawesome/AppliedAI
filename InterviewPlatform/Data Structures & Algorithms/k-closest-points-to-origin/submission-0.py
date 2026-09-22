class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        my_heap = []

        for x, y in points:
            distance = x**2 + y**2
            if len(my_heap) == k and -my_heap[0][0] > distance:
                heapq.heappop(my_heap)
                heapq.heappush(my_heap, (-distance, [x, y]))
            
            if len(my_heap)<k:
                heapq.heappush(my_heap, (-distance, [x, y]))
            
                

            


        return [obj[1] for obj in my_heap]

        