class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = 0
        people.sort()
        left = 0
        rigth = len(people) - 1
        while left <= rigth:
            if people[left] + people[rigth] <= limit:
                left += 1
            rigth -= 1
            count += 1
        return count