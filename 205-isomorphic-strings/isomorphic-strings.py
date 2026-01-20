class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_1 = []
        map_2 = []
        for i in s:
            map_1.append(s.index(i))
        for i in t:
            map_2.append(t.index(i))
        if map_1 == map_2:
            return True
        return False