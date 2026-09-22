class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) -1

        while l <r:
            curr_sum = numbers[l] + numbers[r]
            if target == curr_sum:
                return [l+1, r+1]
            elif target < curr_sum:
                r-=1
            else:
                l+= 1

        
