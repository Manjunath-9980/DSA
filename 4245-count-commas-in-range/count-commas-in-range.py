class Solution:
    def countCommas(self, n: int) -> int:
        count = 0
        num = 1000

        while num <= n:
            last = min(n, num * 1000 - 1)
            count += last - num + 1
            num *= 1000

        return count