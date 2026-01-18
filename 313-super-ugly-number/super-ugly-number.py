class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [1]
        idx = [0] * len(primes)

        for _ in range(n - 1):
            next_val = min(ugly[idx[i]] * primes[i] for i in range(len(primes)))
            ugly.append(next_val)

            for i in range(len(primes)):
                if ugly[idx[i]] * primes[i] == next_val:
                    idx[i] += 1

        return ugly[-1]
            