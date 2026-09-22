class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        arr = [-1]*n

        for i, j in edges:
            parent_i = i

            while arr[parent_i] >=0:
                parent_i = arr[parent_i]


            weight_i = abs(arr[parent_i])


            parent_j = j

            while arr[parent_j] >= 0:
                parent_j = arr[parent_j]

            weight_j = abs(arr[parent_j])

            if parent_i == parent_j:
                continue
            else:
                if weight_i >= weight_j:
                    arr[parent_i] = -(weight_i + weight_j)
                    arr[parent_j] = parent_i
                else:
                    arr[parent_j] = -(weight_i + weight_j)
                    arr[parent_i] = parent_j


        res = 0
        for i in arr:
            if i <0:
                res += 1


        return res



            
        