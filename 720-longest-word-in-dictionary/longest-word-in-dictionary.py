class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        valid = set([""])
        longest = ""
        for w in words:
            if w[:-1] in valid:
                valid.add(w)
                if len(w) > len(longest):
                    longest = w
        return longest
