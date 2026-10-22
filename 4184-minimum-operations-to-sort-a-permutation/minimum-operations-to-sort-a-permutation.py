class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        start = nums[0]

        forward = True
        backward = True

        for i in range(n):
            if nums[i] != (start + i) % n:
                forward = False

            if nums[i] != (start - i) % n:
                backward = False

        if forward:
            rotations = (n - start) % n
            return min(rotations, n - rotations + 2)

        if backward:
            shift = (start + 1) % n
            return 1 + min(shift, n - shift)

        return -1