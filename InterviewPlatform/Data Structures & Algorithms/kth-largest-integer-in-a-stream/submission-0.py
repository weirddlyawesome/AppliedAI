class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap_ = nums.copy()
        heapq.heapify(self.heap_)

        while len(self.heap_) >k:
            heapq.heappop(self.heap_)

        
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap_, val)

        while len(self.heap_) >self.k:
            heapq.heappop(self.heap_)

        return self.heap_[0]

        
