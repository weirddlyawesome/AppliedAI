class MedianFinder:

    def __init__(self):
        self.arr = []
        

    def addNum(self, num: int) -> None:
        flag = True
        for i in range(len(self.arr)):
            if self.arr[i] > num:
                self.arr.insert(i, num)
                flag = False
                break
        if flag:
                self.arr.append(num)


        

    def findMedian(self) -> float:
        length = len(self.arr)
        if length%2:
            return self.arr[length//2]
        else:
            return (self.arr[length//2] + self.arr[length//2 -1])/2.0
        
        