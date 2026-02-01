class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq = Counter(word)
        freq_count = Counter(freq.values())
        if len(freq) == 1:
            return True
        if len(freq_count) == 1:
            return 1 in freq_count
        if len(freq_count) == 2:
            (f1,c1), (f2,c2) = freq_count.items()
            if f1 > f2:
                f1, f2 = f2,f1
                c1,c2 = c2,c1
            if f1 == 1 and c1 ==1:
                return True
            if f2 == f1 +1 and c2 == 1:
                return True
        return False
