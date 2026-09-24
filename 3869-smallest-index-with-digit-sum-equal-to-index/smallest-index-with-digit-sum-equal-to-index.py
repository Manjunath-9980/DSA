class Solution:
    def smallestIndex(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            number = nums[i]
            digit_sum = 0

            while number > 0:
                digit_sum += number % 10
                number //= 10

            if digit_sum == i:
                return i

        return -1