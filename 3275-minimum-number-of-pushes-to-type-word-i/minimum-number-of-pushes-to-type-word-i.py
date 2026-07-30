class Solution:
    def minimumPushes(self, word: str) -> int:
        push = 0
        for i in range(len(word)):
            push += i // 8+1
        return push