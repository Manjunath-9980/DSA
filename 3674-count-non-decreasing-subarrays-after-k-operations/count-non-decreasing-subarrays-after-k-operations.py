
class Solution:
    def countNonDecreasingSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)

        # Find the next greater element for each position
        nxt = [n] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()

            if stack:
                nxt[i] = stack[-1]

            stack.append(i)

        # Build binary lifting tables
        LOG = n.bit_length()

        up = [nxt]
        sm = [[nums[i] * (nxt[i] - i) for i in range(n)]]

        for j in range(1, LOG):
            prev_up = up[-1]
            prev_sm = sm[-1]

            new_up = [n] * n
            new_sm = [0] * n

            for i in range(n):
                mid = prev_up[i]

                if mid < n:
                    new_up[i] = prev_up[mid]
                    new_sm[i] = prev_sm[i] + prev_sm[mid]

            up.append(new_up)
            sm.append(new_sm)

        # Prefix sums of original array
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        # Calculate the minimum increments for a subarray
        def get_cost(left, right):
            pos = left
            total = 0

            for j in range(LOG - 1, -1, -1):
                nxt_pos = up[j][pos]

                if nxt_pos <= right:
                    total += sm[j][pos]
                    pos = nxt_pos

            total += nums[pos] * (right - pos + 1)

            return total - (prefix[right + 1] - prefix[left])

        # Sliding window
        ans = 0
        right = 0

        for left in range(n):
            while right < n and get_cost(left, right) <= k:
                right += 1

            ans += right - left

        return ans
