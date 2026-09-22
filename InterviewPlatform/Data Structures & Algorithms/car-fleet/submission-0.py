class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        trans_ = [(p, s) for p, s in zip(position, speed)]
        trans_.sort(reverse = True)



        stack_ = deque()

        for p, s in trans_:
            new_car_time = (target - p)/s
            stack_.append(new_car_time)
            if len(stack_) >= 2 and stack_[-1] <= stack_[-2]:
                stack_.pop()



        return len(stack_)    