from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.key_dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.key_dict:
            return ""

        arr = self.key_dict[key]

        l, r = 0, len(arr) - 1
        ans = ""

        while l <= r:
            mid = (l + r) // 2

            if arr[mid][0] == timestamp:
                return arr[mid][1]
            elif arr[mid][0] < timestamp:
                ans = arr[mid][1]
                l = mid + 1
            else:
                r = mid - 1

        return ans