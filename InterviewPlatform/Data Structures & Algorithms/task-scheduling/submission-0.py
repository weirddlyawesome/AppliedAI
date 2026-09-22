class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dict_ = {}
        my_heap = []
        q = deque()

        for task in tasks:
            dict_[task] = dict_.get(task, 0) -1

        for key, value in dict_.items():
            heapq.heappush(my_heap, (value, key))


        time = 0

        while q or my_heap:
            time += 1
            if my_heap:
                neg_freq, task = heapq.heappop(my_heap)
                neg_freq += 1
                if neg_freq != 0:
                    q.append((neg_freq, task, time + n))

            if q and q[0][2] == time:
                neg_freq, task, _ = q.popleft()
                heapq.heappush(my_heap, (neg_freq, task))


        return time


