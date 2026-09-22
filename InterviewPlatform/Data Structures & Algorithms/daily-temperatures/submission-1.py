class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack_ = deque()

        for idx, temp in enumerate(temperatures):
            current_temp = temp
            while stack_ and current_temp > stack_[-1][1]:
                idx_e, _ = stack_.pop()
                result[idx_e] = idx- idx_e

            stack_.append((idx, temp))
        return result
        