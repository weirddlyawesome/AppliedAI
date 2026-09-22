class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        arr = [-1]*(len(edges)+1)

        for edge in edges:
            i = edge[0]
            j = edge[1]

            parent_i = i
            while arr[parent_i] >= 0:
                parent_i = arr[parent_i]
            weight_i = abs(arr[parent_i])
        

            parent_j = j
            while arr[parent_j] >= 0:
                parent_j = arr[parent_j]

            weight_j = abs(arr[parent_j])

            if parent_i == parent_j:
                return [i, j]
            else:
                if weight_i >= weight_j:
                    arr[parent_i] = -(weight_i + weight_j)
                    arr[parent_j] = parent_i
                else:
                    arr[parent_j] = -(weight_i + weight_j)
                    arr[parent_i] = parent_j
