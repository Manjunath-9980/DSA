
class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        total = 0

        for i in range(len(nums)):
            seen = set()

            for j in range(i, len(nums)):
                seen.add(nums[j])
                count = len(seen)
                total += count * count

        return total
