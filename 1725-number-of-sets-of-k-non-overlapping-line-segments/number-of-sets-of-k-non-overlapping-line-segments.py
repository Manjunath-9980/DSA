class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        result = 1
        r = 2 * k
        total = n + k - 1

        for i in range(1, r + 1):
            result = result * (total - r + i) // i

        return result % MOD