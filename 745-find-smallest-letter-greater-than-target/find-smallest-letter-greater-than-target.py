class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        result = letters[0]
        flag = False
        for l in letters:
            if not flag:
                if l > target:
                    result = l
                    flag = not flag
                else:
                    if l > target and l < result:
                        result = l
        return result