
class Solution:
    def minMoves(self, nums: list[int]) -> int:
        largest = max(nums)
        moves = 0

        for num in nums:
            moves += largest - num

        return moves
