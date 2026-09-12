class Solution:
    def maximumWeight(self, intervals):
        from bisect import bisect_left

        n = len(intervals)

        # Keep the original index with every interval
        intervals = [
            [l, r, w, i]
            for i, (l, r, w) in enumerate(intervals)
        ]

        # Sort by ending point
        intervals.sort(key=lambda x: x[1])

        ends = [x[1] for x in intervals]

        # dp[i][j] = (maximum score, chosen indices)
        # using the first i intervals and choosing at most j
        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            left, right, weight, index = intervals[i - 1]

            # Find intervals that finish before this one starts
            previous = bisect_left(ends, left)

            for j in range(1, 5):

                # Don't choose the current interval
                best_score, best_list = dp[i - 1][j]

                # Choose the current interval
                old_score, old_list = dp[previous][j - 1]

                new_score = old_score + weight
                new_list = sorted(old_list + [index])

                # Pick the better score.
                # If scores are equal, pick smaller indices.
                if new_score > best_score:
                    dp[i][j] = (new_score, new_list)

                elif new_score == best_score and new_list < best_list:
                    dp[i][j] = (new_score, new_list)

                else:
                    dp[i][j] = (best_score, best_list)

        return dp[n][4][1]