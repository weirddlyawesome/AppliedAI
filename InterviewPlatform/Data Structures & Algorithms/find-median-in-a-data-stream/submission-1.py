class MedianFinder:

    def __init__(self):
        self.max_heap = []  # smaller half, stored as negative
        self.min_heap = []  # larger half

    def addNum(self, num: int) -> None:

        # First decide which half the number belongs to
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        # Balance the heaps
        if len(self.max_heap) - len(self.min_heap) > 1:
            num_ = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, num_)

        if len(self.min_heap) - len(self.max_heap) > 1:
            num_ = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -num_)

    def findMedian(self) -> float:

        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]

        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]

        return (-self.max_heap[0] + self.min_heap[0]) / 2.0