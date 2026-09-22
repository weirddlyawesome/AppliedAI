class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        edge_set = set()
        arr = [-1]*n

        for i, j in edges:
            
            # finding parents

            parent_i = i

            while arr[parent_i] >=0:
                parent_i = arr[parent_i]

            weight_i = abs(arr[parent_i])


            parent_j = j

            while arr[parent_j] >=0:
                parent_j = arr[parent_j]

            weight_j = abs(arr[parent_j])

            if parent_i == parent_j:
                return False

            if weight_i >= weight_j:
                arr[parent_i] = -(weight_i + weight_j)
                arr[parent_j] = parent_i
            else:
                arr[parent_j] = -(weight_i + weight_j)
                arr[parent_i] = parent_j

            edge_set.add((i, j))


        return len(edge_set) == n-1


                

                


        