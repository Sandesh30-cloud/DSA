class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float('inf')
        result = []
        for i in range(len(arr)-1):
            curr = arr[i+1]-arr[i]
            if curr < min_diff:
                min_diff = curr
                result = [[arr[i], arr[i+1]]]
            elif curr == min_diff:
                result.append([arr[i], arr[i+1]])
        return result
